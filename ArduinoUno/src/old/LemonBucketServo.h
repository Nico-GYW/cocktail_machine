#ifndef LEMON_BUCKET_SERVO_H
#define LEMON_BUCKET_SERVO_H

#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>

class LemonBucketServo {
public:
    enum State {
        OPEN_STATE,
        OPENING_STATE,
        CLOSED_STATE,
        CLOSING_STATE
    };

    LemonBucketServo(Adafruit_PWMServoDriver &pwmDriver, uint8_t servoChannel);

    // Update the state and position of the servo
    void update();

    // Open the bucket
    void openBucket();

    // Close the bucket
    void closeBucket();

    // Set servo speed (for both opening and closing)
    void setSpeed(uint16_t speed);

    // Get the current state
    State getState() const;

private:
    Adafruit_PWMServoDriver &_pwmDriver;
    uint8_t _servoChannel;
    int _openPosition = 0;    // Default value, can be adjusted
    int _closedPosition = 180; // Default value, can be adjusted
    int _currentPosition;
    int _targetPosition;
    int _speed;
    State _currentState;

    void moveToTargetPosition();

    // Handle individual states
    void handleOpenState();
    void handleOpeningState();
    void handleClosedState();
    void handleClosingState();
};

#endif // LEMON_BUCKET_SERVO_H
