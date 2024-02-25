from PyQt5.QtWidgets import QFrame, QPushButton, QGridLayout, QDialog, QComboBox, QColorDialog, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer, pyqtSignal


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
        self.current_recipe = None
        self.ui.extraCloseButton.clicked.connect(self.changeCocktailPage)
        self.set_extra_button_layout()
        self.set_extra_glass_bottle()
        self.set_extra_soft_bottle()

    def changeCocktailPage(self):
        self.ui.mainPageStacked.setCurrentIndex(0)

    def set_current_recipe(self, recipe):
        self.current_recipe = recipe

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
        
        glass_bottles = machine.get_glass_bottles()
        for i, bottle in enumerate(glass_bottles[:8]):
            bottle_widget = ExtraBottle(bottle.name, is_glass=True)
            bottle_widget.extraSelected.connect(self.add_extra_to_recipe)
            row = i // 4
            col = i % 4
            self.ui.extraGlassBottleGrid.addWidget(bottle_widget, row, col)

        self.ui.extraGlassBottleButton.clicked.connect(lambda: self.changeExtraPage(0))

    def set_extra_soft_bottle(self):
        clear_grid_layout(self.ui.extraSoftBottleGrid)
        
        soft_bottles = machine.get_soft_bottles()
        for i, bottle in enumerate(soft_bottles[:4]):
            bottle_widget = ExtraBottle(bottle.name, is_glass=False)
            bottle_widget.extraSelected.connect(self.add_extra_to_recipe)
            row = i // 2
            col = i % 2
            self.ui.extraSoftBottleGrid.addWidget(bottle_widget, row, col)

        self.ui.extraSoftBottleButton.clicked.connect(lambda: self.changeExtraPage(0))

    def add_extra_to_recipe(self, bottle_name, change, is_glass):
        if change != 0:  # Ajoute seulement si le changement n'est pas nul
            recipe = self.current_recipe
            
            if change > 0:
                recipe.add_bottle(bottle_name, change, is_glass)
            else:
                # Si la quantité après le changement est zéro ou négative, supprimez la bouteille de la recette.
                # Note: Cette logique suppose que `add_bottle` réduit la quantité si `change` est négatif.
                current_quantity = recipe.glass_bottles[bottle_name] if is_glass else recipe.soft_drink_bottles[bottle_name]
                new_quantity = current_quantity + change
                if new_quantity <= 0:
                    recipe.remove_bottle(bottle_name, is_glass)
                else:
                    recipe.add_bottle(bottle_name, change, is_glass)
                    
            self.update_recipe_display(recipe)

    def update_recipe_display(self, recipe):
        ingredients_list = []
        for bottle_type, bottles in [('glass_bottles', recipe.glass_bottles), ('soft_drink_bottles', recipe.soft_drink_bottles)]:
            for name, amount in bottles.items():
                ingredients_list.append(f"{name} - {amount} ml")
        if recipe.lemon > 0:
            ingredients_list.append(f"Lemon - {recipe.lemon} slice(s)")
        if recipe.ice > 0:
            ingredients_list.append("Ice")
        self.ui.cocktailReceipe.setText('\n'.join(ingredients_list))

    def reset_all_extras(self):
        # Réinitialiser tous les ExtraBottle dans extraGlassBottleGrid
        for i in range(self.ui.extraGlassBottleGrid.count()): 
            widget = self.ui.extraGlassBottleGrid.itemAt(i).widget()
            if isinstance(widget, ExtraBottle):
                widget.reset()
        
        # Réinitialiser tous les ExtraBottle dans extraSoftBottleGrid
        for i in range(self.ui.extraSoftBottleGrid.count()): 
            widget = self.ui.extraSoftBottleGrid.itemAt(i).widget()
            if isinstance(widget, ExtraBottle):
                widget.reset()


class ExtraBottle(QFrame):
    extraSelected = pyqtSignal(str, int, bool)
    
    def __init__(self, title, is_glass=True, parent=None):
        super(ExtraBottle, self).__init__(parent)
        self.ui = Ui_extraBottle()  # Assurez-vous que cette classe UI est bien définie
        self.ui.setupUi(self)
        self.title = title
        self.is_glass = is_glass
        self.last_value = 0  # Initialisez la dernière valeur à 0

        self.ui.titleLabel.setText(title)
        self.ui.lineEdit.setText("0 ml")

        self.ui.pushButtonLeft.clicked.connect(lambda: self.update_value(-5))
        self.ui.pushButtonRight.clicked.connect(lambda: self.update_value(5))

    def update_value(self, change):
        current_value = int(self.ui.lineEdit.text().split()[0])
        new_value = max(0, min(50, current_value + change))
        self.ui.lineEdit.setText(f"{new_value} ml")
        
        # Calculez le changement par rapport à la dernière valeur
        change_since_last = new_value - self.last_value
        self.last_value = new_value  # Mettez à jour la dernière valeur
        
        # Émettez le signal avec le nom de la bouteille, le changement et si c'est une bouteille en verre
        self.extraSelected.emit(self.title, change_since_last, self.is_glass)

    def reset(self):
        self.ui.lineEdit.setText("0 ml")
        self.last_value = 0
        # Émettre le signal avec un changement de 0 pour réinitialiser la quantité sans affecter la recette
        self.extraSelected.emit(self.title, 0, self.is_glass)