#include "Adafruit_NeoPixel.h"

// Définition des structures pour chaque état
struct StateSettings {
  uint32_t color;
  uint8_t brightness;
};

struct OnState : StateSettings { };
struct OffState : StateSettings { };
struct PulseState : StateSettings {
  uint8_t pulseSpeed;
};
struct RollState : StateSettings {
  uint8_t rollSpeed;
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
    LedStripState currentState;
    OnState onState;
    OffState offState;
    PulseState pulseState;
    RollState rollState;

    void handleOnState();
    void handleOffState();
    void handlePulseState();
    void handleRollState();
    void handleIdleState();

public:
    LedStrip(uint16_t num_leds, uint8_t led_pin);

    void setPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b);
    void setPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b, uint8_t w);
    void setPixelColor(uint16_t n, uint32_t c);
    void setBrightness(uint8_t b);
    void fill(uint32_t c);
    void fill(uint32_t c, uint16_t first, uint16_t count);
    void begin();
    void show();
    void loop();

    static uint32_t Color(uint8_t r, uint8_t g, uint8_t b);
    static uint32_t Color(uint8_t r, uint8_t g, uint8_t b, uint8_t w);
    uint16_t numPixels() const;
    void pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse);

};