#include "CmdMessenger.h"
#include "ServoSequenceManager.h"
#include "CommandsEnum.h"

// Déclarations externes et partagée
extern CmdMessenger cmdMessenger;

// Déclaration des variable internes 
Adafruit_PWMServoDriver pwmDriver;
ServoHandler servoHandler(pwmDriver);

uint8_t servoOrder[8] = {0, 1, 2, 3, 4, 5, 6, 7};
DispenserSequenceManager dispenserManager(servoHandler, servoOrder);


void beginServo(){
    servoHandler.begin();
}

void updateServo(){
    servoHandler.loop();
}

// ------------- Dispenser command ------------------ //

void onDispenser(){
    uint8_t dispenserIndex = cmdMessenger.readBinArg<int>();
    uint16_t releaseTime = cmdMessenger.readBinArg<int>();
    dispenserManager.assignDispenserActions(dispenserIndex, releaseTime);
    cmdMessenger.sendCmd(cmd_ack, "Dispenser " + String(dispenserIndex) + " for " + String(releaseTime) + " ms");
}

void onDispenserSettings(){
    uint8_t positionMax = cmdMessenger.readBinArg<int>();
    uint16_t tMax = cmdMessenger.readBinArg<int>();
    uint8_t positionRelease = cmdMessenger.readBinArg<int>();

    dispenserManager.setDispenserParams(positionMax, tMax, positionRelease);
    cmdMessenger.sendCmd(cmd_ack, "New dispenser parameters");
}

void onDispenserStop(){
    uint8_t dispenserIndex = cmdMessenger.readBinArg<int>();
    dispenserManager.stopDispenser(dispenserIndex);
    cmdMessenger.sendCmd(cmd_ack, "Dispenser " + String(dispenserIndex) + " stopped");
}

void onDispenserAnimation(){
    uint8_t speed = cmdMessenger.readBinArg<int>();
    uint8_t positionMax = cmdMessenger.readBinArg<int>();
    uint16_t delayFactor = cmdMessenger.readBinArg<int>();

    dispenserManager.dispenserAnimation(speed, positionMax, delayFactor);
    cmdMessenger.sendCmd(cmd_ack, "Dispensers animated");
}

// ------------- Lemon bucket command ------------------ //

// ------------- Lemon ramp command ------------------ //


// Attacher les commandes du servo-moteur du distributeur au CmdMessenger
void attachServoCommands() {
    cmdMessenger.attach(cmd_SERVO_dispenser, onDispenser);
    cmdMessenger.attach(cmd_SERVO_dispenser_setting, onDispenserSettings);
    cmdMessenger.attach(cmd_SERVO_dispenser_stop, onDispenserStop);
    cmdMessenger.attach(cmd_SERVO_dispenser_stop, onDispenserAnimation);
}
