import commandUno as command  # Remplacez 'commandArduino' par le nom de votre fichier contenant les classes de contrôleurs
import time

# Créez des instances des contrôleurs
dispenser_controller = command.DispenserController()
servo_handler = command.ServoHandler()
valve_controller = command.DCValveController()


# Test du DispenserController
print("Test du DispenserController")
dispenser_index = 0  # Remplacez par l'index de votre distributeur
release_time = 2000  # Durée de l'action en millisecondes (2000 ms = 2 secondes)

# Activez le distributeur avec un temps de libération spécifique
print("Activation du distributeur")
dispenser_controller.activate_dispenser(dispenser_index, release_time)
dispenser_controller.set_dispenser_settings(160, 1000, 120)

dispenser_controller.animate_dispensers(20, 100, 100)

time.sleep(5)  # Attendez pour observer l'action

# Réinitialisation du distributeur
print("Arrêt du distributeur")
dispenser_controller.stop_dispenser(dispenser_index)
time.sleep(2)  # Attendez avant de passer au test suivant

# Test du DCValveController
print("Test du DCValveController")
valve_index = 1  # Remplacez par l'index de votre vanne

# Ouvrir la vanne
print("Ouverture de la vanne")
valve_controller.open_valve(valve_index, release_time)
time.sleep(5)  # Attendez pour observer l'action

# Fermer la vanne
print("Fermeture de la vanne")
valve_controller.close_valve(valve_index)
time.sleep(2)  # Attendez avant de passer au test suivant

# Arrêter toutes les vannes
print("Arrêt de toutes les vannes")
valve_controller.stop_all_valves()
time.sleep(2)  # Fin du test
