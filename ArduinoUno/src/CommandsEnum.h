enum GlobalCommands {
    // Dispenser Servo Command
    cmd_SERVO_dispenser,
    cmd_SERVO_dispenser_setting,
    cmd_SERVO_dispenser_stop,
    cmd_SERVO_dispenser_animation,

    // LemonBowl Servo Command
    cmd_SERVO_lemonBowl_open,
    cmd_SERVO_lemonBowl_close,
    cmd_SERVO_lemonBowl_setting,
    cmd_SERVO_lemonBowl_is_open,

    // Lemon Ramp Servo Command
    cmd_SERVO_lemonRamp_release,
    cmd_SERVO_lemonRamp_down,
    cmd_SERVO_lemonRamp_up,
    cmd_SERVO_lemonRamp_custo,
    cmd_SERVO_lemonRamp_setting,

    // Servo Handler
    cmd_SERVO_handler_move,
    cmd_SERVO_handler_stop,

    // Valve Command
    cmd_VALVE_open,
    cmd_VALVE_close,
    cmd_VALVE_stop,

    // Electric Cylinder Command
    cmd_EC_forward,
    cmd_EC_backward,
    cmd_EC_stop,
    
    //Shared Command
    cmd_ack,
};
