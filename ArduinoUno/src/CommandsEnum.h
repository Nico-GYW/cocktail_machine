enum GlobalCommands {
    // Servo Command
    cmd_SERVO_dispenser,
    cmd_SERVO_dispenser_setting,
    cmd_SERVO_dispenser_stop,
    cmd_SERVO_dispenser_animation,

    cmd_SERVO_lemonBowl_open,
    cmd_SERVO_lemonBowl_close,
    cmd_SERVO_lemonBowl_setting,
    cmd_SERVO_lemonBowl_is_open,

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
