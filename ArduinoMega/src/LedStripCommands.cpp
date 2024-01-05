#include "CmdMessenger.h"
#include "LedStrip.h"
#include "LedStripCommands.h"
#include "CommandsEnum.h"

// Configuration du LedStrip
#define LedPin A3

extern CmdMessenger cmdMessenger; // Déclaration externe de CmdMessenger

LedStrip leds(24, LedPin); // Initialisation du LedStrip

// Initialisation du LedStrip
void beginLedStrip(){
  leds.begin();
}

void updateLedStrip(){
  leds.loop();
}

// Gère le mode du LedStrip en fonction de l'entrée Serial
void onLedMode(){
  char mode = cmdMessenger.readCharArg();
  switch (mode) {
    case 'T':
        leds.on();
        cmdMessenger.sendCmd(cmd_ack, "Led On");
        break;
    case 'F':
        leds.off();
        cmdMessenger.sendCmd(cmd_ack, "Led Off");
        break;
    case 'P':
        leds.pulse();
        cmdMessenger.sendCmd(cmd_ack, "Led pulse");
        break;
    case 'R':
        leds.roll();
        cmdMessenger.sendCmd(cmd_ack, "Led roll");
        break;
    default:
        // Gestion d'erreur ou log
        break;
  }
}

// Exécute un effet de pulsation bloquant sur le LedStrip
void onPulseBlock() {
  uint32_t whiteColor = Adafruit_NeoPixel::Color(255, 255, 255);
  int pulses = cmdMessenger.readBinArg<int>();
  leds.pulse(whiteColor, pulses, 10);
  cmdMessenger.sendCmd(cmd_ack, "Led pulses");
}

// Met à jour les paramètres du LedStrip en fonction de l'entrée Serial et active le mode correspondant
void onLedSettings() {
    char stateType = cmdMessenger.readBinArg<char>();
    uint8_t r = cmdMessenger.readBinArg<int>();
    uint8_t g = cmdMessenger.readBinArg<int>();
    uint8_t b = cmdMessenger.readBinArg<int>();
    uint8_t brightness = cmdMessenger.readBinArg<int>();
    uint16_t speed = cmdMessenger.readBinArg<int>();

    uint32_t color = Adafruit_NeoPixel::Color(r, g, b);

    switch (stateType) {
        case 'T':
            leds.updateStateSettings(leds.onState, color, brightness, speed);
            leds.on();
            break;
        case 'F':
            leds.updateStateSettings(leds.offState, color, brightness, speed);
            leds.off();
            break;
        case 'P':
            leds.updateStateSettings(leds.pulseState, color, brightness, speed*5);
            leds.pulse();
            break;
        case 'R':
            leds.updateStateSettings(leds.rollState, color, brightness, speed*10);
            leds.roll();
            break;
        default:
            break;
    }

    cmdMessenger.sendCmd(cmd_ack, "New Led Settings");
}

// Attache les commandes pour la gestion du LedStrip
void attachLedStripCommands(){
  cmdMessenger.attach(cmd_LED_mode, onLedMode);
  cmdMessenger.attach(cmd_LED_pulseBlock, onPulseBlock);
  cmdMessenger.attach(cmd_LED_settings, onLedSettings);
}
