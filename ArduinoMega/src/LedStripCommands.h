#ifndef LED_STRIP_H
#define LED_STRIP_H

#include "CmdMessenger.h"

void beginLedStrip();
void updateLedStrip();
void onLedMode();
void onPulseBlock();
void onLedSettings();
void attachLedStripCommands();

#endif