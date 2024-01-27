#include "DCValve.h"

// Constructeur: initialise chaque servo avec des valeurs par défaut.
DCValveHandler::DCValveHandler(int pins[NUMBER_OF_VALVES]) {
    for (int i = 0; i < NUMBER_OF_VALVES; i++) {
        valves[i].pin = pins[i];
    }
}

void DCValveHandler::begin(){
    for (int i = 0; i < NUMBER_OF_VALVES; i++) {
        pinMode(valves[i].pin, OUTPUT);
        digitalWrite(valves[i].pin, HIGH);

    }
}

// Gère l'état d'attente d'un servo.
void DCValveHandler::handleWaitState(DCValve &valve) {
    // Calcule le temps écoulé depuis le début de l'attente.
    unsigned long elapsed = millis() - valve.timer;
    if (elapsed >= valve.delay) {
        valve.timer = 0;  // Réinitialise le timer.
        close(valve);
    }
}

// Méthode principale pour traiter les actions de chaque vanne dans une boucle.
void DCValveHandler::loop() {
    for (int i = 0; i < NUMBER_OF_VALVES; ++i) {
        // Récupère l'action courante du servo.
        ValveState state = valves[i].state;

        // Traite l'action en fonction de son type.
        switch (state){
            case WAIT:
                handleWaitState(valves[i]);
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

void DCValveHandler::open(int valveIndex, unsigned long delay = 0){
    digitalWrite(valves[valveIndex].pin, LOW);

    if (delay == 0) {
        // Comportement de la fonction 'open'
        valves[valveIndex].state = IDLE;
    } else {
        // Comportement de la fonction 'openAndWait'
        valves[valveIndex].timer = millis();
        valves[valveIndex].delay = delay;
        valves[valveIndex].state = WAIT;
    }
}

void DCValveHandler::close(int valveIndex){
    digitalWrite(valves[valveIndex].pin, HIGH);
    valves[valveIndex].state = IDLE;
}

void DCValveHandler::close(DCValve &valve){
    digitalWrite(valve.pin, HIGH);
    valve.state = IDLE;
}

void DCValveHandler::stop() {
    for (int i = 0; i < NUMBER_OF_VALVES; ++i) {
        close(valves[i]);
    }
}
