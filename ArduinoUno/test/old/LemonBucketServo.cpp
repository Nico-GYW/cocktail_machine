#include "LemonBucketServo.h"

LemonBucketServo::LemonBucketServo(Adafruit_PWMServoDriver &pwmDriver, uint8_t servoChannel)
    : _pwmDriver(pwmDriver), _servoChannel(servoChannel), _currentState(CLOSED_STATE), _currentPosition(_closedPosition) {
    _openPosition = 1000;
    _closedPosition = 2000;
    _speed = 1;
}

void LemonBucketServo::openBucket() {
    _currentState = OPENING_STATE;
}

void LemonBucketServo::closeBucket() {
    _currentState = CLOSING_STATE;
}

void LemonBucketServo::update() {
    switch (_currentState) {
        case OPEN_STATE:
            handleOpenState();
            break;
        case CLOSED_STATE:
            handleClosedState();
            break;
        case OPENING_STATE:
            handleOpeningState();
            break;
        case CLOSING_STATE:
            handleClosingState();
            break;
    }
}

void LemonBucketServo::handleOpenState() {
    // Nothing to do when it's fully open
}

void LemonBucketServo::handleOpeningState() {
    if (_currentPosition != _openPosition) {
        _currentPosition += _speed;
        if (_currentPosition > _openPosition) _currentPosition = _openPosition;
        _pwmDriver.writeMicroseconds(_servoChannel, _currentPosition);
    } else {
        _currentState = OPEN_STATE;
    }
}

void LemonBucketServo::handleClosedState() {
    // Nothing to do when it's fully closed
}

void LemonBucketServo::handleClosingState() {
    if (_currentPosition != _closedPosition) {
        _currentPosition -= _speed;
        if (_currentPosition < _closedPosition) _currentPosition = _closedPosition;
        _pwmDriver.writeMicroseconds(_servoChannel, _currentPosition);
    } else {
        _currentState = CLOSED_STATE;
    }
}

void LemonBucketServo::setSpeed(uint16_t speed) {
    _speed = speed;
}

LemonBucketServo::State LemonBucketServo::getState() const {
    return _currentState;
}
