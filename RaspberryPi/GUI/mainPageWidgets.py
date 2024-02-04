from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Signal

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))

from ui_cocktailCard import Ui_cocktailCard
from cocktailMachine import CocktailMachine

machine = CocktailMachine()
machine.load_state()

class MainPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        self.ui = ui
        ui.toolButtonMainPage.clicked.connect(lambda: self.changePage(2))
        self.ui.rightButtonMainPage.clicked.connect(self.incrementerPage)
        self.ui.leftButtonMainPage.clicked.connect(self.decrementerPage)

        self.populate_cocktail_carousel()
        self.mettreAJourTextePage()

    def populate_cocktail_carousel(self):
        # self.ui.cocktailCarousel.clear()
        cocktail_recipes = machine.get_recipes()
        cocktails_per_page = 6
        num_pages = (len(cocktail_recipes) + cocktails_per_page - 1) // cocktails_per_page

        # Supprime les deux premières pages du CocktailCarousel
        for _ in range(2):  # Répète l'opération deux fois
            widgetToRemove = self.ui.cocktailCarousel.widget(0)  # Obtient le widget actuellement au début
            if widgetToRemove:  # Vérifie si widgetToRemove n'est pas None
                self.ui.cocktailCarousel.removeWidget(widgetToRemove)
                widgetToRemove.deleteLater()  # Supprime le widget de manière sûre

        for page_index in range(num_pages):
            page = QFrame(self.ui.cocktailCarousel)  # Créez une nouvelle page
            layout = QGridLayout()  # Créez un QGridLayout pour la page
            page.setLayout(layout)

            start_index = page_index * cocktails_per_page
            end_index = start_index + cocktails_per_page
            page_recipes = cocktail_recipes[start_index:end_index]

            num_columns = 3  # Nombre total de colonnes dans le gridLayout
            # Ajoutez les cartes de cocktails et notez le dernier index utilisé
            last_card_index = -1
            for i, recipe in enumerate(page_recipes):
                card = CocktailCard(page, self.ui)
                card.set_cocktail_data(recipe.get_name(), recipe.get_image())
                # Calcul pour un remplissage de droite à gauche
                row, col = divmod(i, num_columns)
                col = num_columns - 1 - col  # Inverse l'ordre des colonnes
                layout.addWidget(card, row, col)
                last_card_index = i

            # Ajoutez des widgets vides pour combler les espaces restants, si nécessaire
            if page_index == num_pages - 1:
                for j in range(last_card_index + 1, cocktails_per_page):
                    placeholder = QWidget(page)
                    placeholder.setFixedSize(130, 130)
                    # Même calcul pour les placeholders pour maintenir l'ordre de droite à gauche
                    row, col = divmod(j, num_columns)
                    col = num_columns - 1 - col
                    layout.addWidget(placeholder, row, col)

            self.ui.cocktailCarousel.addWidget(page)


    def changePage(self, pageIndex):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(pageIndex)

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
        self.mainWindow_ui = mainWindow  # Référence à la MainWindow

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
