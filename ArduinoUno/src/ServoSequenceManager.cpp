#include "ServoSequenceManager.h"


// ------------- DispenserSequenceManager ------------------ //


DispenserSequenceManager::DispenserSequenceManager(ServoHandler& handler, uint8_t order[NUMBER_OF_DISPENSER])
    : servoHandler(handler) {

    dispenserParams = {160, 1000, 120, 0}; // positionMax, tMax ,positionRelease, positionIdle

    moveUp = ServoAction(WAIT, dispenserParams.positionMax, 0, dispenserParams.tMax);
    release = ServoAction(WAIT, dispenserParams.positionRelease, 0, 0);
    release_idle = ServoAction(IDLE, dispenserParams.positionRelease, 0, 0);
    idle = ServoAction(IDLE, dispenserParams.positionIdle, 0, 0);
    animation_1 = ServoAction(MOVE, 150, 0, 0); // Bouger à la position 150 avec une vitesse donnée
    animation_2 = ServoAction(MOVE, 0, 0, 0);   // Retour à la position 0 avec la même vitesse

    for (uint8_t i = 0; i < NUMBER_OF_DISPENSER; ++i) {
        // Création et initialisation des Servo directement dans le tableau servos
        servos[i].ServoID = order[i];

        for (int j = 0; j < MAX_ACTIONS - 1; ++j) {
            servos[i].actionList[j] = &idle;
        }

        // Ajouter le Servo au ServoHandler
        if (!servoHandler.addServo(&servos[i])) {
            // Gérer l'échec de l'ajout du servo
        }
    }
}

void DispenserSequenceManager::setDispenserParams(uint8_t positionMax, uint16_t tMax, uint8_t positionRelease) {
    dispenserParams.positionMax = positionMax;
    dispenserParams.tMax = tMax;
    dispenserParams.positionRelease = positionRelease;

    moveUp.targetPosition = positionMax;
    moveUp.delay = tMax;
    release_idle.targetPosition = positionRelease;
    release.targetPosition = positionRelease;
}

void DispenserSequenceManager::assignDispenserActions(uint8_t dispenserIndex, uint16_t releaseTime) {
    servos[dispenserIndex].actionList[0] = &moveUp;
    if (releaseTime <= 0) {
        servos[dispenserIndex].actionList[1] = &release_idle;
    } else {
        servos[dispenserIndex].actionList[1] = &release;
        release.delay = releaseTime;
    }
    servos[dispenserIndex].actionList[2] = &idle;
    servoHandler.initializeAction(servos[dispenserIndex], true);
}

void DispenserSequenceManager::stopDispenser(uint8_t dispenserIndex){
    servos[dispenserIndex].actionList[0] = &idle;
    servoHandler.initializeAction(servos[dispenserIndex], true);
}

void DispenserSequenceManager::dispenserAnimation(uint8_t dispenserIndex, uint8_t speed, uint8_t positionMax, uint16_t delayFactor) {
    if (dispenserIndex >= NUMBER_OF_DISPENSER) {
        return;
    }

    animation_1.targetPosition = positionMax;
    animation_1.speed = speed;
    animation_2.speed = speed;

    servos[dispenserIndex].persoAction = ServoAction(WAIT, 0, 0, delayFactor);  // Attendre avec le délai calculé

    servos[dispenserIndex].actionList[0] = &(servos[dispenserIndex].persoAction);
    servos[dispenserIndex].actionList[1] = &animation_1;
    servos[dispenserIndex].actionList[2] = &animation_2;

    servoHandler.initializeAction(servos[dispenserIndex], true);
}



// ------------- LemonBowlSequenceManager ------------------ //


LemonBowlSequenceManager::LemonBowlSequenceManager(ServoHandler& handler, uint8_t servoID)
    : servoHandler(handler) {

    lemonBowlParams = {100, 0, 20}; // positionOpen, positionMax ,speed

    openMove = ServoAction(MOVE, lemonBowlParams.positionOpen, lemonBowlParams.speed, 0);
    openIdle = ServoAction(IDLE, lemonBowlParams.positionOpen, 0, 0);
    closedMove = ServoAction(MOVE, lemonBowlParams.positionClosed, lemonBowlParams.speed, 0);
    closedIdle = ServoAction(IDLE, lemonBowlParams.positionClosed, 0, 0);

    servo.ServoID = servoID;
    for (int j = 0; j < MAX_ACTIONS - 1; ++j) {
        servo.actionList[j] = &closedIdle;
    }
    servoHandler.addServo(&servo);
}

