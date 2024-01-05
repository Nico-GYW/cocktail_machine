#ifndef DispenserCommand_h
#define DispenserCommand_h

#include "Servo.h"  // Assurez-vous d'inclure ou de déclarer les types nécessaires

struct DispenserParams {
    int position_max;
    unsigned long t_max;
    int position_release;
    unsigned long t_release;
    int speed;
};

// Prototype de la fonction pour créer la liste d'actions
ServoStateParams* createDispenserActions(const DispenserParams& params);

#endif