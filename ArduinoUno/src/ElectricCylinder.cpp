#include "ElectricCylinder.h"

ElectricCylinder::ElectricCylinder(int pinControlA, int pinControlB)
: _pinControlA(pinControlA), _pinControlB(pinControlB), _timer(0), _delay(0), _isTiming(false), _state(IDLE_LOW) {
}

void ElectricCylinder::begin() {
  pinMode(_pinControlA, OUTPUT);
  pinMode(_pinControlB, OUTPUT);
  stopIdleLow(); // Initial state to idle low
}

void ElectricCylinder::loop() {
  if (_state == FORWARD || _state == BACKWARD) {
    if (millis() - _timer >= _delay) {
      stopIdleLow(); // Retour à l'état idle low après expiration du timer
    }
  }
}

void ElectricCylinder::moveForward(unsigned long duration) {
  digitalWrite(_pinControlA, HIGH);
  digitalWrite(_pinControlB, LOW);
  _state = FORWARD;
  _timer = millis(); // Démarre le timer
  _delay = duration; // Définit le temps avant le changement d'état
}

void ElectricCylinder::moveBackward(unsigned long duration) {
  digitalWrite(_pinControlA, LOW);
  digitalWrite(_pinControlB, HIGH);
  _state = BACKWARD;
  _timer = millis(); // Démarre le timer
  _delay = duration; // Définit le temps avant le changement d'état
}

void ElectricCylinder::stopIdleHigh() {
  digitalWrite(_pinControlA, HIGH);
  digitalWrite(_pinControlB, HIGH);
  _state = IDLE_HIGH;
}

void ElectricCylinder::stopIdleLow() {
  digitalWrite(_pinControlA, LOW);
  digitalWrite(_pinControlB, LOW);
  _state = IDLE_LOW;
}
