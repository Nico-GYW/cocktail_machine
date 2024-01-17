#include <SPI.h>
#include <Adafruit_PWMServoDriver.h>

#define MAX_ACTIONS 5  // Nombre maximum d'actions par servo
#define NUMBER_OF_SERVO 16  // Nombre total de servo

enum ServoState {
    IDLE,
    MOVE,
    WAIT
};

struct ServoAction {
    ServoState stateType;
    uint8_t targetPosition;  // in degrees
    uint8_t speed; // taux d'incrémentation en degré
    uint16_t delay; // Durée maximale de 20000 ms

    // Constructeur qui initialise direction à true et timer à 0 par défaut.
    ServoAction(ServoState state = IDLE, uint8_t pos = 0, uint8_t spd = 0, uint16_t del = 0)
        : stateType(state), targetPosition(pos), speed(spd), delay(del) {}
};

struct Servo {
    uint8_t ServoID;
    uint8_t currentActionIndex;
    ServoAction* actionList[MAX_ACTIONS];
    ServoAction persoAction;
    uint8_t currentPosition;
    bool direction;
    unsigned long timer; // Pour enregistrer le temps actuel avec millis()

    // Constructeur avec argument pour ServoID
    Servo() : ServoID(0), currentActionIndex(0), persoAction(ServoAction()), currentPosition(0), direction(true), timer(0) {
        for (int i = 0; i < MAX_ACTIONS; ++i) {
            actionList[i] = nullptr;  // Initialiser tous les pointeurs à nullptr
        }
    }
};

class ServoHandler {
private:
    Adafruit_PWMServoDriver& pwmDriver;
    Servo* servos[NUMBER_OF_SERVO];
    void handleMoveState(Servo &servo, ServoAction &action);
    void handleWaitState(Servo &servo, ServoAction &action);

public:
    ServoHandler(Adafruit_PWMServoDriver& pwmDriver);
    bool addServo(Servo* newServo);
    void begin();
    void loop();
    void initializeAction(Servo &servo, bool resetActionIndex);
    void stop(Servo &servo);
    void stop();
    void move(uint8_t position, uint8_t id);
    void moveAll(uint8_t position);

};
