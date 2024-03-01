#include "ServoSequenceManager.h"

DispenserSequenceManager::DispenserSequenceManager(ServoHandler& handler, uint8_t order[NUMBER_OF_DISPENSER])
    : servoHandler(handler) {

    dispenserParams = {160, 1000, 120}; // positionMax, tMax ,positionRelease

    moveUp = ServoAction(WAIT, dispenserParams.positionMax, 0, dispenserParams.tMax);
    release = ServoAction(WAIT, dispenserParams.positionRelease, 0, 0);
    release_idle = ServoAction(IDLE, dispenserParams.positionRelease, 0, 0);
    idle = ServoAction();
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
    servos[dispenserIndex].actionList[3] = &idle;
    servoHandler.initializeAction(servos[dispenserIndex], true);
}

void DispenserSequenceManager::stopDispenser(uint8_t dispenserIndex){
    servoHandler.stop(servos[dispenserIndex]);
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

LemonBowlSequenceManager::LemonBowlSequenceManager(ServoHandler& handler, uint8_t servoID)
    : servoHandler(handler) {

    lemonBowlParams = {0, 180, 10}; // positionOpen, positionMax ,speed

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