from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal as Signal

from copy import deepcopy
import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_cocktailCard import Ui_cocktailCard
from pompetteUtils import PompetteMessageBox
from cocktailMachine import CocktailMachine
from cocktailRecipe import CocktailRecipe

machine = CocktailMachine()
machine.load_state()

class MainPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        self.ui = ui
        self.current_recipe = None
        ui.toolButtonMainPage.clicked.connect(lambda: self.changePage(2))
        self.ui.rightButtonMainPage.clicked.connect(self.incrementerPage)
        self.ui.leftButtonMainPage.clicked.connect(self.decrementerPage)
        self.ui.modifyButton.clicked.connect(self.changeBarmanPage)
        self.ui.extraButton.clicked.connect(self.changeExtraPage)
        self.ui.makeButton.clicked.connect(self.changeProcessPage)

        self.populate_cocktail_carousel()
        self.mettreAJourTextePage()


    def populate_cocktail_carousel(self):
        cocktail_recipes = machine.get_recipes()
        cocktails_per_page = 6  # Nombre total de cartes par page
        num_pages = (len(cocktail_recipes) + 1 + cocktails_per_page - 1) // cocktails_per_page  # +1 pour la carte de création
        self.current_recipe = cocktail_recipes[0]
        
        for _ in range(2):
            widgetToRemove = self.ui.cocktailCarousel.widget(0)
            if widgetToRemove:
                self.ui.cocktailCarousel.removeWidget(widgetToRemove)
                widgetToRemove.deleteLater()

        for page_index in range(num_pages):
            page = QFrame(self.ui.cocktailCarousel)
            layout = QGridLayout()
            page.setLayout(layout)

            start_index = page_index * cocktails_per_page
            end_index = min(start_index + cocktails_per_page, len(cocktail_recipes))
            page_recipes = cocktail_recipes[start_index:end_index]

            num_columns = 3
            total_cards_added = 0  # Compteur pour les cartes ajoutées, y compris la carte spéciale

            # Ajouter les cartes de cocktails normales
            for recipe in page_recipes:
                card = CocktailCard(page, self)
                card.set_cocktail_data(recipe.get_name(), recipe.get_image())
                row, col = divmod(total_cards_added, num_columns)
                layout.addWidget(card, row, col)
                total_cards_added += 1

            # Ajouter la carte spéciale sur la dernière page
            if page_index == num_pages - 1:
                special_card = CocktailCreationCard(page, self, self.changePage)
                special_card.set_cocktail_data("Cocktail Perso", "ressources/generic/plus.png")
                row, col = divmod(total_cards_added, num_columns)
                layout.addWidget(special_card, row, col)
                total_cards_added += 1

            # Compléter avec des widgets vides si nécessaire pour maintenir la structure 3x2
            remaining_slots = cocktails_per_page - total_cards_added
            for _ in range(remaining_slots):
                placeholder = QWidget(page)
                placeholder.setFixedSize(130, 130)
                row, col = divmod(total_cards_added, num_columns)
                layout.addWidget(placeholder, row, col)
                total_cards_added += 1

            self.ui.cocktailCarousel.addWidget(page)

    def changePage(self, pageIndex):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(pageIndex)
    
    def changeBarmanPage(self):
        if self.current_recipe.save:
            self.ui.barmanPage.set_cocktail_recipe(deepcopy(self.current_recipe))
            self.ui.barmanPage.set_cocktail_mode(is_new_cocktail=True)
        else:
            self.ui.barmanPage.set_cocktail_recipe(self.current_recipe)
            self.ui.barmanPage.set_cocktail_mode(is_new_cocktail=False)
        self.changePage(3)

    def changeExtraPage(self):
        self.ui.mainPageStacked.setCurrentIndex(1)
        self.ui.extraStack.setCurrentIndex(0)
        self.current_recipe = deepcopy(self.current_recipe)
        self.ui.extraPage.set_current_recipe(self.current_recipe)
        self.ui.extraPage.reset_all_extras()

    def changeProcessPage(self):
        missing_ingredients = self.machine.check_ingredients(self.current_recipe)
        
        if not missing_ingredients:
            # Si tous les ingrédients sont présents, continuer le processus
            self.ui.processingStackedWidget.setCurrentIndex(0)
            self.ui.processPage.setRecipe(self.current_recipe)
            self.changePage(4)
        else:
            # Si des ingrédients manquent, afficher un message d'erreur
            missing_ingredients_list = '\n'.join([f"{ingredient} (quantité manquante : {quantity})" for ingredient, quantity in missing_ingredients])
            message = f"Il manque les ingrédients suivants pour que Pompette te régale :\n{missing_ingredients_list}"
            
            errorMessageBox = PompetteMessageBox(message, self)
            errorMessageBox.exec_()

    def mettreAJourTextePage(self):
        index_courant = self.ui.cocktailCarousel.currentIndex() + 1  # +1 car l'index commence à 0
        nombre_total_pages = self.ui.cocktailCarousel.count()
        texte = f"Page {index_courant}/{nombre_total_pages}"
        self.ui.pageCount.setText(texte)

    def incrementerPage(self):
        index_courant = self.ui.cocktailCarousel.currentIndex()
        nombre_total_pages = self.ui.cocktailCarousel.count()

        # Incrémenter l'index ou revenir à la première page
        nouvel_index = (index_courant + 1) % nombre_total_pages
        self.ui.cocktailCarousel.setCurrentIndex(nouvel_index)
        self.mettreAJourTextePage()

    def decrementerPage(self):
        index_courant = self.ui.cocktailCarousel.currentIndex()
        nombre_total_pages = self.ui.cocktailCarousel.count()

        # Décrémenter l'index ou aller à la dernière page si à la première page
        nouvel_index = (index_courant - 1 + nombre_total_pages) % nombre_total_pages
        self.ui.cocktailCarousel.setCurrentIndex(nouvel_index)
        self.mettreAJourTextePage()

