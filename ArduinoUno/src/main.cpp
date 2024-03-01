#include <Arduino.h>
#include <CmdMessenger.h>

#include "ServoCommand.h"
#include "DCValveCommand.h"
#include "ElectricCylinderCommand.h"

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');


void setup() {
  Serial.begin(9600);
  beginServo();
  beginValve();
  beginElectricCylinder();

  attachServoCommands();
  attachValveCommands();
  attachElectricCylinderCommands();
}

void loop() {
  updateServo();
  updateValve();
  updateElectricCylinder();
  cmdMessenger.feedinSerialData();
}


// -----------------------------------------------------------------------------------------------------------
