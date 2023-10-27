#ifndef StepperMotor_h
#define StepperMotor_h

#include <AccelStepper.h>

class StepperMotor {
  public:
    enum MotorState {
      IDLE_STATE,
      MOVING_STATE,
      MOVING_TO_HOME_STATE,
      REACHED_HOME_STATE,
    };

    StepperMotor(int stepPin, int dirPin, int endStop, int enablePin);
    void begin();
    void loop();
    void moveTo(int position);
    void home();
    void stop();
    long getPosition();
    int getCurrentState();

  private:
    void handleIdleState();
    void handleMovingState();
    void handleHomingReverseState(bool isEndStopReached);
    void handleHomingForwardState(bool isEndStopReached);

    AccelStepper stepper;
    MotorState currentState;
    int endStop;
    int enablePin;
};

#endif
