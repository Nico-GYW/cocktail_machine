#include "CmdMessenger.h"
#include "DCValve.h"
#include "CommandsEnum.h"

// Déclarations externes et partagée
extern CmdMessenger cmdMessenger;

// Déclaration des variable internes 
int valvepins[NUMBER_OF_VALVES] = {2, 3, 4, 5};
DCValveHandler valveManager(valvepins);


void beginValve(){
    valveManager.begin();
}

void updateValve(){
    valveManager.loop();
}

void onValveOpen() {
    uint8_t valveIndex = cmdMessenger.readBinArg<int>();
    int releaseTime = cmdMessenger.readBinArg<int>();

    if (valveIndex < 0 || valveIndex > 3) {
        cmdMessenger.sendCmd(cmd_ack, "Error: valve index must be between 0 and 3");
    } else {
        valveManager.open(valveIndex, static_cast<unsigned long>(releaseTime));
        cmdMessenger.sendCmd(cmd_ack, "Valve " + String(valveIndex) + " open for " + String(releaseTime) + " ms");
    }
}

void onValveClose(){
    uint8_t valveIndex = cmdMessenger.readBinArg<int>();
    valveManager.close(valveIndex);
    cmdMessenger.sendCmd(cmd_ack, "Valve " + String(valveIndex) + " closed");
}

void onValveStop(){
    valveManager.stop();
    cmdMessenger.sendCmd(cmd_ack, "All valves closed");
}

// Attacher les commandes du servo-moteur du distributeur au CmdMessenger
void attachValveCommands() {
    cmdMessenger.attach(cmd_VALVE_open, onValveOpen);
    cmdMessenger.attach(cmd_VALVE_close, onValveClose);
    cmdMessenger.attach(cmd_VALVE_stop, onValveStop);
}
