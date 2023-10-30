#include <Arduino.h>
#include <CmdMessenger.h>
#include "StepperMotor.h"
#include "StepperMotorCommands.h"

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');

void setup() {
  Serial.begin(115200);
  
  attachStepperMotorXCommands();
  attachStepperMotorYCommands();

  beginStepper();
}

void loop() {
  updateStepperMotor();
  cmdMessenger.feedinSerialData();
}

// -----------------------------------------------------------------------------------------------------------
