#include <Arduino.h>
#include "LedStrip.h"
#include <Adafruit_NeoPixel.h>

// Constructeur pour initialiser le bandeau de LED et définir les états par défaut.
// @param num_leds Le nombre total de LEDs dans le bandeau.
// @param led_pin Le numéro de pin sur lequel le bandeau de LED est connecté.

uint32_t whiteColor = Adafruit_NeoPixel::Color(254, 254, 254);

uint32_t colorPattern[24]; // Nouveau tableau pour les couleurs ajustées


uint32_t setBrightness(uint32_t color, uint8_t brightness) {
    uint8_t r = (uint8_t)(brightness * ((color >> 16) & 0xFF) / 255);
    uint8_t g = (uint8_t)(brightness * ((color >> 8) & 0xFF) / 255);
    uint8_t b = (uint8_t)(brightness * (color & 0xFF) / 255);

    return Adafruit_NeoPixel::Color(r, g, b);
}

LedStrip::LedStrip(uint16_t num_leds, uint8_t led_pin) 
    : strip(num_leds, led_pin, NEO_GRB + NEO_KHZ800),
      currentState(STATE_IDLE),
      onState({whiteColor, 255, 0, true}), 
      offState({whiteColor, 0, 0, true}), 
      pulseState({whiteColor, 255, 10, true}), 
      rollState({whiteColor, 255, 10, true}) {
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
        default:
            break;
    }
}

void LedStrip::handleRollState() {

    static int counter = 0; // Variable static pour suivre le nombre de cycles

    if(counter > 0) {
        counter--;
        return;
    }

    counter = rollState.speed;

    // Faire tourner les valeurs de luminosité
    uint32_t lastColor = colorPattern[23];
    for (int i = 23; i > 0; i--) {
        colorPattern[i] = colorPattern[i - 1];
    }
    colorPattern[0] = lastColor;

    // Appliquer les valeurs de luminosité
    for (int i = 0; i <= 23 ; i++) {
        strip.setPixelColor(i, colorPattern[i]);
    }
    strip.show();
}

// Gère l'état de pulsation des LEDs.
void LedStrip::handlePulseState() {

    static int counter = 0; // Variable static pour suivre le nombre de cycles

    if(counter > 0) {
        counter--;
        return; // Sauter la mise à jour si le compteur n'est pas à zéro
    }

    // Réinitialiser le compteur
    counter = pulseState.speed;

    // Inverser la direction si la luminosité atteint ses limites
    if (pulseState.brightness >= 254 || pulseState.brightness <= 1) {
        pulseState.direction = !pulseState.direction;
    }

    // Modifier la luminosité en fonction de la direction

    pulseState.brightness += (pulseState.direction ? 5 : -5);

    // Appliquer la luminosité et la couleur
    uint32_t adjustedColor = setBrightness(pulseState.color, pulseState.brightness);
    strip.fill(adjustedColor);

    strip.show();
}

// Met à jour les paramètres d'état des LEDs (couleur, luminosité, vitesse).
// @param state Référence à la structure StateSettings à mettre à jour.
// @param color La nouvelle couleur (RGB combinée en uint32_t) pour les LEDs.
// @param brightness La nouvelle luminosité pour les LEDs (0-255).
// @param speed La nouvelle vitesse pour les animations des LEDs.
void LedStrip::updateStateSettings(StateSettings& state, uint32_t color, uint8_t brightness, uint16_t speed){
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
    strip.setBrightness(0); 
    strip.show();
    currentState = STATE_IDLE;
}

// Définit le bandeau de LED en mode pulsation.
void LedStrip::pulse(){
    strip.fill(pulseState.color);
    strip.setBrightness(254); 
    strip.show();
    currentState = STATE_PULSE; 
}

// Définit le bandeau de LED en mode défilement.
void LedStrip::roll(){

    static uint8_t brightnessPattern[24] = {
    0, 10, 20, 40, 60, 80, 100, 140, 180, 200, 220, 250,
    250, 220, 200, 180, 140, 100, 80, 60, 40, 20, 10, 0
    };

    strip.fill(rollState.color);
    
    for (int i = 0; i < 24; ++i) {
        colorPattern[i] = setBrightness(rollState.color, brightnessPattern[i]);
    }

    strip.setBrightness(254); 
    strip.show();
    currentState = STATE_ROLL; 
}

// Exécute un effet de pulsation bloquant avec une couleur, un nombre de pulsations et une vitesse spécifiés.
// @param color La couleur (RGB combinée en uint32_t) pour l'effet de pulsation.
// @param num_pulses Le nombre de pulsations à effectuer.
// @param speedOfPulse La vitesse de la pulsation (plus le nombre est élevé, plus la pulsation est rapide).
void LedStrip::pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse){
    strip.fill(color);

    for(int k=1; k<=num_pulses; k++){
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
