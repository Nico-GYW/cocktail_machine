#include <Arduino.h>
#include <CmdMessenger.h>


// PORT ttyACM1 (Arduino Mega)

CmdMessenger cmdMessenger = CmdMessenger(Serial, ',', ';', '/');


// LedStrip
#define LedPin A3

LedStrip leds(24, LedPin);
uint32_t white = leds.Color(255, 255, 255);


void setup() {
  Serial.begin(115200);
  leds.begin();
  
}

void loop() {
  updateStepperMotor();
  // cmdMessenger.feedinSerialData();
  // leds.pulse(white,2,10); 
}

// -----------------------------------------------------------------------------------------------------------
