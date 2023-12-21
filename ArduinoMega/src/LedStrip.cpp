#include <Arduino.h>
#include "LedStrip.h"
#include <Adafruit_NeoPixel.h>

// Constructeur pour initialiser le bandeau de LED et définir les états par défaut.
// @param num_leds Le nombre total de LEDs dans le bandeau.
// @param led_pin Le numéro de pin sur lequel le bandeau de LED est connecté.
LedStrip::LedStrip(uint16_t num_leds, int16_t led_pin) 
    : strip(num_leds, led_pin, NEO_GRB + NEO_KHZ800),
      onState({whiteColor, 255}), 
      offState({whiteColor, 0}), 
      pulseState({whiteColor, 255, 10}), 
      rollState({whiteColor, 255, 10}),
      currentState(STATE_IDLE) {
}

// Initialise le bandeau de LED et allume toutes les LEDs.
void LedStrip::begin() {
    strip.begin();
}

// Boucle principale pour gérer l'état actuel du bandeau de LED.
void LedStrip::loop() {
    switch (currentState) {
        case STATE_IDLE:
            // Ne fait rien en état de repos.
            break;
        case STATE_PULSE:
            handlePulseState();
            break;
        case STATE_ROLL:
            handleRollState();
            break;
    }
}

// Gère l'état de défilement en rotation des LEDs.
void LedStrip::handleRollState() {
    static uint16_t currentLed = 0; // LED actuelle

    strip.setPixelColor(currentLed, rollState.color); // Allumer la LED actuelle
    strip.show();

    currentLed = (currentLed + 1) % strip.numPixels(); // Passer à la LED suivante
    if (currentLed == 0) {
        currentState = STATE_IDLE; // Revenir à l'état de repos à la fin du cycle
    }
}

// Gère l'état de pulsation des LEDs.
void LedStrip::handlePulseState() {
    // Mettre à jour la luminosité
    if (pulseState.brightness + pulseState.speed > 255 || 
        pulseState.brightness + pulseState.speed < 0) {
        pulseState.speed = -pulseState.speed; // Inverser la direction
    }
    pulseState.brightness += pulseState.speed;

    // Appliquer la luminosité et la couleur
    strip.setBrightness(pulseState.brightness);
    strip.fill(pulseState.color); 
    strip.show();
}

// Met à jour les paramètres d'état des LEDs (couleur, luminosité, vitesse).
// @param state Référence à la structure StateSettings à mettre à jour.
// @param color La nouvelle couleur (RGB combinée en uint32_t) pour les LEDs.
// @param brightness La nouvelle luminosité pour les LEDs (0-255).
// @param speed La nouvelle vitesse pour les animations des LEDs.
void LedStrip::updateStateSettings(StateSettings& state, uint32_t color = state.color, uint8_t brightness = state.brightness, uint8_t speed = state.speed){
    state.color = color;
    state.brightness = brightness;
    state.speed = speed;
}

// Active le bandeau de LED avec les paramètres de l'état "on".
void LedStrip::on(){
    strip.fill(onState.color);
    strip.setBrightness(onState.brightness); 
    strip.show();
    currentState = STATE_IDLE; 
}

// Éteint le bandeau de LED en appliquant les paramètres de l'état "off".
void LedStrip::off(){
    strip.fill(offState.color); 
    strip.setBrightness(offState.brightness); 
    strip.show();
    currentState = STATE_IDLE;
}

// Définit le bandeau de LED en mode pulsation.
void LedStrip::pulse(){
    strip.fill(pulseState.color);
    currentState = STATE_PULSE; 
}

// Définit le bandeau de LED en mode défilement.
void LedStrip::roll(){
    strip.fill(rollState.color); 
    currentState = STATE_ROLL; 
}

// Exécute un effet de pulsation bloquant avec une couleur, un nombre de pulsations et une vitesse spécifiés.
// @param color La couleur (RGB combinée en uint32_t) pour l'effet de pulsation.
// @param num_pulses Le nombre de pulsations à effectuer.
// @param speedOfPulse La vitesse de la pulsation (plus le nombre est élevé, plus la pulsation est rapide).
void LedStrip::pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse){
    strip.fill(color);

    for(int k=1; k<num_pulses; k++){
      for(int i=1; i<255; i+=speedOfPulse){
        strip.setBrightness(i);
        strip.show();
      }
      for( int i=255; i>0; i--){
        strip.setBrightness(i);
        strip.show();
      }
    }
}
