import PyCmdMessenger
import serial.tools.list_ports
import time

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
    ["cmd_SERVO_handler_move", "ii"], 
    ["cmd_SERVO_handler_stop", ""],
    ["cmd_VALVE_open", "ii"], # 
    ["cmd_VALVE_close", "i"], # Get the current state of StepperMotorX
    ["cmd_VALVE_stop", "i"], # Move StepperMotorY to a specific position
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

    def animate_dispensers(self, speed: int, position_max: int, delay_factor: int, dispenser_index: int):
        self.cmd.send("cmd_SERVO_dispenser_animation", speed, position_max, delay_factor, dispenser_index)
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
