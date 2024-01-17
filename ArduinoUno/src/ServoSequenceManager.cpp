#include "ServoSequenceManager.h"

DispenserSequenceManager::DispenserSequenceManager(ServoHandler& handler, uint8_t order[NUMBER_OF_DISPENSER])
    : servoHandler(handler) {

    dispenserParams = {160, 1000, 130}; // positionMax, tMax ,positionRelease

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

void DispenserSequenceManager::dispenserAnimation(uint8_t speed, uint8_t positionMax, uint16_t delayFactor) {

    animation_1.targetPosition = positionMax;
    animation_1.speed = speed;
    animation_2.speed = speed;

    for (uint8_t i = 0; i < NUMBER_OF_DISPENSER; ++i) {
        uint16_t delay = i * delayFactor; // Calcule le délai en fonction de la position du servo

        servos[i].persoAction = ServoAction(WAIT, 0, 0, delay);  // Attendre avec le délai calculé

        servos[i].actionList[0] = &(servos[i].persoAction);
        servos[i].actionList[1] = &animation_1;
        servos[i].actionList[2] = &animation_2;

        servoHandler.initializeAction(servos[i], true);
    }
}
