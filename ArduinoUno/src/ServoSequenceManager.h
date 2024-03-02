#include "Servo.h"  // Assurez-vous d'inclure ou de déclarer les types nécessaires
#define NUMBER_OF_DISPENSER 9

// Prototype de la fonction pour créer la liste d'actions

class DispenserSequenceManager {
    private:
        // Structure interne pour définir les paramètres d'un distributeur.
        struct DispenserParams {
            uint8_t positionMax;
            uint16_t tMax;
            uint8_t positionRelease;
        };

        ServoHandler& servoHandler; // Gère les servos associés aux distributeurs.
        DispenserParams dispenserParams; // Paramètres actuels des distributeurs.
        Servo servos[NUMBER_OF_DISPENSER]; // Ordre des servos pour les distributeurs.
        ServoAction moveUp;
        ServoAction release;
        ServoAction release_idle;
        ServoAction idle;
        ServoAction animation_1;
        ServoAction animation_2;
        
    public:
        DispenserSequenceManager(ServoHandler& handler, uint8_t order[8]);
        void setDispenserParams(uint8_t positionMax, uint16_t tMax, uint8_t positionRelease);
        void assignDispenserActions(uint8_t dispenserIndex, uint16_t releaseTime);
        void stopDispenser(uint8_t dispenserIndex);
        void dispenserAnimation(uint8_t dispenserIndex, uint8_t speed, uint8_t positionMax, uint16_t delayFactor);
};

class LemonBowlSequenceManager{
    private:

        struct LemonBowlParams {
            uint8_t positionOpen;
            uint8_t positionClosed;
            uint8_t speed;
        };

        ServoHandler& servoHandler;
        Servo servo;
        ServoAction openMove;
        ServoAction openIdle;
        ServoAction closedMove;
        ServoAction closedIdle;
        LemonBowlParams lemonBowlParams;

    public:
        LemonBowlSequenceManager(ServoHandler& handler, uint8_t servoID);

        void setLemonBowlParams(uint8_t positionOpen, uint16_t positionClosed, uint8_t speed);
        void closeBowl();
        void openBowl();
        bool isBowlOpen();
};

class LemonRampSequenceManager {
private:
    struct RampParams {
        uint8_t positionDown;
        uint8_t positionUp;
        uint8_t speed;
        uint16_t downWaitDelay;
        uint16_t upWaitDelay;
    };

    ServoHandler& servoHandler;
    Servo servo;
    RampParams rampParams;

    ServoAction moveDown;
    ServoAction downWait;
    ServoAction downIdle;
    ServoAction moveUp;
    ServoAction upWait;
    ServoAction upIdle;
    ServoAction idle;

public:
    LemonRampSequenceManager(ServoHandler& handler, uint8_t servoID);

    void setRampParams(uint8_t positionDown, uint8_t positionUp, uint8_t speed, uint16_t downWaitDelay, uint16_t upWaitDelay);
    void releaseLemon();
    void moveDownOnly();
    void moveUpOnly();
    void customPosition(uint8_t position);
};