#include <Arduino.h>
#include <CmdMessenger.h>

#include "StepperMotorCommands.h"
#include "LedStripCommands.h"


// PORT ttyACM1 (Arduino Mega)
CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');

void setup() {
  Serial.begin(9600);
  
  attachStepperMotorCommands();
  attachLedStripCommands();

  beginStepper();
  beginLedStrip();
}

void loop() {
  updateStepperMotor();
  updateLedStrip();
  cmdMessenger.feedinSerialData();
}

// -----------------------------------------------------------------------------------------------------------
