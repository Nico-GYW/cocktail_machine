#include <Arduino.h>

class ElectricCylinder {
  public:
    // Constructor
    ElectricCylinder(int pinControlA, int pinControlB);
    
    // Méthodes pour contrôler le cylindre
    void moveForward(unsigned long duration);
    void moveBackward(unsigned long duration);
    void stopIdleHigh();
    void stopIdleLow();
    void begin();
    void loop();

  private:
    // Pins pour le contrôle des relais
    int _pinControlA, _pinControlB;
    unsigned long _timer; // Pour stocker le moment du début d'une action
    unsigned long _delay; // Durée de l'action en millisecondes
    bool _isTiming; // Indique si un timer est actif
    
    // États possibles pour le cylindre
    enum State {FORWARD, BACKWARD, IDLE_HIGH, IDLE_LOW};
    State _state;
};

