#include "Servo.h"

#define USMIN  600 // This is the rounded 'minimum' microsecond length 0° (-90°)
#define USMAX  2400 // This is the rounded 'maximum' microsecond length 180° (+90°)

// Constructeur: initialise chaque servo avec des valeurs par défaut.
ServoHandler::ServoHandler(Adafruit_PWMServoDriver& pwmDriver) : pwmDriver(pwmDriver) {
    for (int i = 0; i < NUMBER_OF_SERVO; ++i) {
        servos[i] = nullptr;  // Initialiser tous les pointeurs à nullptr
    }
}

void ServoHandler::begin(){
    pwmDriver.begin(); 
    pwmDriver.setOscillatorFrequency(27000000);
    pwmDriver.setPWMFreq(50);
}

bool ServoHandler::addServo(Servo* newServo){
    for (int i = 0; i < NUMBER_OF_SERVO; ++i) {
        if (servos[i] == nullptr) {
            servos[i] = newServo;
            return true;
        }
    }
    return false; // Liste pleine
}

// Gère l'état de mouvement d'un servo.
void ServoHandler::handleMoveState(Servo &servo, ServoAction &action) {
    // Calcule et applique le pas de mouvement.
    int moveStep = servo.direction ? action.speed : -action.speed;
    servo.currentPosition += moveStep;
    pwmDriver.writeMicroseconds(servo.ServoID, map(servo.currentPosition, 0, 180, USMIN, USMAX));

    // Vérifie si la position cible est atteinte.
    if ((servo.direction && servo.currentPosition >= action.targetPosition) ||
        (!servo.direction && servo.currentPosition <= action.targetPosition)) {
        servo.currentActionIndex++;
        initializeAction(servo, false);
    }
}

// Gère l'état d'attente d'un servo.
void ServoHandler::handleWaitState(Servo &servo, ServoAction &action) {
    // Calcule le temps écoulé depuis le début de l'attente.
    unsigned long elapsed = millis() - servo.timer;
    if (elapsed >= action.delay) {
        servo.timer = 0;  // Réinitialise le timer.
        servo.currentActionIndex++;
        initializeAction(servo, false);
    }
}

// Initialise la prochaine action d'un servo.
void ServoHandler::initializeAction(Servo &servo, bool resetActionIndex = false) {
    
    if(resetActionIndex){
        servo.currentActionIndex = 0;
    }
    
    ServoAction &action = *(servo.actionList[servo.currentActionIndex]);

    switch (action.stateType) {
        case MOVE:
            // Détermine la direction du mouvement en fonction de la position actuelle et de la position cible.
            servo.direction = servo.currentPosition < action.targetPosition;
            break;
        case WAIT:
            // Initialise le timer pour l'attente.
            servo.timer = millis();
            pwmDriver.writeMicroseconds(servo.ServoID, map(action.targetPosition, 0, 180, USMIN, USMAX));
            break;
        case IDLE:
            // Place le servo dans une position de repos.
            pwmDriver.writeMicroseconds(servo.ServoID, map(action.targetPosition, 0, 180, USMIN, USMAX));
            break;
        default:
            // Gestion des cas inattendus.
            break;
    }
}

// Méthode principale pour traiter les actions de chaque servo dans une boucle.
void ServoHandler::loop() {
    for (int i = 0; i < NUMBER_OF_SERVO; ++i) {
        if (servos[i] != nullptr) { // Vérifie si le pointeur n'est pas nul
            // Récupère l'action courante du servo.
            ServoAction &action = *(servos[i]->actionList[servos[i]->currentActionIndex]);

            // Traite l'action en fonction de son type.
            switch (action.stateType){
                case MOVE:
                    handleMoveState(*servos[i], action);
                    break;
                case WAIT:
                    handleWaitState(*servos[i], action);
                    break;
                case IDLE:
                    // Aucune action particulière pour l'état IDLE.
                    break;
                default:
                    // Gestion des états non reconnus.
                    break;
            }
        }
    }
}

// Arrête un servo en le plaçant dans son état de repos.
void ServoHandler::stop(Servo &servo) {
    servo.currentActionIndex = MAX_ACTIONS - 1;  // Place l'index sur l'action de repos.
    initializeAction(servo, false);
}

// Arrête tous les servos en les plaçant dans leur état de repos.
void ServoHandler::stop() {
    for (int i = 0; i < NUMBER_OF_SERVO; ++i) {
        if (servos[i] != nullptr) { // Vérifie si le pointeur n'est pas nul
            stop(*servos[i]); // Déréférence le pointeur et appelle la fonction stop pour chaque servo
        }
    }
}
