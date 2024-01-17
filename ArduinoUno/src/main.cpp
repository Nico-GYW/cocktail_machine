#include <Arduino.h>
#include <CmdMessenger.h>

#include "ServoCommand.h"
#include "DCValveCommand.h"

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');

void setup() {
  Serial.begin(115200);
  beginServo();
  beginValve();

  attachServoCommands();
  attachValveCommands();
}

void loop() {
  updateServo();
  updateValve();
  cmdMessenger.feedinSerialData();
}

// -----------------------------------------------------------------------------------------------------------
