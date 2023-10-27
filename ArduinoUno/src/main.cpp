#include <Arduino.h>
#include <CmdMessenger.h>
#include "StepperMotor.h"
#include "StepperMotorCommands.h"

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');

void setup() {
  Serial.begin(115200);
  beginStepper();
  attachStepperMotorXCommands();
  attachStepperMotorYCommands();
}

void loop() {
  updateStepperMotor();
  cmdMessenger.feedinSerialData();
}

// -----------------------------------------------------------------------------------------------------------
