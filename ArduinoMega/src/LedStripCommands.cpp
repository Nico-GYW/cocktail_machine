#include "CmdMessenger.h"
#include "LedStrip.h"
#include "LedStripCommands.h"
#include "CommandsEnum.h"

// LedStrip
#define LedPin A3

extern CmdMessenger cmdMessenger; // Déclaration externe

LedStrip leds(24, LedPin);
uint32_t white = leds.Color(255, 255, 255);


void beginLedStrip(){
  leds.begin();
}

void testLed(){
  leds.pulse(white,2,10);
}

// Moves StepperMotorY to a specific position
void onPulse(){
  int pulses = cmdMessenger.readBinArg<int>();
  leds.pulse(white, pulses, 10);
  cmdMessenger.sendCmd(cmd_ack, "Led pulses");
}

// Attaches command handlers for StepperMotorX
void attachLedStripCommands(){
  cmdMessenger.attach(cmd_pulse, onPulse);
}
