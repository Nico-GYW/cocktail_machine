#include "LemonSlideServo.h"

LemonSlideServo::LemonSlideServo(Adafruit_PWMServoDriver &pwmDriver, uint8_t servoChannel)
    : _pwmDriver(pwmDriver), _servoChannel(servoChannel), _currentState(IDLE_STATE), _currentPosition(0) {
    // Set default values for configuration
    _idlePosition = 0;
    _targetPosition = 180;
    _waitDuration = 1000; // 1 second by default
    _upSpeed = 4;        // This represents the amount of degrees the servo should move per update during the up motion
    _downSpeed = 4;      // This represents the amount of degrees the servo should move per update during the down motion
}

void LemonSlideServo::update() {
    switch (_currentState) {
        case IDLE_STATE:
            handleIdleState();
            break;
        case TARGET_POSITION_STATE_UP:
            handleTargetPositionStateUp();
            break;
        case WAIT_STATE:
            handleWaitState();
            break;
        case TARGET_POSITION_STATE_DOWN:
            handleTargetPositionStateDown();
            break;
    }
}

void LemonSlideServo::activate() {
    // Start the sequence by transitioning to the TARGET_POSITION_STATE_UP
    _currentState = TARGET_POSITION_STATE_UP;
}

void LemonSlideServo::setTargetPosition(uint16_t position) {
    _targetPosition = position;
}

void LemonSlideServo::setIdlePosition(uint16_t position) {
    _idlePosition = position;
    _currentPosition = position;
}

void LemonSlideServo::setWaitDuration(uint32_t duration) {
    _waitDuration = duration;
}

void LemonSlideServo::setUpSpeed(uint16_t speed) {
    _upSpeed = speed;
}

void LemonSlideServo::setDownSpeed(uint16_t speed) {
    _downSpeed = speed;
}

// Private Methods for state handling

void LemonSlideServo::handleIdleState() {
    // In the idle state, we just make sure the servo is at the idle position.
    _pwmDriver.writeMicroseconds(_servoChannel, _idlePosition);
}

void LemonSlideServo::handleTargetPositionStateUp() {
    // Move the servo to the target position at the specified upSpeed
    if (_currentPosition < _targetPosition) {
        _currentPosition += _upSpeed;
        _pwmDriver.writeMicroseconds(_servoChannel, _currentPosition);
    } else {
        // Transition to the next state once we've reached the target position
        _currentState = WAIT_STATE;
        _stateChangeTimestamp = millis(); // Capture the time when the state changed
    }
}

void LemonSlideServo::handleWaitState() {
    if (millis() - _stateChangeTimestamp >= _waitDuration) {
        // Transition to the next state after waiting the specified duration
        _currentState = TARGET_POSITION_STATE_DOWN;
    }
}

void LemonSlideServo::handleTargetPositionStateDown() {
    // Move the servo back to the idle position at the specified downSpeed
    if (_currentPosition > _idlePosition) {
        _currentPosition -= _downSpeed;
        _pwmDriver.writeMicroseconds(_servoChannel, _currentPosition);
    } else {
        // Transition back to the idle state once we've reached the idle position
        _currentState = IDLE_STATE;
    }
}
