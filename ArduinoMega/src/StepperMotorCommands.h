#ifndef STEPPER_MOTOR_COMMANDS_H
#define STEPPER_MOTOR_COMMANDS_H

#include "StepperMotor.h"
#include "CmdMessenger.h"

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
void attachStepperMotorCommands();


#endif // STEPPER_MOTOR_COMMANDS_H
