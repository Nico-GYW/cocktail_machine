#include "DispenserCommand.h"

ServoStateParams* createDispenserActions(const DispenserParams& params) {
    static ServoStateParams actions[3];

    actions[0] = {params.position_max, params.speed, 0, params.t_max, WAIT}; // WAIT à x_max pour 1000 ms
    actions[1] = {params.position_release, params.speed, 0, params.t_release, WAIT}; // WAIT à p_release pour t_release
    actions[2] = {0, 0, 0, IDLE}; // Repos à la position 0

    return actions;
}