void beginServo();
void updateServo();

//  Dispenser command 
void onDispenser();
void onDispenserSettings();
void onDispenserStop();
void onDispenserAnimation();

// Lemon bucket command 
void onLemonBowlOpen();
void onLemonBowlClose();
void onLemonBowlSetting();
void onLemonBowlIsOpen();

//  Lemon ramp command 
void onLemonRampRelease();
void onLemonRampDown();
void onLemonRampUp();
void onLemonRampCustomPosition();
void onLemonRampSetting();

// Servo Handler
void onServoHandlerMove();
void onServoHandlerStop();

void attachServoCommands();
