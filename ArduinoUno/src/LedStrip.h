#include "Adafruit_NeoPixel.h"

class LedStrip {
private:
    Adafruit_NeoPixel strip;
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

    static uint32_t Color(uint8_t r, uint8_t g, uint8_t b);

    static uint32_t Color(uint8_t r, uint8_t g, uint8_t b, uint8_t w);

    uint16_t numPixels() const;

    void pulse(uint32_t color, uint8_t num_pulses, uint8_t speedOfPulse);

};