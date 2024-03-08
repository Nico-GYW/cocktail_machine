import PyCmdMessenger
import serial.tools.list_ports
import time
import threading

# Initialize an ArduinoBoard instance.  

def find_arduino(pid):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.pid == pid:
            return port.device
    return None

# PID
arduino_uno_pid = 0x0043

port_uno = find_arduino(arduino_uno_pid)

arduino_uno = PyCmdMessenger.ArduinoBoard(port_uno, baud_rate=9600)


commands_uno = [
    ["cmd_SERVO_dispenser", "ii"], # Move StepperMotorX to a specific positiimon
    ["cmd_SERVO_dispenser_setting", "iii"], # Initiate homing sequence for StepperMotorX
    ["cmd_SERVO_dispenser_stop", "i"], # Stop StepperMotorX immediately
    ["cmd_SERVO_dispenser_animation", "iiii"],

    ["cmd_SERVO_lemonBowl_open", ""],
    ["cmd_SERVO_lemonBowl_close", ""],
    ["cmd_SERVO_lemonBowl_setting", "iii"],
    ["cmd_SERVO_lemonBowl_is_open", ""],

    ["cmd_SERVO_lemonRamp_release", ""],
    ["cmd_SERVO_lemonRamp_down", ""],
    ["cmd_SERVO_lemonRamp_up", ""],
    ["cmd_SERVO_lemonRamp_custo", "i"],
    ["cmd_SERVO_lemonRamp_setting", "iiiii"],

    ["cmd_SERVO_handler_move", "ii"], 
    ["cmd_SERVO_handler_stop", ""],

    ["cmd_VALVE_open", "ii"],
    ["cmd_VALVE_close", "i"],
    ["cmd_VALVE_stop", "i"], 

    ["cmd_EC_forward", "i"],
    ["cmd_EC_backward", "i"],
    ["cmd_EC_stop", ""],

    ["cmd_ack","s"] # Acknowledge a command,
]

# Initialize the messenger
cmd_arduino_uno = PyCmdMessenger.CmdMessenger(arduino_uno, commands_uno)

class Controller:
    def __init__(self, cmd_arduino):
        self.cmd = cmd_arduino
        
class DispenserController(Controller):

    def __init__(self):
        super().__init__(cmd_arduino_uno)

    def activate_dispenser(self, dispenser_index: int, release_time: int):
        """
        Active un distributeur spécifique. Si release_time est 0 ou négatif, 
        le distributeur passe en mode idle après avoir monté. 
        Sinon, il effectue une action de libération après un délai spécifié.
        """
        self.cmd.send("cmd_SERVO_dispenser", dispenser_index, release_time)
        msg = self.cmd.receive()
        print(msg)

    def set_dispenser_settings(self, position_max: int, t_max: int, position_release: int):
        self.cmd.send("cmd_SERVO_dispenser_setting", position_max, t_max, position_release)
        msg = self.cmd.receive()
        print(msg)

    def stop_dispenser(self, dispenser_index: int):
        self.cmd.send("cmd_SERVO_dispenser_stop", dispenser_index)
        msg = self.cmd.receive()
        print(msg)

    def animate_dispensers(self, speed: int, position_max: int, delay_factor: int):
        for i in range(8):
            self.cmd.send("cmd_SERVO_dispenser_animation", speed, position_max, delay_factor * i, i)
            msg = self.cmd.receive()
            print(msg)

    
class ServoHandler(Controller):

    def __init__(self):
        super().__init__(cmd_arduino_uno)

    def move(self, position, id):
        self.cmd.send("cmd_SERVO_handler_move", position, id)
        msg = self.cmd.receive()
        print(f"Servo {id if id <= 15 else 'All'} stopped at position {position}: {msg}")

    def stop(self):
        self.cmd.send("cmd_SERVO_handler_stop")
        msg = self.cmd.receive()
        print("Servos stopped: " + msg)


class DCValveController(Controller):

    def __init__(self):
        super().__init__(cmd_arduino_uno)

    def open_valve(self, valve_index: int, release_time: int):
        """
        Ouvre une vanne spécifique. Si release_time est 0, la vanne reste ouverte indéfiniment.
        Sinon, elle reste ouverte pendant release_time millisecondes.
        """
        self.cmd.send("cmd_VALVE_open", valve_index, release_time)
        msg = self.cmd.receive()
        print(msg)

    def close_valve(self, valve_index: int):
        """
        Ferme une vanne spécifique.
        """
        self.cmd.send("cmd_VALVE_close", valve_index)
        msg = self.cmd.receive()
        print(msg)

    def stop_all_valves(self):
        """
        Ferme toutes les vannes.
        """
        self.cmd.send("cmd_VALVE_stop")
        msg = self.cmd.receive()
        print(msg)

