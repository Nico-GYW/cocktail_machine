from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QDialog, QComboBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_bottleDialog import Ui_bottleDialog
from ui_bottleParameter import Ui_bottleParameter

from mainPageWidgets import machine

class ParameterPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        self.ui = ui
        ui.toolButtonParameterPage.clicked.connect(lambda: self.changePage(1))
        self.set_bottle_glasses()

    def changePage(self, pageIndex):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(pageIndex)

    def set_bottle_glasses(self):
        # Vider gridLayoutGlass de tous ses widgets avant d'ajouter les nouveaux
        while self.ui.gridLayoutGlass.count():
            item = self.ui.gridLayoutGlass.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        glass_bottles = machine.get_glass_bottles()
        num_columns = 4  # Nombre total de colonnes dans le gridLayout
        for i, bottle in enumerate(glass_bottles[:8]):  # Limite à 8 bouteilles
            bottle_param = BottleParameter(bottle.name, bottle.quantity, bottle.position, True, self)
            # Calcul pour un remplissage de droite à gauche
            row, col = divmod(i, num_columns)
            col = num_columns - 1 - col  # Inverse l'ordre des colonnes
            self.ui.gridLayoutGlass.addWidget(bottle_param, row, col)


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
            self.accept()  # Fermer la boîte de dialogue après la mise à jour
