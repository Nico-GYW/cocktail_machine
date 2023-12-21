#include "Adafruit_NeoPixel.h"

// Définition des structures pour chaque état
struct StateSettings {
  uint32_t color;
  uint8_t brightness;
  uint8_t speed;
};

// Énumérateur pour les états du LED strip
enum LedStripState {
    STATE_ON,
    STATE_OFF,
    STATE_PULSE,
    STATE_ROLL,
    STATE_IDLE
};

class LedStrip {
private:
    Adafruit_NeoPixel strip;
    StateSettings onState;
    StateSettings offState;
    StateSettings pulseState;
    StateSettings rollState;
    LedStripState currentState;

    static constexpr uint32_t whiteColor = Adafruit_NeoPixel::Color(255, 255, 255);
    void handlePulseState();
    void handleRollState();

public:
    LedStrip(uint16_t num_leds, uint8_t led_pin);
    void updateStateSettings(StateSettings& state, uint32_t color, uint8_t brightness, uint8_t speed)
    void begin();
    void loop();
    void on();
    void off();
    void pulse();
    void roll();
    void pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse);
};