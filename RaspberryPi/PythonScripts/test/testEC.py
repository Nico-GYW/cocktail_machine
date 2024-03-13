class ElectricCylinderController(Controller):
    FULL_CYCLE_DURATION = 7800  # Temps nécessaire pour faire une course complète du cylindre en ms

    def __init__(self, cmd_arduino_uno):
        super().__init__(cmd_arduino_uno)
        self.interrupt = asyncio.Event()
        self.lock = asyncio.Lock()  # Verrou pour synchroniser l'accès au port série
        self.position = 0
        self.current_process = None

    def move_forward(self, duration: int):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_forward", duration)
            msg = self.cmd.receive()
            print(msg)

    def move_backward(self, duration: int):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_backward", duration)
            msg = self.cmd.receive()
            print(msg)

    def stop(self):
        with self.lock:  # Applique le verrou pour éviter l'accès concurrent
            self.cmd.send("cmd_EC_stop")
            msg = self.cmd.receive()
            print(msg)

    async def go_home(self):
        async with self.lock:
            self.cmd.send("cmd_EC_backward", self.FULL_CYCLE_DURATION + 500)
            await asyncio.sleep((self.FULL_CYCLE_DURATION + 500) / 1000)
            if self.interrupt.is_set():
                self.interrupt.clear()
                return
            self.position = 0

    async def check_interrupt_and_sleep(self, duration):
        if self.interrupt:
            self.interrupt = False
            return True
        await asyncio.sleep(duration)
        if self.interrupt.is_set():
            self.interrupt.clear()
            return True  # Interruption détectée après le sommeil
        return False  # Pas d'interruption

    async def press_lemon(self, cycle_number: int):
        DELAY = 1000
        INITIAL_ADVANCE_DURATION = self.FULL_CYCLE_DURATION - DELAY
        BACK_AND_FORTH_DURATION = 200

        async with self.lock:
            if self.position != 0:
                await self.go_home()
            self.cmd.send("cmd_EC_forward", INITIAL_ADVANCE_DURATION)
            if await self.check_interrupt_and_sleep(INITIAL_ADVANCE_DURATION / 1000):
                return  # Interrompt la fonction si une interruption est détectée

            for _ in range(cycle_number):
                self.cmd.send("cmd_EC_backward", BACK_AND_FORTH_DURATION)
                if await self.check_interrupt_and_sleep(BACK_AND_FORTH_DURATION / 1000):
                    return  # Interrompt la fonction si une interruption est détectée

                self.cmd.send("cmd_EC_forward", BACK_AND_FORTH_DURATION + DELAY)
                if await self.check_interrupt_and_sleep((BACK_AND_FORTH_DURATION + DELAY) / 1000):
                    return  # Interrompt la fonction si une interruption est détectée

            if not self.interrupt.is_set():
                await self.go_home()

    def go_home_interrupt(self):
        self.interrupt.set()
        # Planifiez go_home de manière asynchrone si nécessaire

    def stop_interrupt(self):
        self.interrupt.set()
        # Envoyez la commande d'arrêt immédiatement si nécessaire