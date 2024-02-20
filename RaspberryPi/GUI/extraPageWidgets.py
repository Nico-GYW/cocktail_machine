from PyQt5.QtWidgets import QFrame, QPushButton, QGridLayout, QDialog, QComboBox, QColorDialog, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_extraBottle import Ui_extraBottle

from pompetteUtils import  clear_grid_layout
from mainPageWidgets import machine

class extraPage(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        self.ui = ui
        self.ui.extraCloseButton.clicked.connect(self.changeCocktailPage)
        self.set_extra_button_layout()
        self.set_extra_glass_bottle()
        self.set_extra_soft_bottle()

    def changeCocktailPage(self):
        self.ui.mainPageStacked.setCurrentIndex(0)

    def changeExtraPage(self, index):
        self.ui.extraStack.setCurrentIndex(index)
        print("Button pressed " + str(index))

    def set_extra_button_layout(self):
        buttons = [self.ui.extraGlassButton, self.ui.extraSoftButton, self.ui.extraLemonButton, self.ui.extraIceButton]
        for index, button in enumerate(buttons):
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            # Utiliser une lambda pour capturer la valeur courante de 'index'
        
        self.ui.extraGlassButton.clicked.connect(lambda: self.changeExtraPage(1))
        self.ui.extraSoftButton.clicked.connect(lambda: self.changeExtraPage(2))

    def set_extra_glass_bottle(self):
        clear_grid_layout(self.ui.extraGlassBottleGrid)
        
        glass_bottles = machine.get_glass_bottles()  # Obtenir la liste des bouteilles depuis la machine à cocktail
        for i, bottle in enumerate(glass_bottles[:8]):  # Limite à 8 bouteilles
            # Créer une instance de ExtraBottle avec le nom de la bouteille
            bottle_widget = ExtraBottle(bottle.name)
            
            # Calcul pour un remplissage en 2x4
            row = i // 4  # Calculer la ligne
            col = i % 4   # Calculer la colonne
            self.ui.extraGlassBottleGrid.addWidget(bottle_widget, row, col)

        self.ui.extraGlassBottleButton.clicked.connect(lambda: self.changeExtraPage(0))

    def set_extra_soft_bottle(self):
        clear_grid_layout(self.ui.extraSoftBottleGrid)
        
        soft_bottles = machine.get_soft_bottles()
        num_columns = 2  # Pour un layout de 2x2
        
        for i, bottle in enumerate(soft_bottles[:4]):  # Limite à 4 bouteilles pour correspondre à un layout 2x2
            # Créer une instance de ExtraBottle avec le nom de la bouteille
            bottle_widget = ExtraBottle(bottle.name)
            
            # Calculer la position dans le grid
            row = i // num_columns
            col = i % num_columns
            self.ui.extraSoftBottleGrid.addWidget(bottle_widget, row, col)

        self.ui.extraSoftBottleButton.clicked.connect(lambda: self.changeExtraPage(0))        

class ExtraBottle(QFrame):
    def __init__(self, title, parent=None):
        super(ExtraBottle, self).__init__(parent)
        self.ui = Ui_extraBottle()
        self.ui.setupUi(self)

        # Set title
        self.ui.titleLabel.setText(title)

        # Initialize lineEdit with 0 ml
        self.ui.lineEdit.setText("0 ml")

        # Connect push buttons to their respective slots
        self.ui.pushButtonLeft.clicked.connect(lambda: self.update_value(-5))
        self.ui.pushButtonRight.clicked.connect(lambda: self.update_value(5))

    def update_value(self, change):
        # Extract the current numeric value from lineEdit
        current_value = int(self.ui.lineEdit.text().split()[0])  # Split and take the first part to ignore "ml"
        new_value = current_value + change

        # Ensure new_value is within 0 and 50
        new_value = max(0, min(50, new_value))

        # Update lineEdit with the new value and append "ml"
        self.ui.lineEdit.setText(f"{new_value} ml")
