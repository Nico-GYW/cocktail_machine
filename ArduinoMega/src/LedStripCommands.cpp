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

// Gère le mode du LedStrip en fonction de l'entrée Serial
void onLedMode(){
  char mode = cmdMessenger.readCharArg();
  switch (mode) {
    case 'T':
        leds.on();
        break;
    case 'F':
        leds.off();
        break;
    case 'P':
        leds.pulse();
        break;
    case 'R':
        leds.roll();
        break;
    default:
        // Gestion d'erreur ou log
        break;
  }
}

// Exécute un effet de pulsation bloquant sur le LedStrip
void onPulseBlock() {
  int pulses = cmdMessenger.readBinArg<int>();
  leds.pulse(white, pulses, 10); // `white` doit être défini quelque part
  cmdMessenger.sendCmd(cmd_ack, "Led pulses");
}

// Met à jour les paramètres du LedStrip en fonction de l'entrée Serial et active le mode correspondant
void onLedSettings() {
    char stateType = cmdMessenger.readCharArg();
    uint8_t r = cmdMessenger.readByteArg();
    uint8_t g = cmdMessenger.readByteArg();
    uint8_t b = cmdMessenger.readByteArg();
    uint8_t brightness = cmdMessenger.readByteArg();
    uint8_t speed = cmdMessenger.readByteArg();

    uint32_t color = Adafruit_NeoPixel::Color(r, g, b);

    switch (stateType) {
        case 'T':
            updateStateSettings(leds.onState, color, brightness, speed);
            leds.on();
            break;
        case 'F':
            updateStateSettings(leds.offState, color, brightness, speed);
            leds.off();
            break;
        case 'P':
            updateStateSettings(leds.pulseState, color, brightness, speed);
            leds.pulse();
            break;
        case 'R':
            updateStateSettings(leds.rollState, color, brightness, speed);
            leds.roll();
            break;
        default:
            // Gestion d'erreur ou log
            break;
    }

    String ackMessage = "New Led Settings: Type=" + String(stateType) + 
                        ", Color(RGB)=" + String(r) + "," + String(g) + "," + String(b) + 
                        ", Brightness=" + String(brightness) + 
                        ", Speed=" + String(speed);

    cmdMessenger.sendCmd(cmd_ack, ackMessage.c_str());
}

// Attache les commandes pour la gestion du LedStrip
void attachLedStripCommands(){
  cmdMessenger.attach(cmd_LED_mode, onLedMode);
  cmdMessenger.attach(cmd_LED_pulseBlock, onPulseBlock);
  cmdMessenger.attach(cmd_LED_settings, onLedSettings);
}
