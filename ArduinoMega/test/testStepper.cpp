#include <AccelStepper.h>

// X motor
#define StepPinX A0
#define DirPinX A1
#define EnablePinX 38

AccelStepper stepper(AccelStepper::DRIVER, StepPinX, DirPinX); 

void setup()
{  
   stepper.setMaxSpeed(1000);
   stepper.setSpeed(50);	
}

void loop()
{  
   stepper.runSpeed();
}
