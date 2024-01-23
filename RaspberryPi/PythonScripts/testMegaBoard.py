# Import the file that contains the StepperMotorController class
import commandMega as commandMegaMega
import time
# Create an instance of the StepperMotorController class
stepper_motor = commandMega.StepperMotorController()
led_strip = commandMega.LedStripController()

# screen /dev/ttyACM0 9600
 
# Test the moveToX commandMega with different positions
stepper_motor.moveToX(1000) # Move to position 1000
time.sleep(5) # Wait for 5 seconds
stepper_motor.moveToX(2000) # Move to position 2000
time.sleep(5) # Wait for 5 seconds
stepper_motor.moveToX(3000) # Move to position 3000
time.sleep(5) # Wait for 5 seconds

# Test the homeX commandMega
stepper_motor.homeX() # Initiate homing sequence
time.sleep(10) # Wait for 10 seconds

# Test the stopX commandMega
stepper_motor.moveToX(1500) # Move to position 1500
time.sleep(2) # Wait for 2 seconds
stepper_motor.stopX() # Stop the movement
time.sleep(2) # Wait for 2 seconds

# Test the getPositionX commandMega
position = stepper_motor.getPositionX() # Get the current position
print(f"The current position of StepperMotorX is {position}") # Print the position

# Test the getStateX commandMega
state = stepper_motor.getStateX() # Get the current state
print(f"The current state of StepperMotorX is {state}") # Print the state

# Test the moveToY commandMega with different positions
stepper_motor.moveToY(500) # Move to position 500
time.sleep(5) # Wait for 5 seconds
stepper_motor.moveToY(1000) # Move to position 1000
time.sleep(5) # Wait for 5 seconds
stepper_motor.moveToY(1500) # Move to position 1500
time.sleep(5) # Wait for 5 seconds

# Test the homeY commandMega
stepper_motor.homeY() # Initiate homing sequence
time.sleep(10) # Wait for 10 seconds

# Test the stopY commandMega
stepper_motor.moveToY(750) # Move to position 750
time.sleep(2) # Wait for 2 seconds
stepper_motor.stopY() # Stop the movement
time.sleep(2) # Wait for 2 seconds

# Test the getPositionY commandMega
position = stepper_motor.getPositionY() # Get the current position
print(f"The current position of StepperMotorY is {position}") # Print the position

# Test the getStateY commandMega
state = stepper_motor.getStateY() # Get the current state
print(f"The current state of StepperMotorY is {state}") # Print the state

# Tests pour le LedStripController
led_strip.set_mode('T')  # Allumer le bandeau LED
time.sleep(5)  # Attendre 5 secondes
led_strip.set_mode('F')  # Éteindre le bandeau LED
time.sleep(5)  # Attendre 5 secondes
led_strip.pulse_block(5)  # Faire pulser le bandeau LED 5 fois
time.sleep(5)  # Attendre 5 secondes
led_strip.set_settings('P', 255, 0, 0, 128, 10)  # Configurer le mode pulsation avec une couleur rouge
time.sleep(5)  # Attendre 5 secondes
  # Activer le mode pulsation
time.sleep(10)  # Attendre 10 secondes
led_strip.set_mode('F')  # Éteindre le bandeau LED