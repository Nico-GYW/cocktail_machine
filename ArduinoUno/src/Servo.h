#include <SPI.h>
#include <Adafruit_PWMServoDriver.h>

#define MAX_ACTIONS 5  // Nombre maximum d'actions par servo
#define NUMBER_OF_SERVO 16  // Nombre total de servo

enum ServoState {
    IDLE,
    MOVE,
    WAIT
};

struct ServoStateParams {
    ServoState stateType;
    int targetPosition;
    int speed;
    unsigned long timer;
};

struct Servo {
    int restPosition;
    int currentPosition;
    int numberID;
    ServoStateParams actionList[MAX_ACTIONS];
    int currentActionIndex;
};

class ServoHandler {
private:
    Adafruit_PWMServoDriver& pwmDriver;
    Servo servos[NUMBER_OF_SERVO];
    void ServoHandler::handleMoveState(Servo &servo, ServoStateParams &action);
    void ServoHandler::handleWaitState(Servo &servo, ServoStateParams &action);

public:
    ServoHandler(Adafruit_PWMServoDriver& pwmDriver);
    void loop();
    void ServoHandler::assignActions(int servoIndex, ServoStateParams newActions[], int sizeOfNewActions);
    void ServoHandler::stop(int servoIndex);

}