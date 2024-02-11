#include "CmdMessenger.h"
#include "ServoSequenceManager.h"
#include "CommandsEnum.h"

// Déclarations externes et partagée
extern CmdMessenger cmdMessenger;

// Déclaration des variable internes 
Adafruit_PWMServoDriver pwmDriver;
ServoHandler servoHandler(pwmDriver);

uint8_t servoOrder[NUMBER_OF_DISPENSER] = {0, 1, 14, 3, 11, 12, 4, 2, 15};
// {0, 1, 2, 3, 4, 5, 6, 7, 8};
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

void onDispenserAnimation() {
    uint8_t speed = cmdMessenger.readBinArg<int>();
    uint8_t positionMax = cmdMessenger.readBinArg<int>();
    uint16_t delayFactor = cmdMessenger.readBinArg<int>();
    uint8_t dispenserIndex = cmdMessenger.readBinArg<int>();

    if (dispenserIndex < NUMBER_OF_DISPENSER) {
        dispenserManager.dispenserAnimation(dispenserIndex, speed, positionMax, delayFactor);
        cmdMessenger.sendCmd(cmd_ack, "Dispenser(s) animated");
    } else {
        cmdMessenger.sendCmd(cmd_ack, "Dispenser index out of range");
        return;
    }
    
}

// ------------- Lemon bucket command ------------------ //

// ------------- Lemon ramp command ------------------ //

// ------------- Servo Handler ramp command ------------------ //

void onServoHandlerMove() {
    uint8_t position = cmdMessenger.readBinArg<int>();
    uint8_t id = cmdMessenger.readBinArg<int>();

    if (id < NUMBER_OF_SERVO) {
        servoHandler.move(position, id);
        cmdMessenger.sendCmd(cmd_ack, "Servo " + String(id) + " stopped at position " + String(position));
    } else {
        cmdMessenger.sendCmd(cmd_ack, "Servo index out of range");
    }
}

void onServoHandlerStop(){
    servoHandler.stop();
}

// Attacher les commandes du servo-moteur du distributeur au CmdMessenger
void attachServoCommands() {
    cmdMessenger.attach(cmd_SERVO_dispenser, onDispenser);
    cmdMessenger.attach(cmd_SERVO_dispenser_setting, onDispenserSettings);
    cmdMessenger.attach(cmd_SERVO_dispenser_stop, onDispenserStop);
    cmdMessenger.attach(cmd_SERVO_dispenser_animation, onDispenserAnimation);
    cmdMessenger.attach(cmd_SERVO_handler_move, onServoHandlerMove);
    cmdMessenger.attach(cmd_SERVO_handler_stop, onServoHandlerStop);
}