class CocktailCard(QFrame):
    # Signal qui envoie le nom du cocktail lorsqu'une carte est cliquée
    clicked = Signal(str)

    def __init__(self, parent=None, mainWindow=None):
        super(CocktailCard, self).__init__(parent)
        self.ui = Ui_cocktailCard()  # Assurez-vous que cette UI est correctement définie quelque part
        self.ui.setupUi(self)
        if mainWindow is not None:
            self.mainWindow = mainWindow
            self.mainWindow_ui = mainWindow.ui  # Référence à la MainWindow
                
    def set_cocktail_data(self, name, image_path):
        self.ui.cocktailCardName.setText(name)
        self.ui.cocktailCardImage.setPixmap(QPixmap(image_path))
        self.cocktailName = name
        self.imagePath = image_path

    def mousePressEvent(self, event):
        # Émettre le signal clicked avec le nom du cocktail
        self.clicked.emit(self.cocktailName)
        # Mettre à jour l'UI de la MainWindow
        self.update_main_window_ui()

        super(CocktailCard, self).mousePressEvent(event)

    def update_main_window_ui(self):
        # Récupérer la recette par son nom
        recipe = machine.get_recipe_by_name(self.cocktailName)
        self.mainWindow.current_recipe = recipe
        if recipe:
            # Mettre à jour les éléments de l'UI de la MainWindow
            self.mainWindow_ui.cocktailImage.setPixmap(QPixmap(self.imagePath))
            self.mainWindow_ui.cocktailName.setText(self.cocktailName)
            # Préparation de la chaîne de caractères pour les ingrédients
            ingredients_list = []
            for bottle_type, bottles in [('glass_bottles', recipe.glass_bottles), ('soft_drink_bottles', recipe.soft_drink_bottles)]:
                for name, amount in bottles.items():
                    ingredients_list.append(f"{name} - {amount} ml")

            # Ajouter le citron s'il y en a
            if recipe.lemon > 0:
                ingredients_list.append(f"Lemon - {recipe.lemon} slice(s)")

            # Ajouter de la glace si elle est présente
            if recipe.ice > 0:
                ingredients_list.append("Ice")

            # Mettre à jour le QLabel avec les ingrédients
            self.mainWindow_ui.cocktailReceipe.setText('\n'.join(ingredients_list))

class CocktailCreationCard(CocktailCard):
    def __init__(self, parent, mainPage, changePageFunc):
        super().__init__(parent, mainPage)
        self.changePageFunc = changePageFunc
        self.setRecipeFunc = mainPage.ui.barmanPage.set_cocktail_recipe
        self.set_cocktail_mode = mainPage.ui.barmanPage.set_cocktail_mode
        self.clicked.connect(self.onChangePage)

    def onChangePage(self):
        self.set_cocktail_mode(is_new_cocktail=True)
        self.setRecipeFunc(CocktailRecipe(name="Mon Cocktail"))  # Mise à jour de la recette avant de changer de page
        self.changePageFunc(3)
