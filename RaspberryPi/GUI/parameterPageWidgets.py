from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QDialog, QComboBox, QColorDialog, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_bottleDialog import Ui_bottleDialog
from ui_bottleParameter import Ui_bottleParameter
from ui_dispenserControl import Ui_dispenserControl

from pompetteUtils import  clear_grid_layout
from mainPageWidgets import machine

class ParameterPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.objectControls = []

    def setup(self, ui):
        self.ui = ui
        self.changeParameterPage(0)
        ui.toolButtonParameterPage.clicked.connect(lambda: self.changeMainPage(1))
        ui.pushButtonBottleParameter.clicked.connect(lambda: self.changeParameterPage(0))
        ui.pushButtonSoftParameter.clicked.connect(lambda: self.changeParameterPage(1))
        ui.pushButtonMachineParameter.clicked.connect(lambda: self.changeParameterPage(2))
        ui.pushButtonMachineSettings.clicked.connect(lambda: self.changeParameterPage(3))
        self.ui.rightButtonControl.clicked.connect(self.incrementerPage)
        self.ui.leftButtonControl.clicked.connect(self.decrementerPage)

        self.adjust_brightness(255)
        self.set_bottle_glasses()
        self.set_bottle_plastic()
        self.set_dispenser_control_page()
        self.set_soft_control_page()
        self.set_settings_page()
        self.set_other_control_page()

    def changeMainPage(self, pageIndex):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(pageIndex)
        self.ui.mainPageStacked.setCurrentIndex(0)

    def changeParameterPage(self, pageIndex):
        stacked_widget = self.ui.parameterStack
        stacked_widget.setCurrentIndex(pageIndex)

    def incrementerPage(self):
        index_courant = self.ui.machineParameterStack.currentIndex()
        nombre_total_pages = self.ui.machineParameterStack.count()
        # Incrémenter l'index ou revenir à la première page
        nouvel_index = (index_courant + 1) % nombre_total_pages
        self.ui.machineParameterStack.setCurrentIndex(nouvel_index)

    def decrementerPage(self):
        index_courant = self.ui.machineParameterStack.currentIndex()
        nombre_total_pages = self.ui.machineParameterStack.count()
        # Décrémenter l'index ou aller à la dernière page si à la première page
        nouvel_index = (index_courant - 1 + nombre_total_pages) % nombre_total_pages
        self.ui.machineParameterStack.setCurrentIndex(nouvel_index)

    def set_settings_page(self):
        # Connexion du powerButton pour quitter l'application
        self.ui.powerButton.clicked.connect(self.confirm_quit)

        # Connexion du brightnessSlider pour ajuster la luminosité
        self.ui.brightnessSlider.valueChanged.connect(self.adjust_brightness)

        # Lire la valeur actuelle de la luminosité et l'ajuster si nécessaire
        self.initialize_brightness()

    def confirm_quit(self):
        reply = QMessageBox.question(self, 'Confirmation',
                                     "Êtes-vous sûr de vouloir quitter ?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.instance().quit()

    def initialize_brightness(self):
        # Chemin vers le fichier de luminosité
        brightness_file_path = "/sys/class/backlight/10-0045/brightness"
        
        try:
            # Lire la valeur actuelle de la luminosité
            with open(brightness_file_path, 'r') as file:
                current_brightness = int(file.read().strip())

            # Si la luminosité actuelle est inférieure à 50, la régler sur 100
            if current_brightness < 50:
                current_brightness = 100
                with open(brightness_file_path, 'w') as file:
                    file.write(str(current_brightness))

            # Régler la valeur du slider sur la luminosité actuelle
            self.ui.brightnessSlider.setValue(current_brightness)

        except FileNotFoundError:
            print("Le fichier de luminosité n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la lecture ou de l'écriture de la luminosité: {e}")

    def adjust_brightness(self, value):
        # Chemin vers le fichier de luminosité, remplacez '<id_backlight>' par le votre
        brightness_file_path = "/sys/class/backlight/10-0045/brightness"

        # Assurez-vous d'avoir les permissions nécessaires pour écrire dans ce fichier
        try:
            with open(brightness_file_path, 'w') as f:
                f.write(str(value))
        except PermissionError:
            QMessageBox.critical(self, 'Erreur', "Permission refusée pour écrire dans le fichier de luminosité.")
        except FileNotFoundError:
            QMessageBox.critical(self, 'Erreur', "Le fichier de luminosité n'a pas été trouvé.")
        except Exception as e:
            QMessageBox.critical(self, 'Erreur', f"Une erreur inattendue est survenue: {str(e)}")

    def set_bottle_glasses(self):
        clear_grid_layout(self.ui.gridLayoutGlass)

        glass_bottles = machine.get_glass_bottles()
        num_columns = 4  # Nombre total de colonnes dans le gridLayout
        for i, bottle in enumerate(glass_bottles[:8]):  # Limite à 8 bouteilles
            bottle_param = BottleParameter(bottle.name, bottle.quantity, bottle.position, True, self)
            # Calcul pour un remplissage de droite à gauche
            row, col = divmod(i, num_columns)
            self.ui.gridLayoutGlass.addWidget(bottle_param, row, col)

    def set_bottle_plastic(self):
        clear_grid_layout(self.ui.gridLayoutPlastic)

        plastic_bottles = machine.get_soft_bottles()  # Utilise machine.get_soft_bottles()
        num_columns = 2  # Nombre total de colonnes dans le gridLayout (4 bouteilles / 2 colonnes)
        for i, bottle in enumerate(plastic_bottles[:4]):  # Limite à 4 bouteilles
            bottle_param = BottleParameter(bottle.name, bottle.quantity, bottle.position, False, self)  # Utilise False pour le type de bouteille
            # Calcul pour un remplissage de droite à gauche
            row, col = divmod(i, num_columns)
            self.ui.gridLayoutPlastic.addWidget(bottle_param, row, col)

    def set_dispenser_control_page(self):
        clear_grid_layout(self.ui.dispenserGridLayout)

        num_columns = 4
        for i in range(8):  # Pour 8 bouteilles
            bottle_name = f"Bouteille {i+1}"
            dispenser_param = DispenserControl(self, bottle_name)
            row, col = divmod(i, num_columns)
            self.ui.dispenserGridLayout.addWidget(dispenser_param, row, col)

    def set_soft_control_page(self):
        clear_grid_layout(self.ui.softGridLayout)

        num_columns = 4
        for i in range(4):  # Pour 8 bouteilles
            bottle_name = f"Bouteille {i+1}"
            soft_param = SoftControl(self, bottle_name)
            row, col = divmod(i, num_columns)
            self.ui.softGridLayout.addWidget(soft_param, row, col)

    def set_other_control_page(self):
        # Créer une instance de StepperControl et la stocker dans la liste
        xStepperControl = SliderLinearControl(self.ui.xStepperSlider, "X")
        yStepperControl = SliderLinearControl(self.ui.yStepperSlider, "Y")
        cylinderControl = SliderLinearControl(self.ui.cylinderSlider, "V")
        ledstrip = ledStripControl(self.ui)

        self.objectControls.append(xStepperControl)
        self.objectControls.append(yStepperControl) 
        self.objectControls.append(cylinderControl) 
        self.objectControls.append(ledstrip) 

        self.ui.xStepperButton.clicked.connect(xStepperControl.goHome)
        self.ui.yStepperButton.clicked.connect(yStepperControl.goHome)
        self.ui.cylinderButton.clicked.connect(cylinderControl.goHome)

class BottleParameter(QFrame):
    def __init__(self, name="", quantity=0, position=0, is_glass=False, parent=None):
        super().__init__(parent)
        self.ui = Ui_bottleParameter()
        self.ui.setupUi(self)
        self.set_bottle_data(name, quantity, position)
        self.position = position
        self.is_glass = is_glass

    def set_bottle_data(self, name, quantity, position):
        self.ui.title.setText(f"Bouteille {position}")
        self.ui.content.setText(f"{name}")
        self.ui.quantity.setText(f"{quantity}ml")

    def mousePressEvent(self, event):
        dialog = BottleDialog(self.ui.title.text(), machine, self)
        dialog.exec_()

class BottleDialog(QDialog):
    def __init__(self, bottle_name="", machine=None, parent=None):
        super(BottleDialog, self).__init__(parent)
        self.ui = Ui_bottleDialog()
        self.ui.setupUi(self)

        self.machine = machine
        self.bottle_name = bottle_name
        self.position = parent.position
        self.is_glass = parent.is_glass

        self.initializeDialog()

    def initializeDialog(self):
        self.ui.title.setText(self.bottle_name)

        # Charger les valeurs possibles dans le QComboBox
        if self.machine:
            bottle_list = self.machine.get_bottle_list(self.is_glass)
            self.ui.bottleComboBox.clear()
            self.ui.bottleComboBox.addItems(bottle_list)
            # Mettre la valeur par défaut sur la valeur du contenu de la bouteille
            index = self.ui.bottleComboBox.findText(self.bottle_name, Qt.MatchFixedString)
            if index >= 0:
                self.ui.bottleComboBox.setCurrentIndex(index)

        # Connecter le bouton "Valider" à la méthode de mise à jour de la machine
        self.ui.buttonBox.accepted.connect(self.update_machine)

    def update_machine(self):
        if self.machine:
            new_bottle_name = self.ui.bottleComboBox.currentText()
            new_quantity = self.ui.quantitySpinBox.value()
            bottle_type = "glass" if self.is_glass else "soft"
            self.machine.change_bottle(bottle_type, self.position, new_bottle_name, new_quantity)
            self.parent().ui.content.setText(f"{new_bottle_name}")
            self.parent().ui.quantity.setText(f"{new_quantity}ml")
            self.accept()  # Fermer la boîte de dialogue après la mise à jour

class DispenserControl(QFrame):
    def __init__(self, parent=None, title=""):
        super(DispenserControl, self).__init__(parent)
        self.ui = Ui_dispenserControl()
        self.ui.setupUi(self)
        self.ui.titleLabel.setText(title)

class SoftControl(DispenserControl):
    def __init__(self, parent=None, title=""):
        super(SoftControl, self).__init__(parent, title)

class SliderLinearControl():
    def __init__(self, stepperSlider, control_type="X"):
        self.control_type = control_type
        self.stepperSlider = stepperSlider
        self.commandTimer = QTimer()  # Créer un QTimer pour l'envoi périodique de la commande
        self.commandTimer.setInterval(1000)  # Définir l'intervalle à 1000 ms (1 seconde)
        self.commandTimer.timeout.connect(self.sendCommand)  # Connecter le signal timeout du QTimer
        
        # Connecter les signaux du slider
        self.stepperSlider.sliderPressed.connect(self.startSendingCommand)
        self.stepperSlider.sliderReleased.connect(self.stopSendingCommandAndReset)

    def startSendingCommand(self):
        if self.stepperSlider.value() != 0:  # Vérifier si le slider n'est pas déjà à 0
            self.commandTimer.start()  # Commencer à envoyer la commande périodiquement

    def stopSendingCommandAndReset(self):
        self.commandTimer.stop()  # Arrêter d'envoyer la commande
        self.stepperSlider.setValue(0)  # Réinitialiser la valeur du slider à 0

    def sendCommand(self):
        position = self.stepperSlider.value()  # Obtenir la position actuelle du slider
        if self.control_type == "X":
            print("Send Stepper X cmd with position " + str(position))
        elif self.control_type == "Y":
            print("Send Stepper Y cmd with position " + str(position))
        else:  # Pour le vérin électrique
            print("Send Verin cmd with position " + str(position))

    def goHome(self):
        if self.control_type == "X":
            print("Stepper Motor X Go Home")
        elif self.control_type == "Y":
            print("Stepper Motor Y Go Home")
        else:  # Pour le vérin électrique
            print("Verin Go Home")


class ledStripControl:
    def __init__(self, ui):
        self.ui = ui
        # self.ledStripController = ledStripController
        
        self.ui.ledStripComboBox.addItems(["Éteind", "Allumé", "Pulsation", "Rotation"])

        # Configurer les signaux
        self.ui.ledStripComboBox.currentIndexChanged.connect(self.updateLedStripSettings)
        self.ui.ledStripSpeedSpinBox.valueChanged.connect(self.updateLedStripSettings)
        self.ui.ledStripBrightnessSpinBox.valueChanged.connect(self.updateLedStripSettings)
        self.ui.ledStripColorButton.clicked.connect(self.chooseColor)

        # Définir la couleur par défaut du bouton
        self.updateButtonColor("#F79643")

    def chooseColor(self):
        color = QColorDialog.getColor(QColor(self.ui.ledStripColorButton.styleSheet().split(": ")[1].split(";")[0]))
        if color.isValid():
            self.updateButtonColor(color.name())
            self.updateLedStripSettings()

    def updateButtonColor(self, color):
        self.ui.ledStripColorButton.setStyleSheet(f"background-color: {color};\nborder-radius: 50px;")

    def updateLedStripSettings(self):
        mode = self.ui.ledStripComboBox.currentText()
        speed = self.ui.ledStripSpeedSpinBox.value()
        brightness = self.ui.ledStripBrightnessSpinBox.value()
        color = QColor(self.ui.ledStripColorButton.styleSheet().split(": ")[1].split(";")[0])

        if mode == "Éteind":
            state_type = "F"
            # self.ledStripController.set_settings(state_type, 0, 0, 0, 0, 0)
            print(("LedStrip éteind"))
        elif mode == "Allumé":
            state_type = "T"
            # self.ledStripController.set_settings(state_type, color.red(), color.green(), color.blue(), brightness, 0)
            print(("LedStrip allumé"))
        elif mode == "Pulsation":
            state_type = "P"
            # self.ledStripController.set_settings(state_type, color.red(), color.green(), color.blue(), 0, speed)
            print(("LedStrip pulsation"))
        elif mode == "Rotation":
            state_type = "R"
            # self.ledStripController.set_settings(state_type, color.red(), color.green(), color.blue(), 0, speed)
            print(("LedStrip rotation"))

    def convertColorToRgb(self, qcolor):
        color = QColor(qcolor)
        return color.red(), color.green(), color.blue()