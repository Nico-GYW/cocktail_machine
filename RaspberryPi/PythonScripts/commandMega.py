import PyCmdMessenger
import serial.tools.list_ports
import time

# Initialize an ArduinoBoard instance.  
# arduino_uno = PyCmdMessenger.ArduinoBoard("/dev/ttyACM0", baud_rate=115200)

def find_arduino(pid):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.pid == pid:
            return port.device
    return None

# PID
arduino_uno_pid = 0x0043
arduino_mega_pid = 0x0042

port_uno = find_arduino(arduino_uno_pid)
port_mega = find_arduino(arduino_mega_pid)


arduino_mega = PyCmdMessenger.ArduinoBoard(port_mega, baud_rate=9600)

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.

#commands_uno = [
#]

commands_mega = [
    ["cmd_moveToX", "i"], # Move StepperMotorX to a specific positiimon
    ["cmd_homeX", ""], # Initiate homing sequence for StepperMotorX
    ["cmd_stopX", ""], # Stop StepperMotorX immediately
    ["cmd_getPositionX", "l"], # Get the current position of StepperMotorX
    ["cmd_getStateX", "i"], # Get the current state of StepperMotorX
    ["cmd_moveToY", "i"], # Move StepperMotorY to a specific position
    ["cmd_homeY", ""], # Initiate homing sequence for StepperMotorY
    ["cmd_stopY", ""], # Stop StepperMotorY immediately
    ["cmd_getPositionY", "l"], # Get the current position of StepperMotorY
    ["cmd_getStateY", "i"], # Get the current state of StepperMotorY
    ["cmd_LED_mode", "c"], # Commande pour changer le mode du LedStrip
    ["cmd_LED_pulseBlock", "i"], # Commande pour effectuer une pulsation bloquante
    ["cmd_LED_settings", "ciiiii"], # Commande pour mettre à jour les paramètres du LedStrip
    ["cmd_ack","s"] # Acknowledge a command,
]

# Initialize the messenger
#cmd_arduino_uno = PyCmdMessenger.CmdMessenger(arduino_uno, commands_uno)
cmd_arduino_mega = PyCmdMessenger.CmdMessenger(arduino_mega, commands_mega)

class Controller:
    def __init__(self, cmd_arduino):
        self.cmd = cmd_arduino
        
class StepperMotorController(Controller):
    Y1 = 500
    Y2 = 2000
    B1 = (None, None)
    B2 = (3500, Y1)
    B3 = (3000, Y1)
    B4 = (2600, Y2)
    B5 = (2200, Y1)
    B6 = (1725, Y1)
    B7 = (1300, Y2)
    B8 = (950, Y1)
    B9 = (475, Y2)

    GLASS_BOTTLE_POSITIONS = [B1, B2, B3, B4, B5, B6, B7, B8, B9]

    S1 = (2000, 0)
    S4 = (3300, 0)

    SOFT_BOTTLE_POSITIONS = [S1, S1, S4, S4]

    def __init__(self):
        super().__init__(cmd_arduino_mega)

    def moveToX(self, position: int):
        # Send the command to move StepperMotorX to a specific position
        self.cmd.send("cmd_moveToX", position)
        # Receive the acknowledgement message from Arduino
        time.sleep(1)
        msg = self.cmd.receive()
        print(msg)

    def homeX(self):
        # Send the command to initiate homing sequence for StepperMotorX
        self.cmd.send("cmd_homeX")
        # Receive the acknowledgement message from Arduino
        time.sleep(0.1)
        msg = self.cmd.receive()
        print(msg)

    def stopX(self):
        # Send the command to stop StepperMotorX immediately
        self.cmd.send("cmd_stopX")
        # Receive the acknowledgement message from Arduino
        msg = self.cmd.receive()
        print(msg)

    def getPositionX(self):
        # Send the command to get the current position of StepperMotorX
        self.cmd.send("cmd_getPositionX")
        # Receive the position value from Arduino
        msg = self.cmd.receive()
        position = msg[1][0]
        return position

    def getStateX(self):
        # Send the command to get the current state of StepperMotorX
        self.cmd.send("cmd_getStateX")
        # Receive the state value from Arduino
        msg = self.cmd.receive()
        state = msg[1][0]
        return state

    def moveToY(self, position):
        # Send the command to move StepperMotorY to a specific position
        self.cmd.send("cmd_moveToY", position)
        # Receive the acknowledgement message from Arduino
        msg = self.cmd.receive()
        print(msg)

    def homeY(self):
        # Send the command to initiate homing sequence for StepperMotorY
        self.cmd.send("cmd_homeY")
        # Receive the acknowledgement message from Arduino
        msg = self.cmd.receive()
        print(msg)

    def stopY(self):
        # Send the command to stop StepperMotorY immediately
        self.cmd.send("cmd_stopY")
        # Receive the acknowledgement message from Arduino
        msg = self.cmd.receive()
        print(msg)

    def getPositionY(self):
        # Send the command to get the current position of StepperMotorY
        self.cmd.send("cmd_getPositionY")
        # Receive the position value from Arduino
        msg = self.cmd.receive()
        position = msg[1][0]
        return position

    def getStateY(self):
        # Send the command to get the current state of StepperMotorY
        self.cmd.send("cmd_getStateY")
        # Receive the state value from Arduino
        msg = self.cmd.receive()
        state = msg[1][0]
        return state

class LedStripController(Controller):

    def __init__(self):
        super().__init__(cmd_arduino_mega)

    def set_mode(self, mode: str):
        self.cmd.send("cmd_LED_mode", mode)
        msg = self.cmd.receive()
        print(msg)

    def pulse_block(self, pulses: int):
        self.cmd.send("cmd_LED_pulseBlock", pulses)
        msg = self.cmd.receive()
        print(msg)

    def set_settings(self, state_type: str, r: int, g: int, b: int, brightness: int, speed: int):
        self.cmd.send("cmd_LED_settings", state_type, r, g, b, brightness, speed)
        msg = self.cmd.receive()
        print(msg)
