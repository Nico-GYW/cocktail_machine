#include <Arduino.h>

#include "LedStrip.h"
#include <Adafruit_NeoPixel.h>


LedStrip::LedStrip(uint16_t num_leds, uint8_t led_pin) {
  strip = Adafruit_NeoPixel(num_leds, led_pin, NEO_GRB + NEO_KHZ800);
  strip.begin();
}

void LedStrip::setPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b) {
    strip.setPixelColor(n, r, g, b);
}

void LedStrip::setPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b, uint8_t w) {
    strip.setPixelColor(n, r, g, b, w);
}

void LedStrip::setPixelColor(uint16_t n, uint32_t c) {
    strip.setPixelColor(n, c);
}

void LedStrip::setBrightness(uint8_t b) {
    strip.setBrightness(b);
}

void LedStrip::fill(uint32_t c) {
    strip.fill(c);
    strip.show();
}

void LedStrip::begin() {
    strip.begin();
}

void LedStrip::fill(uint32_t c, uint16_t first, uint16_t count) {
    strip.fill(c, first, count);
    strip.show();
}

void LedStrip::show() {
    strip.show();
}

uint32_t LedStrip::Color(uint8_t r, uint8_t g, uint8_t b) {
    return Adafruit_NeoPixel::Color(r, g, b);
}

uint32_t LedStrip::Color(uint8_t r, uint8_t g, uint8_t b, uint8_t w) {
    return Adafruit_NeoPixel::Color(r, g, b, w);
}

uint16_t LedStrip::numPixels() const {
    return strip.numPixels();
}

void LedStrip::loop() {
    switch (currentState) {
        case STATE_ON:
            handleOnState();
            break;
        case STATE_OFF:
            handleOffState();
            break;
        case STATE_PULSE:
            handlePulseState();
            break;
        case STATE_ROLL:
            handleRollState();
            break;
    }
}


void LedStrip::handleOnState() {
    fill(onState.color); // Remplir avec la couleur définie
    setBrightness(onState.brightness); // Régler la luminosité
    show(); // Mettre à jour le bandeau LED
    currentState = STATE_IDLE; // Passer à l'état de repos
}

void LedStrip::handleOffState() {
    fill(0); // Éteindre toutes les LEDs
    show();
    currentState = STATE_IDLE; // Passer à l'état de repos
}

void LedStrip::handleRollState() {
    static uint16_t currentLed = 0; // LED actuelle

    setPixelColor(currentLed, rollState.color); // Allumer la LED actuelle
    show();

    currentLed = (currentLed + 1) % numPixels(); // Passer à la LED suivante
    if (currentLed == 0) {
        currentState = STATE_IDLE; // Revenir à l'état de repos à la fin du cycle
    }
}

void LedStrip::handlePulseState() {
    static int brightness = 0; // Luminosité actuelle
    static int step = pulseState.pulseSpeed; // Pas d'augmentation/de diminution

    brightness += step;
    if (brightness >= 255 || brightness <= 10) {
        step = -step; // Inverser la direction de la luminosité
    }

    setBrightness(brightness);
    fill(pulseState.color); // Appliquer la couleur
    show();

    if (brightness == 10) {
        currentState = STATE_IDLE; // Revenir à l'état de repos
    }
}

void LedStrip::handleIdleState() {
    // Ne fait rien
}


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
