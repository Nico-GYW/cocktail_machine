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
        self.ack_received = {"Stepper X done": False, "Stepper Y done": False}

    def moveTo(self, motor: str, position: int):
        # Envoie la commande pour déplacer le moteur spécifié à une position spécifique
        self.cmd.send(f"cmd_moveTo{motor}", position)
        # Recevoir le message d'accusé de réception de l'Arduino
        msg = self.cmd.receive()
        print(msg)

    def home(self, motor: str):
        # Envoie la commande pour initier la séquence de retour à l'origine pour le moteur spécifié
        self.cmd.send(f"cmd_home{motor}")
        # Recevoir le message d'accusé de réception de l'Arduino
        msg = self.cmd.receive()
        print(msg)

    def stop(self, motor: str):
        # Envoie la commande pour arrêter immédiatement le moteur spécifié
        self.cmd.send(f"cmd_stop{motor}")
        # Recevoir le message d'accusé de réception de l'Arduino
        msg = self.cmd.receive()
        print(msg)

    def getPosition(self, motor: str):
        # Envoie la commande pour obtenir la position actuelle du moteur spécifié
        self.cmd.send(f"cmd_getPosition{motor}")
        # Recevoir la valeur de position de l'Arduino
        msg = self.cmd.receive()
        position = msg[1][0]
        return position

    def getState(self, motor: str):
        # Envoie la commande pour obtenir l'état actuel du moteur spécifié
        self.cmd.send(f"cmd_getState{motor}")
        # Recevoir la valeur d'état de l'Arduino
        msg = self.cmd.receive()
        state = msg[1][0]
        return state
    
    def isAcked(self, ack_type=None, reset=False):
        if reset:
            self.ack_received = {"Stepper X done": False, "Stepper Y done": False}  # Réinitialisation des ack

        msg = self.arduino.receive()  # Tente de recevoir un message une fois
        if msg:
            command, values, timestamp = msg
            if command in ["Stepper X done", "Stepper Y done"]:
                self.ack_received[command] = True  # Marquer l'ack comme reçu

                # Vérifier si on a reçu les ack nécessaires
                if ack_type is None:  # Si on attend les deux ack
                    return all(self.ack_received.values())  # Retourner True si les deux ack ont été reçus
                else:  # Si on attend un ack spécifique
                    return self.ack_received[ack_type]  # Retourner True si l'ack spécifique a été reçu
        return False  # Retourner False si aucun message pertinent n'a été reçu
    
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
