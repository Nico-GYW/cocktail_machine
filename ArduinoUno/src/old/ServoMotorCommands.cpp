#include "ServoMotorCommands.h"
#include "ServoDispenserManager.h"
#include "LemonSlideServo.h"
#include "CmdMessenger.h"

// Déclarations externes et partagée
extern CmdMessenger cmdMessenger;
Adafruit_PWMServoDriver pwmDriver = Adafruit_PWMServoDriver(); 

// Déclaration des variable internes 
uint8_t servoOrder[8] = {0, 1, 2, 3, 4, 5, 6, 7};
ServoDispenserManager dispenserManager(pwmDriver, servoOrder);
LemonSlideServo lemonSlideServo(pwmDriver, 0);

// Déclaration des variable pour le LemonSlide Servo

void initServo(){
    pwmDriver.begin(); 
    pwmDriver.setPWMFreq(60);
}

// Fonction pour régler la durée d'attente d'engagement du distributeur
void onDispenserSetEngageWaitDuration() {
    uint16_t duration = cmdMessenger.readInt16Arg();
    dispenserManager.setEngageWaitDuration(duration);
    cmdMessenger.sendCmd(cmd_DispenserAck, "Duration set for engage wait");
}

// Fonction pour régler la durée d'attente de la demi-distribution
void onDispenserSetHalfDispenseWaitDuration() {
    uint16_t duration = cmdMessenger.readInt16Arg();
    dispenserManager.setHalfDispenseWaitDuration(duration);
    cmdMessenger.sendCmd(cmd_DispenserAck, "Duration set for half dispense wait");
}

// Fonction pour régler la durée d'attente de la distribution complète
void onDispenserSetFullDispenseWaitDuration() {
    uint16_t duration = cmdMessenger.readInt16Arg();
    dispenserManager.setFullDispenseWaitDuration(duration);
    cmdMessenger.sendCmd(cmd_DispenserAck, "Duration set for full dispense wait");
}

// Fonction pour régler la durée d'attente de la position personnalisée
void onDispenserSetCustomWaitDuration() {
    uint16_t duration = cmdMessenger.readInt16Arg();
    dispenserManager.setCustomWaitDuration(duration);
    cmdMessenger.sendCmd(cmd_DispenserAck, "Duration set for custom wait");
}

// Fonction pour régler la vitesse du servo-moteur du distributeur
void onDispenserSetServoSpeed() {
    uint16_t speed = cmdMessenger.readInt16Arg();
    dispenserManager.setServoSpeed(speed);
    cmdMessenger.sendCmd(cmd_DispenserAck, "Speed set for servo");
}

// Fonction pour activer le servo du distributeur pour une action spécifiée
void onDispenserActivateServo() {
    uint8_t index = static_cast<uint8_t>(cmdMessenger.readInt16Arg());
    uint8_t action = static_cast<uint8_t>(cmdMessenger.readInt16Arg());
    dispenserManager.activateServo(index, static_cast<ServoDispenserManager::ActionType>(action));
    cmdMessenger.sendCmd(cmd_DispenserAck, "Servo activated for action");
}

// Attacher les commandes du servo-moteur du distributeur au CmdMessenger
void attachDispenserServoCommands() {
    cmdMessenger.attach(cmd_DispenserSetEngageWaitDuration, onDispenserSetEngageWaitDuration);
    cmdMessenger.attach(cmd_DispenserSetHalfDispenseWaitDuration, onDispenserSetHalfDispenseWaitDuration);
    cmdMessenger.attach(cmd_DispenserSetFullDispenseWaitDuration, onDispenserSetFullDispenseWaitDuration);
    cmdMessenger.attach(cmd_DispenserSetCustomWaitDuration, onDispenserSetCustomWaitDuration);
    cmdMessenger.attach(cmd_DispenserSetServoSpeed, onDispenserSetServoSpeed);
    cmdMessenger.attach(cmd_DispenserActivateServo, onDispenserActivateServo);
}

// LemonSlide Servo Command Handlers

void onLemonSetTargetPosition() {
    int position = cmdMessenger.readInt16Arg();
    lemonSlideServo.setTargetPosition(position);
    cmdMessenger.sendCmd(cmd_LemonAck, "Target position set for LemonSlideServo");
}

void onLemonSetIdlePosition() {
    int position = cmdMessenger.readInt16Arg();
    lemonSlideServo.setIdlePosition(position);
    cmdMessenger.sendCmd(cmd_LemonAck, "Idle position set for LemonSlideServo");
}

void onLemonSetWaitDuration() {
    int duration = cmdMessenger.readInt16Arg();
    lemonSlideServo.setWaitDuration(duration);
    cmdMessenger.sendCmd(cmd_LemonAck, "Wait duration set for LemonSlideServo");
}

void onLemonSetUpSpeed() {
    int speed = cmdMessenger.readInt16Arg();
    lemonSlideServo.setUpSpeed(speed);
    cmdMessenger.sendCmd(cmd_LemonAck, "Up speed set for LemonSlideServo");
}

void onLemonSetDownSpeed() {
    int speed = cmdMessenger.readInt16Arg();
    lemonSlideServo.setDownSpeed(speed);
    cmdMessenger.sendCmd(cmd_LemonAck, "Down speed set for LemonSlideServo");
}

void onLemonActivate() {
    lemonSlideServo.activate();
    cmdMessenger.sendCmd(cmd_LemonAck, "LemonSlideServo activated");
}

void attachLemonSlideServoCommands() {
    cmdMessenger.attach(cmd_LemonSetTargetPosition, onLemonSetTargetPosition);
    cmdMessenger.attach(cmd_LemonSetIdlePosition, onLemonSetIdlePosition);
    cmdMessenger.attach(cmd_LemonSetWaitDuration, onLemonSetWaitDuration);
    cmdMessenger.attach(cmd_LemonSetUpSpeed, onLemonSetUpSpeed);
    cmdMessenger.attach(cmd_LemonSetDownSpeed, onLemonSetDownSpeed);
    cmdMessenger.attach(cmd_LemonActivate, onLemonActivate);
}