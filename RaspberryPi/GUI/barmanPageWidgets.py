from PySide6.QtWidgets import QWidget, QFrame, QLabel, QSpacerItem, QDialogButtonBox, QVBoxLayout, QWidget, QSizePolicy, QDialog
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt, QTimer

from copy import deepcopy

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_ingredientCard import Ui_ingredientCard
from ui_ingredientCardDialog import Ui_ingredientCardDialog

from pompetteUtils import  PompetteMessageBox

from mainPageWidgets import machine

class BarmanPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cocktailRecipe = None

    def setup(self, ui):
        self.ui = ui
        self.set_cocktail_recipe(machine.get_recipes()[0]) 
        self.ui.toolButtonBarManPage.clicked.connect(lambda: self.changeParameterPage(1))

    def set_cocktail_recipe(self, cocktailRecipe):
        self.cocktailRecipe = deepcopy(cocktailRecipe)

        self.ui.barmanCocktailName.setText(cocktailRecipe.name)
        self.ui.barmanImage.setPixmap(QPixmap(cocktailRecipe.image))
        total_quantity = self.cocktailRecipe.total_liquid_quantity()
        alc_percentage = self.cocktailRecipe.alcohol_percentage()
        self.ui.barmanQuantity.setText(f"{total_quantity} ml")
        self.ui.barmanAlc.setText(f"{alc_percentage:.2f} %")

        # Nettoyer les layouts avant d'ajouter de nouveaux ingrédients
        self.clear_ingredients(self.ui.verticalLayoutGlassBottleBarMan)
        self.clear_ingredients(self.ui.verticalLayoutSoftBottleBarMan)

        # Ajouter les cartes d'ingrédient pour les bouteilles en verre
        for bottle_name, quantity in self.cocktailRecipe.glass_bottles.items():
            card = IngredientCard(True, bottle_name, quantity, self.cocktailRecipe, self.ui.verticalLayoutGlassBottleBarMan)
            self.ui.verticalLayoutGlassBottleBarMan.addWidget(card)

        self.ui.verticalLayoutGlassBottleBarMan.addWidget(IngredientSpacer(True, self.cocktailRecipe, self.ui.verticalLayoutGlassBottleBarMan))

        # Ajouter les cartes d'ingrédient pour les softs
        for bottle_name, quantity in self.cocktailRecipe.soft_drink_bottles.items():
            card = IngredientCard(False, bottle_name, quantity, self.cocktailRecipe, self.ui.verticalLayoutSoftBottleBarMan)
            self.ui.verticalLayoutSoftBottleBarMan.addWidget(card)

        self.ui.verticalLayoutSoftBottleBarMan.addWidget(IngredientSpacer(False, self.cocktailRecipe, self.ui.verticalLayoutSoftBottleBarMan))

        
    def clear_ingredients(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def changeParameterPage(self, pageIndex):
        stacked_widget = self.ui.parameterStack
        stacked_widget.setCurrentIndex(pageIndex)

class IngredientCard(QFrame):
    def __init__(self, is_glass, bottle_name, quantity, cocktailRecipe, layoutParent, parent=None):
        super().__init__(parent)
        self.ui = Ui_ingredientCard()
        self.ui.setupUi(self)
        self.is_new_ingredient = False
        self.is_glass = is_glass
        self.bottle_name = bottle_name
        self.quantity = quantity
        self.cocktailRecipe = cocktailRecipe
        self.layoutParent = layoutParent
        self.set_name()
        
    def set_name(self):
        self.ui.bottle.setText(self.bottle_name)
        self.ui.quantity.setText(f"{self.quantity} ml")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet(self.styleSheet() + "background-color: #EAEAEA;")
            self.dialog = IngredientCardDialog(self)
            self.dialog.accepted.connect(self.apply_changes)
            self.dialog.rejected.connect(self.delete_card)
            self.dialog.exec_()

    def apply_changes(self):
        # Récupérer les valeurs depuis le dialogue
        new_bottle_name = self.dialog.ui.bottleComboBox.currentText()
        new_quantity = self.dialog.ui.quantitySpinBox.value()

        # Vérifier si le nom de la nouvelle bouteille est différent de l'actuel
        name_changed = self.bottle_name != new_bottle_name

        # Vérifier si la nouvelle bouteille est déjà présente dans la recette correspondante (verre ou soft)
        bottle_exists_in_recipe = (self.is_glass and new_bottle_name in self.cocktailRecipe.glass_bottles) or \
                                (not self.is_glass and new_bottle_name in self.cocktailRecipe.soft_drink_bottles)

        # Condition complète combinée
        if name_changed and bottle_exists_in_recipe:
            msg = PompetteMessageBox("T'as trop bu ? L'ingrédient est déjà dans le cocktail, choisis un autre")
            msg.exec_()
        else:
            # Appliquer les changements
            if self.cocktailRecipe:
                self.cocktailRecipe.replace_bottle(self.ui.bottle.text(), new_bottle_name, new_quantity, self.is_glass)
            self.bottle_name = new_bottle_name
            self.quantity = new_quantity
            self.set_name()
            print(self.cocktailRecipe.to_dict())

        self.setStyleSheet(self.styleSheet() + "background-color: #FFF;")

    def delete_card(self):
        # Retirer le widget du layout
        item = self.layoutParent.takeAt(self.layoutParent.indexOf(self))
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                self.cocktailRecipe.remove_bottle(self.bottle_name)
                print(self.cocktailRecipe.to_dict())

class NewIngredientCard(QLabel):

    def __init__(self, is_glass, cocktailRecipe, layoutParent, parent=None):
        super().__init__(parent)
        self.is_glass = is_glass
        self.cocktailRecipe = cocktailRecipe
        self.layoutParent = layoutParent
        self.is_new_ingredient = True  # Toujours False comme spécifié

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dialog = IngredientCardDialog(self)
            self.dialog.accepted.connect(self.create_new_ingredient)
            self.dialog.exec_()

    def create_new_ingredient(self):
        # Vérifier le nombre de composants dans le layout
        if self.layoutParent.count() >= 5:
            # Afficher un message d'erreur si le layout a déjà 5 composants
            if self.is_glass:
                msg = PompetteMessageBox("Tu vas être trop saoul, arrête avec l'alcool")
            else:
                msg = PompetteMessageBox("Il y a trop de soft ici, arrête un peu")
            msg.exec_()
        else:
            new_bottle_name = self.dialog.ui.bottleComboBox.currentText()
            new_quantity = self.dialog.ui.quantitySpinBox.value()

            # Vérifier si l'ingrédient est déjà dans la recette
            if self.is_glass and new_bottle_name in self.cocktailRecipe.glass_bottles or \
               not self.is_glass and new_bottle_name in self.cocktailRecipe.soft_drink_bottles:
                msg = PompetteMessageBox("T'as trop bu ? L'ingrédient est déjà dans le cocktail, choisis un autre")
                msg.exec_()
            else:
                new_ingredient_card = IngredientCard(self.is_glass, new_bottle_name, new_quantity, self.cocktailRecipe, self.layoutParent, self.parent())
                self.cocktailRecipe.add_bottle(new_bottle_name, new_quantity, self.is_glass)
                print(self.cocktailRecipe.to_dict())
                # Ajouter le nouvel IngredientCard à l'avant-dernière position du layout
                self.layoutParent.insertWidget(self.layoutParent.count() - 1, new_ingredient_card)
        
class IngredientSpacer(QWidget):
    def __init__(self, is_glass, cocktailRecipe, layoutParent, parent=None):
        super().__init__(parent)
        self.setObjectName("ingredientSpacer")
        
        # Création et configuration du QVBoxLayout
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Création et configuration du QLabel
        self.label = NewIngredientCard(is_glass, cocktailRecipe, layoutParent, self)
        self.label.setObjectName("label")
        
        # Configuration de la politique de taille pour le label
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        
        # Ajout de l'icône au label
        self.label.setPixmap(QPixmap("ressources/generic/plus.svg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Ajout du label au layout
        self.verticalLayout.addWidget(self.label)

        # Ajout du Spacer
        verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(verticalSpacer_4)

class IngredientCardDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ingredientCardDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.is_glass = parent.is_glass
        self.is_new_ingredient = parent.is_new_ingredient

        # Remplir le QComboBox avec les noms de bouteilles
        bottle_list = machine.get_bottle_list(self.is_glass)  # Assume 'machine' est accessible depuis le parent
        self.ui.bottleComboBox.addItems(bottle_list)
       
        if self.is_new_ingredient:
            self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Annuler")
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Supprimer")
            # Pour régler la valeur actuelle du QComboBox sur bottle_name s'il est dans la liste
            bottle_name_index = self.ui.bottleComboBox.findText(self.parent.bottle_name)
            if bottle_name_index != -1:  # -1 signifie que le texte n'a pas été trouvé
                self.ui.bottleComboBox.setCurrentIndex(bottle_name_index)

            # Pour régler la valeur par défaut du QSpinBox sur quantity
            self.ui.quantitySpinBox.setValue(self.parent.quantity)

        # Connecter les boutons  
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)