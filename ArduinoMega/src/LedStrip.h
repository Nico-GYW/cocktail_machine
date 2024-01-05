#include "Adafruit_NeoPixel.h"

// Définition des structures pour chaque état
struct StateSettings {
  uint32_t color;
  uint8_t brightness;
  uint16_t speed;
  bool direction;
};

// Énumérateur pour les états du LED strip
enum LedStripState {
    STATE_PULSE,
    STATE_ROLL,
    STATE_IDLE
};

class LedStrip {
private:
    Adafruit_NeoPixel strip;
    LedStripState currentState;

    void handlePulseState();
    void handleRollState();

public:
    LedStrip(uint16_t num_leds, uint8_t led_pin);
    StateSettings onState;
    StateSettings offState;
    StateSettings pulseState;
    StateSettings rollState;

    void updateStateSettings(StateSettings& state, uint32_t color, uint8_t brightness, uint16_t speed);
    
    void begin();
    void loop();
    void on();
    void off();
    void pulse();
    void roll();
    void pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse);
};