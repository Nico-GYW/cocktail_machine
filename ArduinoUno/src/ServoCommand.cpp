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
LemonBowlSequenceManager lemonBowlSequenceManager(servoHandler, 13);
LemonRampSequenceManager lemonRampSequenceManager(servoHandler, 10); 

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
    cmdMessenger.sendCmd(cmd_ack, F("New dispenser parameters"));
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
        cmdMessenger.sendCmd(cmd_ack, F("Dispenser(s) animated"));
    } else {
        cmdMessenger.sendCmd(cmd_ack, F("Dispenser index out of range"));
        return;
    }
    
}

// ------------- Lemon bucket command ------------------ //

void onLemonBowlOpen() {
    lemonBowlSequenceManager.openBowl();
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Bowl Opened"));
}

void onLemonBowlClose() {
    lemonBowlSequenceManager.closeBowl();
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Bowl Closed"));
}

void onLemonBowlSetting() {
    uint8_t positionOpen = cmdMessenger.readBinArg<int>();
    uint16_t positionClosed = cmdMessenger.readBinArg<int>();
    uint8_t speed = cmdMessenger.readBinArg<int>();

    lemonBowlSequenceManager.setLemonBowlParams(positionOpen, positionClosed, speed);
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Bowl Settings Updated"));
}

void onLemonBowlIsOpen() {
    bool isOpen = lemonBowlSequenceManager.isBowlOpen();
    cmdMessenger.sendCmd(cmd_ack, isOpen ? F("Open") : F("Closed"));
}

// ------------- Lemon ramp command ------------------ //

void onLemonRampRelease() {
    lemonRampSequenceManager.releaseLemon();
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Ramp Release executed"));
}

void onLemonRampDown() {
    lemonRampSequenceManager.moveDownOnly();
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Ramp Move Down executed"));
}

void onLemonRampUp() {
    lemonRampSequenceManager.moveUpOnly();
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Ramp Move Up executed"));
}

void onLemonRampCustomPosition() {
    uint8_t position = cmdMessenger.readBinArg<uint8_t>();
    lemonRampSequenceManager.customPosition(position);
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Ramp Custom Position executed"));
}

void onLemonRampSetting() {
    uint8_t positionDown = cmdMessenger.readBinArg<int>();
    uint8_t positionUp = cmdMessenger.readBinArg<int>();
    uint8_t speed = cmdMessenger.readBinArg<int>();
    uint16_t downWaitDelay = cmdMessenger.readBinArg<int>();
    uint16_t upWaitDelay = cmdMessenger.readBinArg<int>();

    lemonRampSequenceManager.setRampParams(positionDown, positionUp, speed, downWaitDelay, upWaitDelay);
    cmdMessenger.sendCmd(cmd_ack, F("Lemon Ramp Settings Updated"));
}

// ------------- Servo Handler command ------------------ //

void onServoHandlerMove() {
    uint8_t position = cmdMessenger.readBinArg<int>();
    uint8_t id = cmdMessenger.readBinArg<int>();

    if (id < NUMBER_OF_SERVO) {
        servoHandler.move(position, id);
        cmdMessenger.sendCmd(cmd_ack, "Servo " + String(id) + " stopped at position " + String(position));
    } else {
        cmdMessenger.sendCmd(cmd_ack, F("Servo index out of range"));
    }
}

void onServoHandlerStop(){
    servoHandler.stop();
}

// Attacher les commandes du servo-moteur du distributeur au CmdMessenger
void attachServoCommands() {

    // Commandes pour le Dispenser
    cmdMessenger.attach(cmd_SERVO_dispenser, onDispenser);
    cmdMessenger.attach(cmd_SERVO_dispenser_setting, onDispenserSettings);
    cmdMessenger.attach(cmd_SERVO_dispenser_stop, onDispenserStop);
    cmdMessenger.attach(cmd_SERVO_dispenser_animation, onDispenserAnimation);

    // Commandes pour Lemon Bowl
    cmdMessenger.attach(cmd_SERVO_lemonBowl_open, onLemonBowlOpen);
    cmdMessenger.attach(cmd_SERVO_lemonBowl_close, onLemonBowlClose);
    cmdMessenger.attach(cmd_SERVO_lemonBowl_setting, onLemonBowlSetting);
    cmdMessenger.attach(cmd_SERVO_lemonBowl_is_open, onLemonBowlIsOpen);

    // Commandes pour Lemon Ramp
    cmdMessenger.attach(cmd_SERVO_lemonRamp_release, onLemonRampRelease);
    cmdMessenger.attach(cmd_SERVO_lemonRamp_down, onLemonRampDown);
    cmdMessenger.attach(cmd_SERVO_lemonRamp_up, onLemonRampUp);
    cmdMessenger.attach(cmd_SERVO_lemonRamp_custo, onLemonRampCustomPosition);
    cmdMessenger.attach(cmd_SERVO_lemonRamp_setting, onLemonRampSetting);
    

    // Commandes pour le ServoHandler
    cmdMessenger.attach(cmd_SERVO_handler_move, onServoHandlerMove);
    cmdMessenger.attach(cmd_SERVO_handler_stop, onServoHandlerStop);
}


