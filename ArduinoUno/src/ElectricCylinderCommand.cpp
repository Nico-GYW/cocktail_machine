#include "CmdMessenger.h"
#include "ElectricCylinder.h"
#include "CommandsEnum.h"

// Déclarations externes et partagées
extern CmdMessenger cmdMessenger;

// Création de l'instance de ElectricCylinder
ElectricCylinder electricCylinder(10, 11); // Utiliser les pins appropriés

void beginElectricCylinder() {
    electricCylinder.begin(); // Initialisation du vérin électrique
}

void updateElectricCylinder() {
    electricCylinder.loop(); // Mise à jour de l'état du vérin électrique
}

static void onElectricCylinderForward() {
    unsigned long duration = static_cast<unsigned long>(cmdMessenger.readBinArg<int>());
    electricCylinder.moveForward(duration);
    cmdMessenger.sendCmd(cmd_ack, F("Electric Cylinder moving forward"));
}

static void onElectricCylinderBackward() {
    unsigned long duration = static_cast<unsigned long>(cmdMessenger.readBinArg<int>());
    electricCylinder.moveBackward(duration);
    cmdMessenger.sendCmd(cmd_ack, F("Electric Cylinder moving backward"));
}

static void onElectricCylinderStop() {
    electricCylinder.stopIdleLow(); // Ou stopIdleHigh selon le besoin
    cmdMessenger.sendCmd(cmd_ack, F("Electric Cylinder stopped"));
}

void attachElectricCylinderCommands() {
    cmdMessenger.attach(cmd_EC_forward, onElectricCylinderForward);
    cmdMessenger.attach(cmd_EC_backward, onElectricCylinderBackward);
    cmdMessenger.attach(cmd_EC_stop, onElectricCylinderStop);
}