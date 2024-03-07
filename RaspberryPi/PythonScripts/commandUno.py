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
    FULL_CYCLE_DURATION = 8000  # Temps nécessaire pour faire une course complète du cylindre en ms

    def __init__(self):
        super().__init__(cmd_arduino_uno)
        self.interrupt = threading.Event()

    def move_forward(self, duration: int):
        """
        Commande le vérin électrique pour avancer pendant une durée spécifiée.
        """
        self.cmd.send("cmd_EC_forward", duration)
        msg = self.cmd.receive()
        print(msg)

    def move_backward(self, duration: int):
        """
        Commande le vérin électrique pour reculer pendant une durée spécifiée.
        """
        self.cmd.send("cmd_EC_backward", duration)
        msg = self.cmd.receive()
        print(msg)

    def go_home(self):
        """
        Fait reculer le vérin pendant le temps nécessaire pour revenir à la position de départ.
        """
        self.move_backward(self.FULL_CYCLE_DURATION)

    def stop(self):
        """
        Arrête le vérin électrique et le met en état d'arrêt (idle).
        """
        self.cmd.send("cmd_EC_stop")
        msg = self.cmd.receive()
        print(msg)

    def press_lemon_async(self, cycle_number: int, callback=None):
        """
        Version asynchrone de press_lemon pour être utilisée avec l'interface graphique.
        """
        def run():
            DELAY = 1000
            INITIAL_ADVANCE_DURATION = self.FULL_CYCLE_DURATION - DELAY
            BACK_AND_FORTH_DURATION = 200

            self.move_forward(INITIAL_ADVANCE_DURATION)
            time.sleep(INITIAL_ADVANCE_DURATION / 1000)  # Convertir ms en s

            for _ in range(cycle_number):
                if self.interrupt.is_set():
                    break
                self.move_backward(BACK_AND_FORTH_DURATION)
                time.sleep(BACK_AND_FORTH_DURATION / 1000)
                self.move_forward(BACK_AND_FORTH_DURATION + DELAY)
                time.sleep((BACK_AND_FORTH_DURATION + DELAY) / 1000)

            if callback:
                callback()

        threading.Thread(target=run).start()

    def stop_process(self):
        """
        Méthode pour interrompre le processus en cours.
        """
        self.interrupt.set()
        self.stop()  # Envoyer la commande d'arrêt à l'Arduino

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
