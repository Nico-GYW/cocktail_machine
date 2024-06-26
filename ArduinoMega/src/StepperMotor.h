#ifndef StepperMotor_h
#define StepperMotor_h

#include <AccelStepper.h>
#include "CmdMessenger.h"
#include "CommandsEnum.h"

class StepperMotor {
  public:
    enum MotorState {
      IDLE_STATE,
      MOVING_STATE,
      MOVING_TO_HOME_STATE,
      REACHED_HOME_STATE,
    };

    StepperMotor(int stepPin, int dirPin, int endStop, int enablePin, bool isXStepper);
    void begin();
    void loop();
    void moveTo(int position);
    void home();
    void stop();
    long getPosition();
    int getCurrentState();
    void setSpeed(int speed);

  private:
    void handleIdleState();
    void handleMovingState();
    void handleHomingReverseState(bool isEndStopReached);
    void handleHomingForwardState(bool isEndStopReached);

    AccelStepper stepper;
    MotorState currentState;
    int endStop;
    int enablePin;
    bool isXStepper;
};

#endif
