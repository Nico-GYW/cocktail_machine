#include "StepperMotor.h"

StepperMotor::StepperMotor(int stepPin, int dirPin, int endStop, int enablePin) : 
    stepper(AccelStepper::DRIVER, stepPin, dirPin), 
    currentState(IDLE_STATE) {
    this->endStop = endStop;
    this->enablePin = enablePin;
}

void StepperMotor::begin() {
    pinMode(enablePin, OUTPUT);
    stepper.setEnablePin(enablePin);
    stepper.setPinsInverted(false, false, true);
    stepper.setMaxSpeed(200);
    stepper.setAcceleration(100);
}

// The main loop function to be called in the main loop
void StepperMotor::loop() {
    bool isEndStopReached = digitalRead(endStop);
    
    switch (currentState) {
        case IDLE_STATE:
            handleIdleState();
            break;
        case MOVING_STATE:
            handleMovingState();
            break;
        case MOVING_TO_HOME_STATE:
            handleHomingReverseState(isEndStopReached);
            break;
        case REACHED_HOME_STATE:
            handleHomingForwardState(isEndStopReached);
            break;
    }
}

void StepperMotor::handleIdleState() {
    if (stepper.distanceToGo()) {
        stepper.enableOutputs();
        currentState = MOVING_STATE;
    }
}

void StepperMotor::handleMovingState() {
    if (stepper.distanceToGo()) {
        stepper.run();
    } else {
        stepper.disableOutputs();
        currentState = IDLE_STATE;
    }
}

void StepperMotor::handleHomingReverseState(bool isEndStopReached) {
    if (isEndStopReached) {
        currentState = REACHED_HOME_STATE;
    } else {
        stepper.move(-1);
        stepper.run();
    }
}

void StepperMotor::handleHomingForwardState(bool isEndStopReached) {
    if (!isEndStopReached) {
        stepper.setCurrentPosition(0);
        currentState = IDLE_STATE;
        // Generate an interrupt or feedback here
    } else {
        stepper.move(1);
        stepper.run();
    }
}

void StepperMotor::moveTo(int position) {
    stepper.moveTo(position);
}

void StepperMotor::home() {
    currentState = MOVING_TO_HOME_STATE;
}

void StepperMotor::stop() {
    stepper.stop();
    stepper.disableOutputs();
    currentState = IDLE_STATE;
}

long StepperMotor::getPosition() {
    return stepper.currentPosition();
}

int StepperMotor::getCurrentState() {
    return static_cast<int>(currentState);
}

void updateServo(){
    
}