#ifndef STEPPER_MOTOR_COMMANDS_H
#define STEPPER_MOTOR_COMMANDS_H

#include "StepperMotor.h"
#include "CmdMessenger.h"

// Enum for Stepper Motor Command
enum StepperMotorCommands {
  cmd_moveToX,
  cmd_homeX,
  cmd_stopX,
  cmd_getPositionX,
  cmd_getStateX,
  cmd_moveToY,
  cmd_homeY,
  cmd_stopY,
  cmd_getPositionY,
  cmd_getStateY,
  cmd_ack // acknowledge command
};

void beginStepper();
void updateStepperMotor();

// Function declarations
void onMoveToX();
void onHomeX();
void onStopX();
void onGetPositionX();
void onGetStateX();
void onMoveToY();
void onHomeY();
void onStopY();
void onGetPositionY();
void onGetStateY();
void attachStepperMotorXCommands();
void attachStepperMotorYCommands();


#endif // STEPPER_MOTOR_COMMANDS_H