void LemonBowlSequenceManager::setLemonBowlParams(uint8_t positionOpen, uint16_t positionClosed, uint8_t speed) {
    lemonBowlParams.positionOpen = positionOpen;
    lemonBowlParams.positionClosed = positionClosed;
    lemonBowlParams.speed = speed;

    openMove.targetPosition = positionOpen;
    openMove.speed = speed;
    openIdle.targetPosition = positionOpen;

    closedMove.targetPosition = positionClosed;
    closedMove.speed = speed;
    closedIdle.targetPosition = positionClosed;
}

void LemonBowlSequenceManager::openBowl() {
    servo.actionList[0] = &openMove;
    servo.actionList[1] = &openIdle;
    servoHandler.initializeAction(servo, true);
}

void LemonBowlSequenceManager::closeBowl() {
    servo.actionList[0] = &closedMove;
    servo.actionList[1] = &closedIdle;
    servoHandler.initializeAction(servo, true);
}

bool LemonBowlSequenceManager::isBowlOpen() {
    return servo.currentPosition == lemonBowlParams.positionOpen;
}


// ------------- LemonRampSequenceManager ------------------ //


LemonRampSequenceManager::LemonRampSequenceManager(ServoHandler& handler, uint8_t servoID)
    : servoHandler(handler), servo() {
    // Initialize RampParams with default values
    rampParams = {120, 0, 0, 100, 100, 500}; // Default values for down position, up position, idle position, speed, down and up wait delays

    // Initialize ServoAction objects with initial parameters
    moveDown = ServoAction(MOVE, rampParams.positionDown, rampParams.speed, 0);
    downWait = ServoAction(WAIT, rampParams.positionDown, 0, rampParams.downWaitDelay);
    downIdle = ServoAction(IDLE, rampParams.positionDown, 0, 0);
    moveUp = ServoAction(MOVE, rampParams.positionUp, rampParams.speed, 0);
    upWait = ServoAction(WAIT, rampParams.positionUp, 0, rampParams.upWaitDelay);
    upIdle = ServoAction(IDLE, rampParams.positionIdle, 0, 0);
    idle = ServoAction(IDLE, rampParams.positionUp, 0, 0); // The idle position is the same as the up position

    servo.ServoID = servoID;
    // Initialize all action pointers to idle to start in a known state
    for (int i = 0; i < MAX_ACTIONS; ++i) {
        servo.actionList[i] = &idle;
    }

    // Add the servo to the ServoHandler for management
    servoHandler.addServo(&servo);
}

void LemonRampSequenceManager::setRampParams(uint8_t positionDown, uint8_t positionUp, uint8_t positionIdle, uint8_t speed, uint16_t downWaitDelay, uint16_t upWaitDelay) {
    rampParams.positionDown = positionDown;
    rampParams.positionUp = positionUp;
    rampParams.positionIdle = positionIdle;
    rampParams.speed = speed;
    rampParams.downWaitDelay = downWaitDelay;
    rampParams.upWaitDelay = upWaitDelay;

    moveDown.targetPosition = positionDown;
    moveDown.speed = speed;
    downWait.targetPosition = positionDown;
    downWait.delay = downWaitDelay;
    downIdle.targetPosition = positionDown;

    moveUp.targetPosition = positionUp;
    moveUp.speed = speed;
    upWait.targetPosition = positionUp;
    upWait.delay = upWaitDelay;
    upIdle.targetPosition = positionIdle;

    idle.targetPosition = positionUp; // Assuming the idle position is the same as the up position
}

void LemonRampSequenceManager::releaseLemon() {
    servo.actionList[0] = &moveDown;
    servo.actionList[1] = &downWait;
    servo.actionList[2] = &moveUp;
    servo.actionList[3] = &upWait;
    servoHandler.initializeAction(servo, true);
}

void LemonRampSequenceManager::moveDownOnly() {
    servo.actionList[0] = &moveDown;
    servo.actionList[1] = &downIdle;
    servoHandler.initializeAction(servo, true);
}

void LemonRampSequenceManager::moveUpOnly() {
    servo.actionList[0] = &moveUp;
    servo.actionList[1] = &upIdle;
    servo.actionList[2] = &idle;
    servoHandler.initializeAction(servo, true);
}

void LemonRampSequenceManager::customPosition(uint8_t position) {
    servoHandler.move(position, servo.ServoID);
}