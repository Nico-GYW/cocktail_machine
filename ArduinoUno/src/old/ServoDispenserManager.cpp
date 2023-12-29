#include <Arduino.h>
#include "ServoDispenserManager.h"


// Constructor
ServoDispenserManager::ServoDispenserManager(Adafruit_PWMServoDriver& pwmDriver, uint8_t servoOrder[8]) 
  : pwmDriver(pwmDriver) {
  
  // Initialize shared parameters (vous pouvez les initialiser selon vos besoins)
  engageWaitDuration = 1000;
  halfDispenseWaitDuration = 2000;
  fullDispenseWaitDuration = 6000;
  customWaitDuration = 800;
  positionStep = 7;
  idlePulseLen = 1500;
  engagePulseLen = 1000;
  dispensePulseLen = 2000;
  customUpPulseLen = 1800;

  // Servo Order
  for (int i = 0; i < 8; i++) {
        this->servoOrder[i] = servoOrder[i];
  }

  // Initialize each dispenser with given servo numbers
  for(int i = 0; i < 8; ++i) {
    dispensers[i].servoNum = servoOrder[i];
    dispensers[i].lastUpdate = 0;
    dispensers[i].state = IDLE_STATE;
    dispensers[i].currentPulseLen = idlePulseLen;
    dispensers[i].nextState = IDLE_STATE;
  }
}

void ServoDispenserManager::update() {
  // Loop through each dispenser and update its state
  for(int i = 0; i < 8; ++i) {
    Dispenser& dispenser = dispensers[i];

    unsigned long currentTime = millis();
    
    // State machine logic (à compléter selon vos besoins)
    switch(dispenser.state) {
      case IDLE_STATE:
          handleIdleState(dispenser);
          break;
      case ENGAGE_AND_WAIT_STATE:
          handleEngageAndWaitState(dispenser);
          break;
      case HALF_DISPENSE_AND_WAIT_STATE:
          handleHalfDispenseAndWaitState(dispenser);
          break;
      case FULL_DISPENSE_AND_WAIT_STATE:
          handleFullDispenseAndWaitState(dispenser);
          break;

      case CUSTOM_POSITION_UP_STATE:
          handleCustomPositionUpState(dispenser);
        break;

      case CUSTOM_WAIT_STATE:
          handleCustomWaitState(dispenser);
        break;

      case CUSTOM_POSITION_DOWN_STATE:
          handleCustomPositionDownState(dispenser);
        break;
    }

    dispenser.lastUpdate = currentTime;
  }
}

void ServoDispenserManager::handleIdleState(Dispenser& dispenser) {
    // Rien à faire dans l'état IDLE.
}

void ServoDispenserManager::handleEngageAndWaitState(Dispenser& dispenser) {
    pwmDriver.writeMicroseconds(dispenser.servoNum, engagePulseLen);
    
    if (millis() - dispenser.lastUpdate > engageWaitDuration) {
        dispenser.lastUpdate = millis();
        dispenser.state = dispenser.nextState;
        dispenser.nextState = IDLE_STATE; // Reset nextState pour éviter des surprises
    }
}

void ServoDispenserManager::handleHalfDispenseAndWaitState(Dispenser& dispenser) {
    pwmDriver.writeMicroseconds(dispenser.servoNum, dispensePulseLen);
    
    if (millis() - dispenser.lastUpdate > halfDispenseWaitDuration) {
        dispenser.lastUpdate = millis();
        dispenser.state = IDLE_STATE;
    }
}

void ServoDispenserManager::handleFullDispenseAndWaitState(Dispenser& dispenser) {
    pwmDriver.writeMicroseconds(dispenser.servoNum, dispensePulseLen);
    
    if (millis() - dispenser.lastUpdate > fullDispenseWaitDuration) {
        dispenser.lastUpdate = millis();
        dispenser.state = IDLE_STATE;
    }
}

void ServoDispenserManager::handleCustomPositionUpState(Dispenser& dispenser) {
    int16_t difference = customUpPulseLen - dispenser.currentPulseLen;
    if (difference > 0) {
        uint16_t step = min(positionStep, difference);  // Ne pas dépasser la position cible
        dispenser.currentPulseLen += step;
        pwmDriver.writeMicroseconds(dispenser.servoNum, dispenser.currentPulseLen);
    } else {
        dispenser.state = CUSTOM_WAIT_STATE;
        dispenser.lastUpdate = millis();
    }
}

void ServoDispenserManager::handleCustomWaitState(Dispenser& dispenser) {
    if (millis() - dispenser.lastUpdate >= customWaitDuration) {
        dispenser.state = CUSTOM_POSITION_DOWN_STATE;
    }
}

void ServoDispenserManager::handleCustomPositionDownState(Dispenser& dispenser) {
    int16_t difference = dispenser.currentPulseLen - idlePulseLen;
    if (difference > 0) {
        uint16_t step = min(positionStep, difference);  // Ne pas dépasser la position d'origine
        dispenser.currentPulseLen -= step;
        pwmDriver.writeMicroseconds(dispenser.servoNum, dispenser.currentPulseLen);
    } else {
        dispenser.state = IDLE_STATE;
    }
}

void ServoDispenserManager::activateServo(uint8_t index, ActionType action) {
    if (index < 8) { // Valider l'index
        Dispenser& dispenser = dispensers[servoOrder[index]];
        
        dispenser.lastUpdate = millis();
        dispenser.state = ENGAGE_AND_WAIT_STATE;
        
        // Configurer nextState en fonction de l'action
        if (action == ActionType::HALF_DISPENSE) {
            dispenser.nextState = HALF_DISPENSE_AND_WAIT_STATE;
        } else {
            dispenser.nextState = FULL_DISPENSE_AND_WAIT_STATE;
        }
    }
}

// Setters for shared parameters
void ServoDispenserManager::setEngageWaitDuration(uint16_t duration) {
  engageWaitDuration = duration;
}

void ServoDispenserManager::setHalfDispenseWaitDuration(uint16_t duration) {
  halfDispenseWaitDuration = duration;
}

void ServoDispenserManager::setFullDispenseWaitDuration(uint16_t duration) {
  fullDispenseWaitDuration = duration;
}

void ServoDispenserManager::setCustomWaitDuration(uint16_t duration) {
  customWaitDuration = duration;
}

void ServoDispenserManager::setServoSpeed(uint16_t speed) {
  positionStep = speed;
}

void ServoDispenserManager::setIdleServoAngle(uint16_t angle) {
  idlePulseLen = angle;
}

void ServoDispenserManager::setEngageServoAngle(uint16_t angle) {
  engagePulseLen = angle;
}

void ServoDispenserManager::setDispenseServoAngle(uint16_t angle) {
  dispensePulseLen = angle;
}

void ServoDispenserManager::setCustomUpServoAngle(uint16_t angle) {
  customUpPulseLen = angle;
}