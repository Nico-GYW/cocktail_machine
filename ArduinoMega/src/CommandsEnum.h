// commands_enum.h
#ifndef COMMANDS_ENUM_H
#define COMMANDS_ENUM_H

enum GlobalCommands {
    // StepperMotor
    cmd_moveToX,
    cmd_homeX,
    cmd_stopX,
    cmd_getPositionX,
    cmd_getStateX,
    cmd_moveToY,
    cmd_homeY,
    cmd_stopY,
    cmd_getPositionY,
    cmd_getStateY,

    //LedStrip
    cmd_LED_mode,
    cmd_LED_pulseBlock,
    cmd_LED_settings,

    //Shared Command
    cmd_ack,
};

#endif // COMMANDS_ENUM_H
