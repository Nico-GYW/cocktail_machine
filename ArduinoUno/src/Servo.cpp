#include "Servo.h"


ServoHandler::ServoHandler(Adafruit_PWMServoDriver& pwmDriver) 
  : pwmDriver(pwmDriver) {
}

void ServoHandler::update() {
    for (int i = 0; i < NUMBER_OF_SERVO; ++i) {

        ServoStateParams &action = servos[i].actionList[servos[i].currentActionIndex];

        switch (action.currentState){
            case MOVE:
                handleMoveState(servos[i], action);
                break;
            case WAIT:
                handleWaitState(servos[i], action);
                break;
            case IDLE:
            default:
                // Logique pour IDLE, par exemple retourner à la position de repos
                break;
        }
    }
}

void ServoHandler::handleMoveState(Servo &servo, ServoStateParams &action) {

    int positionDifference = action.targetPosition - servo.currentPosition;

    int moveStep = (positionDifference > 0) ? action.speed : -action.speed;

    // Limiter le déplacement pour ne pas dépasser la position cible
    if ((moveStep > 0 && servo.currentPosition + moveStep > action.targetPosition) ||
        (moveStep < 0 && servo.currentPosition + moveStep < action.targetPosition)) {
        moveStep = positionDifference;
    }

    servo.currentPosition += moveStep;

    pwmDriver.writeMicroseconds(servo.numberID, servo.currentPosition);

    // Vérifier si la position cible est atteinte
    if (servo.currentPosition == action.targetPosition) {
        servo.currentActionIndex++; // Passer à l'action suivante
    }
}

void ServoHandler::handleWaitState(Servo &servo, ServoStateParams &action) {
    // Vérifier si le timer a déjà été initialisé
    if (action.timer == 0) {
        // Initialiser le timer avec le temps actuel
        pwmDriver.writeMicroseconds(servo.numberID, action.targetPosition);
        action.timer = millis();
    } else {
        // Calculer le temps écoulé
        unsigned long elapsed = millis() - action.timer;

        // Vérifier si le temps d'attente est écoulé
        if (elapsed >= action.timer) {
            // Réinitialiser le timer pour la prochaine fois
            action.timer = 0;

            // Passer à l'action suivante
            servo.currentActionIndex++;

            // Remettre le servo à la position de repos si nécessaire
            // Exemple : pwmDriver.writeMicroseconds(servo.restPosition, convertPositionToMicroseconds(servo.restPosition));
        }
    }
}

void ServoHandler::assignActions(int servoIndex, ServoStateParams newActions[], int sizeOfNewActions) {
    if (servoIndex >= 0 && servoIndex < NUMBER_OF_SERVO) {
        for (int i = 0; i < sizeOfNewActions; ++i) {
            servos[servoIndex].actionList[i] = newActions[i];
        }
        servos[servoIndex].currentActionIndex = 0;
        // Assurez-vous que la dernière action est IDLE ou ajustez selon les besoins
    }
}

void ServoHandler::stop(int servoIndex) {
    if (servoIndex >= 0 && servoIndex < NUMBER_OF_SERVO) {
        // Réinitialiser la séquence d'actions du servo
        for (int i = 0; i < MAX_ACTIONS; ++i) {
            servos[servoIndex].actionList[i] = {0, 0, 0, IDLE};
        }

        pwmDriver.writeMicroseconds(servoIndex, servos[servoIndex].restPosition);

        // Réinitialiser l'index de l'action courante
        servos[servoIndex].currentActionIndex = 0;
    }
}