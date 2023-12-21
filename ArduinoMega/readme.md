# Cocktail Machine Controller

## Overview
This repository contains the source code for controlling a cocktail machine using an ArduinoAtmega. The codebase is structured to manage both stepper motors and LED controls, offering a seamless and automated operation of the cocktail machine.

## Contents
- `CommandsEnum.h`: Enumerations for command identifiers used across the system.
- `LedStrip.cpp` & `LedStrip.h`: Implementation and interface for LED strip control.
- `LedStripCommands.cpp` & `LedStripCommands.h`: Command handling for LED strip operations.
- `main.cpp`: The main entry point for the program.
- `StepperMotor.cpp` & `StepperMotor.h`: Implementation and interface for controlling stepper motors.
- `StepperMotorCommands.cpp`: Command handling for stepper motor operations.

## Getting Started
### Prerequisites
- Arduino IDE or compatible IDE for Arduino development.
- ArduinoAtmega hardware setup with stepper motors and LED strip connected.
- Basic understanding of Arduino programming and hardware interaction.

### Installation
1. Clone the repository or download the source code.
2. Open the `.cpp` and `.h` files in the Arduino IDE or your preferred development environment.
3. Upload the code to your ArduinoAtmega board.

### Hardware Setup
Ensure your hardware is set up according to the specifications in `main.cpp`. Connect the stepper motors and LED strips to the designated pins on the Arduino board.

## Usage
The codebase is divided into distinct sections for LED control and stepper motor control, allowing for modular interaction and easy scalability.

### LED Control
- Use `LedStrip.cpp` and `LedStrip.h` for basic LED operations.
- `LedStripCommands.cpp` handles specific commands and integrates with the main control loop.

### Stepper Motor Control
- `StepperMotor.cpp` and `StepperMotor.h` provide a layer of abstraction for motor operations.
- `StepperMotorCommands.cpp` deals with command parsing and execution specific to stepper motors.

### Command Handling
Commands for both LEDs and stepper motors are defined in `CommandsEnum.h`. These commands are used across the system for consistent operation and control flow.

## Contributing
Contributions to the project are welcome. Please ensure you follow the coding standards and add comments to any new functions or major changes you make.

## License
Specify your licensing information here.
