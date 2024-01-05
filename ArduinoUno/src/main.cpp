#include <Arduino.h>
#include <CmdMessenger.h>

// PORT ttyACM1 (Arduino Mega)

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');

void setup() {
  Serial.begin(115200);
  
}

void loop() {
  // cmdMessenger.feedinSerialData();
}

// -----------------------------------------------------------------------------------------------------------
