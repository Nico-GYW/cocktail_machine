#ifndef LEMON_SLIDE_SERVO_H
#define LEMON_SLIDE_SERVO_H

#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>

class LemonSlideServo {
public:
    enum State {
        IDLE_STATE,
        TARGET_POSITION_STATE_UP,
        WAIT_STATE,
        TARGET_POSITION_STATE_DOWN
    };

    // Constructor
    LemonSlideServo(Adafruit_PWMServoDriver &pwmDriver, uint8_t servoChannel);

    // Update function to be called in the main loop
    void update();

    // Start the sequence to slide the lemon
    void activate();

    // Configuration setters
    void setTargetPosition(uint16_t position);
    void setIdlePosition(uint16_t position);
    void setWaitDuration(uint32_t duration);
    void setUpSpeed(uint16_t speed);
    void setDownSpeed(uint16_t speed);

private:
    void handleIdleState();
    void handleTargetPositionStateUp();
    void handleWaitState();
    void handleTargetPositionStateDown();

    Adafruit_PWMServoDriver &_pwmDriver;
    uint8_t _servoChannel;
    State _currentState;

    uint16_t _idlePosition;            // Starting position of the servo
    uint16_t _targetPosition;          // Target position where the lemon is slid
    uint32_t _waitDuration;            // Duration to wait in WAIT_STATE
    uint16_t _currentPosition;         // To track the current position
    uint16_t _upSpeed;                 // Speed to move up
    uint16_t _downSpeed;               // Speed to move down
    uint32_t _stateChangeTimestamp;    // Timestamp when the state was changed (for duration calculations)
};

#endif
