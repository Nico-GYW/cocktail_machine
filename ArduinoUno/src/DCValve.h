#include <Arduino.h>

#define NUMBER_OF_VALVES 4

enum ValveState {
    IDLE,
    WAIT,
};

struct DCValve {
    ValveState state;
    int pin;
    unsigned long delay;
    unsigned long timer;
};

class DCValveHandler{
    private:
        DCValve valves[NUMBER_OF_VALVES];
        void handleWaitState(DCValve &valve);

    public:
        DCValveHandler(int pins[NUMBER_OF_VALVES]);
        void begin();
        void loop();
        void open(int valveIndex, unsigned long delay);
        void close(int valveIndex);
        void close(DCValve &valve);
        void stop();
};