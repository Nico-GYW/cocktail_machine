#ifndef SERVO_MOTOR_COMMANDS_H
#define SERVO_MOTOR_COMMANDS_H

#include "ServoDispenserManager.h"
#include "LemonSlideServo.h"
#include "CmdMessenger.h"

// Enum for DispenserServo Commands
enum DispenserServoCommands {
  cmd_DispenserSetEngageWaitDuration,
  cmd_DispenserSetHalfDispenseWaitDuration,
  cmd_DispenserSetFullDispenseWaitDuration,
  cmd_DispenserSetCustomWaitDuration,
  cmd_DispenserSetServoSpeed,
  cmd_DispenserSetIdleServoAngle,
  cmd_DispenserSetEngageServoAngle,
  cmd_DispenserSetDispenseServoAngle,
  cmd_DispenserSetCustomUpServoAngle,
  cmd_DispenserActivateServo,
  cmd_DispenserAck // acknowledge command
};

// Enum for LemonSlideServo Commands
enum LemonSlideServoCommands {
  cmd_LemonSetTargetPosition,
  cmd_LemonSetIdlePosition,
  cmd_LemonSetWaitDuration,
  cmd_LemonSetUpSpeed,
  cmd_LemonSetDownSpeed,
  cmd_LemonActivate,
  cmd_LemonAck // acknowledge command
};

// Function declarations for DispenserServo
void onDispenserSetEngageWaitDuration();
void onDispenserSetHalfDispenseWaitDuration();
void onDispenserSetFullDispenseWaitDuration();
void onDispenserSetCustomWaitDuration();
void onDispenserSetServoSpeed();
void onDispenserSetIdleServoAngle();
void onDispenserSetEngageServoAngle();
void onDispenserSetDispenseServoAngle();
void onDispenserSetCustomUpServoAngle();
void onDispenserActivateServo();
void attachDispenserServoCommands();

// Function declarations for LemonSlideServo
void onLemonSetTargetPosition();
void onLemonSetIdlePosition();
void onLemonSetWaitDuration();
void onLemonSetUpSpeed();
void onLemonSetDownSpeed();
void onLemonActivate();
void attachLemonSlideServoCommands();

// Function declaration for all Servo
void init();


#endif // SERVO_MOTOR_COMMANDS_H
