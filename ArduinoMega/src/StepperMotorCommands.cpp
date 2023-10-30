#include "StepperMotor.h"
#include "StepperMotorCommands.h"
#include "CmdMessenger.h"

// X motor
#define StepPinX A0
#define DirPinX A1
#define EnablePinX 38
#define EndAxisX 3
#define maxPositionX 3800

// Y motor
#define StepPinY A6
#define DirPinY A7
#define EnablePinY A2
#define EndAxisY 14
#define maxPositionY 2500

extern CmdMessenger cmdMessenger; // Déclaration externe
StepperMotor StepperMotorX(StepPinX, DirPinX, EndAxisX, EnablePinX);  // stepPin, dirPin, endStop, enablePin
StepperMotor StepperMotorY(StepPinY, DirPinY, EndAxisY, EnablePinY);  // stepPin, dirPin, endStop, enablePin

void beginStepper(){
  StepperMotorX.begin();
  StepperMotorY.begin();
  StepperMotorX.runUntilEndStop();
  onHomeY();
  onHomeX();
}

void updateStepperMotor(){
  StepperMotorX.loop();
  StepperMotorY.loop();
}

// Moves StepperMotorX to a specific position
void onMoveToX() {
  int position = cmdMessenger.readBinArg<int>();
  StepperMotorX.moveTo(position);
  cmdMessenger.sendCmd(cmd_ack, "X Moved to position, State : ");
}

// Initiates homing sequence for StepperMotorX
void onHomeX() {
  StepperMotorX.home();
  int currentState = StepperMotorX.getCurrentState();
  cmdMessenger.sendCmd(cmd_ack, "X Homing initiated, State : " + String(currentState));
}

// Stops StepperMotorX immediately
void onStopX() {
  StepperMotorX.stop();
  cmdMessenger.sendCmd(cmd_ack, "X Stopped");
}

// Gets the current position of StepperMotorX
void onGetPositionX() {
  long position = StepperMotorX.getPosition();
  cmdMessenger.sendCmd(cmd_ack, position);
}

// Gets the current state of StepperMotorX
void onGetStateX() {
  int state = StepperMotorX.getCurrentState();
  cmdMessenger.sendCmd(cmd_ack, state);
}

// Moves StepperMotorY to a specific position
void onMoveToY() {
  int position = cmdMessenger.readBinArg<int>();
  StepperMotorY.moveTo(position);
  cmdMessenger.sendCmd(cmd_ack, "Y Moved to position");
}

// Initiates homing sequence for StepperMotorY
void onHomeY() {
  StepperMotorY.home();
  cmdMessenger.sendCmd(cmd_ack, "Y Homing initiated");
}

// Stops StepperMotorY immediately
void onStopY() {
  StepperMotorY.stop();
  cmdMessenger.sendCmd(cmd_ack, "Y Stopped");
}

// Gets the current position of StepperMotorY
void onGetPositionY() {
  long position = StepperMotorY.getPosition();
  cmdMessenger.sendCmd(cmd_ack, position);
}

// Gets the current state of StepperMotorY
void onGetStateY() {
  int state = StepperMotorY.getCurrentState();
  cmdMessenger.sendCmd(cmd_ack, state);
}

// Attaches command handlers for StepperMotorX
void attachStepperMotorXCommands() {
  cmdMessenger.attach(cmd_moveToX, onMoveToX);
  cmdMessenger.attach(cmd_homeX, onHomeX);
  cmdMessenger.attach(cmd_stopX, onStopX);
  cmdMessenger.attach(cmd_getPositionX, onGetPositionX);
  cmdMessenger.attach(cmd_getStateX, onGetStateX);
  StepperMotorX.begin();
}

// Attaches command handlers for StepperMotorY
void attachStepperMotorYCommands() {
  cmdMessenger.attach(cmd_moveToY, onMoveToY);
  cmdMessenger.attach(cmd_homeY, onHomeY);
  cmdMessenger.attach(cmd_stopY, onStopY);
  cmdMessenger.attach(cmd_getPositionY, onGetPositionY);
  cmdMessenger.attach(cmd_getStateY, onGetStateY);
  StepperMotorY.begin();
}