from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer, QPropertyAnimation


import time
import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

import random

from ui_cocktailStep import Ui_cocktailStep
from ui_cocktailStep1Button import Ui_cocktailStep1Button
from ui_cocktailStep2Button import Ui_cocktailStep2Button

from mainPageWidgets import machine
from commandMega import *
from commandUno import *

class ProcessPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cocktailRecipe = None

    def setup(self, ui):
        self.ui = ui
        self.setEndPage()
        self.set_controllers()

    def set_controllers(self):
        self.EC = ElectricCylinderController()
        self.stepperMotorController = StepperMotorController()
        self.LemonRampController = LemonBowlController()
        self.LemnBowlController = LemonRampController()
        self.DispenserController = DispenserController()
        self.LedController = LedStripController()
        self.ValveController = DCValveController()

    def setRecipe(self, recipe):
        self.cocktailRecipe = recipe
        print("Set Recipe")
        self.totalPhases = self.calculateTotalPhases()
        self.progressValue = 0
        self.ui.cocktailProgressBar.setValue(0)
        self.step1PrepareGlassStep()
        
    def clearCocktailStepLayout(self):
        # Supprime tous les widgets du layout
        for i in reversed(range(self.ui.CocktailStepVerticalLayout.count())): 
            widget = self.ui.CocktailStepVerticalLayout.itemAt(i).widget()
            if widget is not None: 
                self.ui.CocktailStepVerticalLayout.removeWidget(widget)
                widget.deleteLater()

    def step1PrepareGlassStep(self):
        self.clearCocktailStepLayout()  # Videz le layout
        step = CocktailStep("En attente d’un verre", "Déposer un verre sur le plateau", num_buttons=1)  # Créez l'étape
        step.ui.button_1.setText("Fait !")  # Configurez le texte du bouton
        step.ui.button_1.clicked.connect(self.step2PourGlassBottles)  # Connectez le signal au slot pour passer à l'étape suivante
        print("step1PrepareGlassStep")
        self.ui.CocktailStepVerticalLayout.addWidget(step)  # Ajoutez le step au layout

    def calculateTotalPhases(self):
        # Calculer le nombre total de phases en fonction des éléments de la recette
        total_phases = 1 # set glass instruction
        total_phases += len(self.cocktailRecipe.glass_bottles)
        total_phases += len(self.cocktailRecipe.soft_drink_bottles)
        total_phases += 2  # Plusieurs sous-phases pour les citrons si nécessaire
        total_phases += 1 if self.cocktailRecipe.ice > 0 else 0
        return total_phases

    def updateProgress(self, progressValue):
        self.progressValue += progressValue
        progress = (self.progressValue / self.totalPhases) * 100
        print(f"Value Progress: {progress}")

        # Création de l'animation
        self.animation = QPropertyAnimation(self.ui.cocktailProgressBar, b"value")
        self.animation.setDuration(1000)  # Durée de l'animation en millisecondes, ajustez selon le besoin
        print(self.ui.cocktailProgressBar.value())
        self.animation.setStartValue(self.ui.cocktailProgressBar.value())  # Valeur de départ (valeur actuelle)
        self.animation.setEndValue(progress)  # Valeur finale (nouvelle valeur calculée)
        self.animation.start()  # Démarre l'animation

    def toggleInterrupt(self): # Interruption pour le bouton stop boutille
        self.bottleInterrupt = not self.bottleInterrupt
        print("Valeur de bottleInterrupt modifiée :", self.bottleInterrupt)  # Pour vérification

    def pourBottle(self, bottleType):
        self.clearCocktailStepLayout()
        self.bottleInterrupt = False
        self.ui.interuptButton.clicked.connect(self.toggleInterrupt)
        stepTitle = "Étape 2 : Bouteille en verre" if bottleType == "glass" else "Étape 3 : Bouteille de soft"
        self.currentStep = CocktailStep(stepTitle)  # Créez un seul CocktailStep pour cette étape
        self.ui.CocktailStepVerticalLayout.addWidget(self.currentStep)
        bottles = self.cocktailRecipe.glass_bottles if bottleType == "glass" else self.cocktailRecipe.soft_drink_bottles
        self.bottle_iterator = iter(bottles.items())  # Créer un itérateur sur les bouteilles
        self.pourNextBottle(bottleType)

    def pourNextBottle(self, bottleType):
        try:
            ingredient, required_quantity = next(self.bottle_iterator)
            self.currentStep.ui.subtitle.setText(f"{ingredient} - {required_quantity} ml")
            print(f"Verser {required_quantity}ml de {ingredient}")

            bottles_to_fetch = self.machine.fetch_bottles_for_ingredient(ingredient, bottleType, required_quantity)

            for bottle_position, position_xy, quantity_to_use in bottles_to_fetch:
                self.movementWithInterruptCheck(position_xy)
                self.dispenseWithInterruptCheck(bottle_position, quantity_to_use)
                print(f"Bouteille {bottle_position} à la position {position_xy} pour {quantity_to_use}ml versés")

            self.updateProgress(1)

        except StopIteration:
            if bottleType == "glass":
                self.step3PourSoftDrinks()
            else:
                self.step4HandleLemons()

    def movementWithInterruptCheck(self, position_xy):
        # Initie le déplacement 
        self.stepperMotorController.moveTo("X", position_xy[0])
        self.stepperMotorController.moveTo("Y", position_xy[1])

        # Boucle jusqu'à ce que le déplacement soit achevé, avec vérification des interruptions
        while not self.stepperMotorController.isAcked():
            if self.bottleInterrupt:
                # Arrêter le mouvement en cas d'interruption
                self.stepperMotorController.stop("X")
                self.stepperMotorController.stop("Y")
                
                # Attendre que l'interruption soit levée
                while self.bottleInterrupt:
                    time.sleep(0.1)  # Utilisez time.sleep pour éviter une utilisation CPU élevée

                # Reprendre le mouvement après l'interruption
                self.stepperMotorController.moveTo("X", position_xy[0])
                self.stepperMotorController.moveTo("Y", position_xy[1])

    def dispenseWithInterruptCheck(self, bottle_position, quantity_to_use):
        doses_needed = quantity_to_use // 25
        remaining_ml = quantity_to_use % 25

        for _ in range(doses_needed):
            total_time_ms = 7000  # Temps pour 25 ml
            self.waitForOrInterrupt(bottle_position, total_time_ms)

        if remaining_ml > 0:
            proportional_time_ms = int((remaining_ml / 25.0) * 7000)
            self.waitForOrInterrupt(bottle_position, proportional_time_ms)

    def waitForOrInterrupt(self, bottle_position, total_time_ms):
        start_time = time.time()  # Marque le début de la distribution
        elapsed_time_ms = 0

        self.DispenserController.activate_dispenser(bottle_position, total_time_ms)
        
        while elapsed_time_ms < total_time_ms:
            if self.bottleInterrupt:
                self.DispenserController.stop(bottle_position)  # Arrête la distribution
                interrupt_start_time = time.time()  # Marque le début de l'interruption

                # Attend que l'interruption soit levée
                while self.bottleInterrupt:
                    time.sleep(0.1)

                interrupt_time = (time.time() - interrupt_start_time) * 1000  # Calcule la durée de l'interruption
                start_time += interrupt_time / 1000  # Ajuste le temps de départ pour exclure le temps d'interruption
                
                # Réactive le distributeur avec le temps restant ajusté
                remaining_time_ms = total_time_ms - elapsed_time_ms
                self.DispenserController.activate_dispenser(bottle_position, remaining_time_ms)

            # Mise à jour du temps écoulé, excluant le temps d'interruption
            elapsed_time_ms = (time.time() - start_time) * 1000
            time.sleep(0.1)  # Attente active courte pour éviter une utilisation excessive du processeur

    # Les méthodes pour l'étape spécifique des bouteilles en verre et des bouteilles de soft
    def step2PourGlassBottles(self):
        self.updateProgress(1)
        self.pourBottle("glass")

    def step3PourSoftDrinks(self):
        self.pourBottle("soft")

    def step4HandleLemons(self):
        if self.cocktailRecipe.lemon > 0:  # Vérifiez si des citrons sont nécessaires
            self.askForLemonInBowl()
        else:
            self.step5CrushIce()  # Passez à l'étape suivante si pas de citrons nécessaires

    def askForLemonInBowl(self):
        self.clearCocktailStepLayout()
        step = CocktailStep("Étape 4 : Citrons", "Y a-t-il des citrons dans le bol ?", num_buttons=2)
        step.ui.button_1.setText("Oui")
        step.ui.button_2.setText("Non")
        step.ui.button_1.clicked.connect(self.checkLemonBowlOpen)
        step.ui.button_2.clicked.connect(self.startLemonCuttingProcess)
        self.ui.CocktailStepVerticalLayout.addWidget(step)

    def checkLemonBowlOpen(self):
        # isOpen = self.machine.checkLemonBowl()  # Méthode hypothétique pour vérifier l'état du bol
        isOpen = random.choice([True, False])  # Génère aléatoirement True ou False
        print(f"Le bol à citron est {'ouvert' if isOpen else 'fermé'}.")

        if isOpen:
            # Logique à exécuter si le bol est ouvert
            print("Le bol est déjà ouvert. Passage à l'étape suivante.")
            self.updateProgress(2)
            self.step5CrushIce()  # Remplacez nextStep par la méthode appropriée pour passer à l'étape suivante
        else:
            # Logique à exécuter si le bol est fermé
            print("Le bol est fermé. Demande d'ouverture.")
            self.updateProgress(1)
            self.askToOpenLemonBowl()  # Assurez-vous que cette méthode demande à l'utilisateur s'il veut ouvrir le bol à citron

    def askToOpenLemonBowl(self):
        # Création d'un CocktailStep pour demander à ouvrir le bol à citrons
        self.clearCocktailStepLayout()
        step = CocktailStep("Ouvrir le bol à citron ?", "", num_buttons=2)
        step.ui.button_1.setText("Oui")
        step.ui.button_2.setText("Non")
        step.ui.button_1.clicked.connect(self.combinedFunction2)
        step.ui.button_2.clicked.connect(self.combinedFunction1)  # Passer à l'étape suivante même si le bol n'est pas ouvert
        self.ui.CocktailStepVerticalLayout.addWidget(step)

    def combinedFunction1(self):
        self.updateProgress(1)
        self.step5CrushIce()

    def combinedFunction2(self):
        self.updateProgress(1/3)
        self.openLemonBowl()

    def openLemonBowl(self):
        # self.machine.openLemonBowl()  # Méthode hypothétique pour ouvrir le bol
        print("Ouverture du bol à citron de la machine")
        self.updateProgress(2/3)
        QTimer.singleShot(5000, self.nextStep)  # Donnez du temps pour l'ouverture avant de passer à la suite

    def startLemonCuttingProcess(self):
        self.clearCocktailStepLayout()
        self.updateProgress(1/3)
        step = CocktailStep("Découpe de citron", "Libération d'un citron dans la chambre de découpe", num_buttons=2)
        step.ui.button_1.setText("Citron bien placé ?")
        step.ui.button_2.setText("Presser le citron")
        step.ui.button_1.clicked.connect(self.askCitronPlacedCorrectly)
        step.ui.button_2.clicked.connect(self.pressLemon)
        self.ui.CocktailStepVerticalLayout.addWidget(step)

    def askCitronPlacedCorrectly(self):
        # Ici, on pourrait simuler la vérification ou demander directement à l'utilisateur
        self.updateProgress(1/3)
        citronPlaced = random.choice([True, False])  # Simule la vérification
        print(f"Citron correctement placé : {'Oui' if citronPlaced else 'Non'}")
        if citronPlaced:
            self.pressLemon()
        else:
            self.manuallyPlaceCitron()

    def manuallyPlaceCitron(self):
        self.clearCocktailStepLayout()
        step = CocktailStep("Découpe de citron", "Veuillez placer manuellement le citron dans la chambre de découpe.", num_buttons=1)
        step.ui.button_1.setText("Fait")
        step.ui.button_1.clicked.connect(self.pressLemon)
        self.ui.CocktailStepVerticalLayout.addWidget(step)

    def pressLemon(self):
        # Simule le pressage du citron
        step = CocktailStep("Découpe de citron", "", num_buttons=2)
        step.ui.button_1.setText("Pause")
        step.ui.button_2.setText("Annuler")
        step.ui.button_1.clicked.connect(self.askCitronPlacedCorrectly)
        step.ui.button_2.clicked.connect(self.interruptProcess)
        self.EC_interrput = False
        total_delay = 0
        
        FULL_CYCLE_DURATION = 8000
        BEFORE_BLADE_DELAY = 500
        INITIAL_ADVANCE_DURATION = FULL_CYCLE_DURATION - BEFORE_BLADE_DELAY
        BACK_AND_FORTH_DURATION = 1000

        if self.EC.position != 0:
            total_delay += 8500
            self.EC.go_home()
            QTimer.singleShot(total_delay, self.executeCommand(self.EC.set_position,0))
            
        QTimer.singleShot(total_delay, lambda: self.executeCommand(self.EC.move_forward, INITIAL_ADVANCE_DURATION))
        total_delay += INITIAL_ADVANCE_DURATION + 100
        QTimer.singleShot(total_delay, lambda: self.executeCommand(self.EC.move_backward, BACK_AND_FORTH_DURATION))
        total_delay += BACK_AND_FORTH_DURATION + 100
        QTimer.singleShot(total_delay, lambda: self.executeCommand(self.EC.move_forward, BACK_AND_FORTH_DURATION+BEFORE_BLADE_DELAY))

    def interruptProcess(self):
        self.EC_interrput = True
        self.EC.stop()
                              
    def executeCommand(self, command, *args, **kwargs):
        """Exécute une commande si aucune interruption n'a été signalée."""
        if not self.EC_interrput:
            command(*args, **kwargs)
        
    def lemonPressed(self):
        print("Les tranches de citron sont prêtes.")
        # Indiquez que les tranches sont dans le bol et passez à l'étape suivante après 5 secondes
        QTimer.singleShot(5000, self.nextStep)
        # Définissez ici les méthodes pour chaque phase spécifique de la découpe et de la pression des citrons

    def step5CrushIce(self):
        if self.cocktailRecipe.ice > 0:  # Vérifiez si de la glace est nécessaire
            self.showIceCrushingStep()
        else:
            self.changePage()  # Passez à la page suivante si pas de glace nécessaire

    def showIceCrushingStep(self):
        self.updateProgress()
        self.clearCocktailStepLayout()
        step = CocktailStep("Étape 5 : Pillage de glace", "Prêt à piler la glace ?", num_buttons=2)
        step.ui.button_1.setText("Piler")
        step.ui.button_2.setText("Terminer")
        step.ui.button_1.clicked.connect(self.crushIce)
        step.ui.button_2.clicked.connect(self.changePage)
        self.ui.CocktailStepVerticalLayout.addWidget(step)

    def crushIce(self):
        # Logique pour démarrer le pilage de la glace
        print("Pilage de la glace en cours...")  # Remplacer par la commande réelle pour piler la glace
        # Vous pouvez ajouter un QTimer.singleShot ici si vous souhaitez simuler un délai de pilage

    def changePage(self):
        # Logique pour changer de page ou passer à l'étape suivante de la préparation du cocktail
        self.ui.endTitle.setText(self.cocktailRecipe.name)
        self.ui.endCocktaiImage.setPixmap(QPixmap(self.cocktailRecipe.get_image()))
        self.ui.proccessingStackedWidget.setCurrentIndex(1)
        print("Changement de page ou étape suivante...")

    def setEndPage(self):
        self.ui.endButton.clicked.connect(self.changeMenuPage)
    
    def changeMenuPage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

class CocktailStep(QFrame):
    def __init__(self, title, subtitle="", num_buttons=0, parent=None):
        super().__init__(parent)

        # Sélectionner et initialiser l'interface utilisateur appropriée
        if num_buttons == 1:
            self.ui = Ui_cocktailStep1Button()
        elif num_buttons == 2:
            self.ui = Ui_cocktailStep2Button()
        else:
            self.ui = Ui_cocktailStep()

        self.ui.setupUi(self)
        self.ui.stepTitle.setText(title)
        self.ui.subtitle.setText(subtitle)