class ElectricCylinderController(Controller):
    FULL_CYCLE_DURATION = 7800  # Temps nécessaire pour faire une course complète du cylindre en ms

    def __init__(self):
        super().__init__(cmd_arduino_uno)
        self.interrupt = threading.Event()
        self.lock = threading.Lock()  # Verrou pour synchroniser l'accès au port série
        self.position = 0
        self.current_process = None

    def move_forward(self, duration: int):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_forward", duration)
            msg = self.cmd.receive()
            print(msg)

    def move_backward(self, duration: int):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_backward", duration)
            msg = self.cmd.receive()
            print(msg)

    def go_home(self):
        with self.lock:  # Applique le verrou ici aussi si nécessaire
            self.move_backward(self.FULL_CYCLE_DURATION + 500)
            self.position = 0
            # Pas besoin de recevoir ici si move_backward s'en occupe déjà

    def stop(self):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_stop")
            msg = self.cmd.receive()
            print(msg)

    def go_home_async(self):
        def run():
            with self.lock:  # Assurez-vous que cette section est protégée
                self.current_process = "go_home_async"
                self.move_backward(self.FULL_CYCLE_DURATION + 500)
                time.sleep((self.FULL_CYCLE_DURATION + 500) / 1000)
                if not self.interrupt.is_set():
                    self.position = 0
                self.interrupt.clear()
                self.current_process = None
                self.stop()

        threading.Thread(target=run).start()

    def press_lemon_async(self, cycle_number: int):
        def run():
            DELAY = 1000
            INITIAL_ADVANCE_DURATION = self.FULL_CYCLE_DURATION - DELAY
            BACK_AND_FORTH_DURATION = 200

            with self.lock:  # Protège également cette section d'exécution
                self.current_process = "press_lemon_async"
                self.move_forward(INITIAL_ADVANCE_DURATION)
                time.sleep(INITIAL_ADVANCE_DURATION / 1000)

                if self.position != 0:
                    self.go_home_async()
                    # Attendez le retour à la position initiale
                    time.sleep((self.FULL_CYCLE_DURATION + 500) / 1000)

                for _ in range(cycle_number):
                    if self.interrupt.is_set():
                        break
                    self.move_backward(BACK_AND_FORTH_DURATION)
                    time.sleep(BACK_AND_FORTH_DURATION / 1000)
                    self.move_forward(BACK_AND_FORTH_DURATION + DELAY)
                    time.sleep((BACK_AND_FORTH_DURATION + DELAY) / 1000)

                self.interrupt.clear()
                self.current_process = None
                if not self.interrupt.is_set():
                    self.go_home()

        threading.Thread(target=run).start()

    def stop_process(self):
        """
        Arrête le processus en cours et active le callback adéquat.
        """
        with self.lock:
            self.interrupt.set()
            # Attendre un peu pour s'assurer que le processus vérifie l'interruption
            time.sleep(0.1)
            if self.current_process == "go_home_async":
                self.stop()
            elif self.current_process == "press_lemon_async":
                self.go_home()
            self.current_process = None

class LemonBowlController(Controller):
    def __init__(self):
        super().__init__(cmd_arduino_uno)

    def open_bowl(self):
        """
        Ouvre le Lemon Bowl.
        """
        self.cmd.send("cmd_SERVO_lemonBowl_open")
        msg = self.cmd.receive()
        print(msg)

    def close_bowl(self):
        """
        Ferme le Lemon Bowl.
        """
        self.cmd.send("cmd_SERVO_lemonBowl_close")
        msg = self.cmd.receive()
        print(msg)

    def set_bowl_params(self, positionOpen: int, positionClosed: int, speed: int):
        """
        Configure les paramètres du Lemon Bowl.
        """
        self.cmd.send("cmd_SERVO_lemonBowl_setting", positionOpen, positionClosed, speed)
        msg = self.cmd.receive()
        print(msg)

    def is_bowl_open(self):
        """
        Vérifie si le Lemon Bowl est ouvert.
        """
        self.cmd.send("cmd_SERVO_lemonBowl_is_open")
        msg = self.cmd.receive()
        print(msg)

class LemonRampController(Controller):
    def __init__(self):
        super().__init__(cmd_arduino_uno)

    def release_lemon(self):
        """
        Exécute la séquence pour libérer un citron sur la rampe.
        """
        self.cmd.send("cmd_SERVO_lemonRamp_release")
        msg = self.cmd.receive()
        print(msg)

    def move_down(self):
        """
        Déplace le ramp uniquement vers le bas.
        """
        self.cmd.send("cmd_SERVO_lemonRamp_down")
        msg = self.cmd.receive()
        print(msg)

    def move_up(self):
        """
        Déplace le ramp uniquement vers le haut.
        """
        self.cmd.send("cmd_SERVO_lemonRamp_up")
        msg = self.cmd.receive()
        print(msg)

    def custom_position(self, position: int):
        """
        Déplace le ramp à une position personnalisée.
        """
        self.cmd.send("cmd_SERVO_lemonRamp_custo", position)
        msg = self.cmd.receive()
        print(msg)

    def set_ramp_settings(self, positionDown: int, positionUp: int, speed: int, downWaitDelay: int, upWaitDelay: int):
        """
        Configure les paramètres du ramp.
        """
        self.cmd.send("cmd_SERVO_lemonRamp_setting", positionDown, positionUp, speed, downWaitDelay, upWaitDelay)
        msg = self.cmd.receive()
        print(msg)
