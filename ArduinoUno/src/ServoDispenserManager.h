#ifndef SERVO_DISPENSER_MANAGER_H
#define SERVO_DISPENSER_MANAGER_H

#include <SPI.h>
#include <Adafruit_PWMServoDriver.h>


class ServoDispenserManager {
public:
  // Enum for dispenser state
  enum DispenserState {
    IDLE_STATE,
    ENGAGE_AND_WAIT_STATE,
    HALF_DISPENSE_AND_WAIT_STATE,
    FULL_DISPENSE_AND_WAIT_STATE,
    CUSTOM_POSITION_UP_STATE,
    CUSTOM_WAIT_STATE,
    CUSTOM_POSITION_DOWN_STATE  
  };

  // Enum for ActionType
  enum ActionType {
    HALF_DISPENSE,
    FULL_DISPENSE,
  };

  // Structure for individual dispenser
  struct Dispenser {
      uint8_t servoNum;
      unsigned long lastUpdate;
      DispenserState state;
      DispenserState nextState;
      uint16_t currentPulseLen;
  };

  // Constructor
  ServoDispenserManager(Adafruit_PWMServoDriver& pwmDriver, uint8_t servoOrder[8]);

  // Update function to update all dispensers
  void update();

  // Setters for shared parameters
  void setEngageWaitDuration(uint16_t duration);
  void setHalfDispenseWaitDuration(uint16_t duration);
  void setFullDispenseWaitDuration(uint16_t duration);
  void setCustomWaitDuration(uint16_t duration);
  void setServoSpeed(uint16_t speed);
  void setIdleServoAngle(uint16_t angle);
  void setEngageServoAngle(uint16_t angle);
  void setDispenseServoAngle(uint16_t angle);
  void setCustomUpServoAngle(uint16_t angle);

  void activateServo(uint8_t index, ActionType action);

private:
  // Shared parameters
  uint16_t engageWaitDuration;
  uint16_t halfDispenseWaitDuration;
  uint16_t fullDispenseWaitDuration;
  uint16_t customWaitDuration;
  uint16_t positionStep;
  uint16_t idlePulseLen;
  uint16_t engagePulseLen;
  uint16_t dispensePulseLen;
  uint16_t customUpPulseLen;

  // Adafruit PWM driver
  Adafruit_PWMServoDriver& pwmDriver;

  // Servo Order
  uint8_t servoOrder[8];

  // Array of dispensers
  Dispenser dispensers[8];

  // Méthodes pour gérer les états individuels
  void handleIdleState(Dispenser& dispenser);
  void handleEngageAndWaitState(Dispenser& dispenser);
  void handleHalfDispenseAndWaitState(Dispenser& dispenser);
  void handleFullDispenseAndWaitState(Dispenser &dispenser);
  void handleCustomPositionUpState(Dispenser &dispenser);
  void handleCustomWaitState(Dispenser& dispenser);
  void handleCustomPositionDownState(Dispenser& dispenser);
};

#endif // SERVO_DISPENSER_MANAGER_H
