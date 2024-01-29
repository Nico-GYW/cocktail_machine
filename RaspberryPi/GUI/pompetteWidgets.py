from PySide6.QtWidgets import QWidget, QFrame, QGridLayout
from PySide6.QtGui import QPixmap

import sys
import os
sys.path.append(os.path.abspath('../PythonScripts'))


from cocktailCard import Ui_cocktailCard

from cocktailMachine import CocktailMachine

machine = CocktailMachine()
machine.load_state()

class LandingPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(1)


class MainPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        self.ui = ui
        ui.toolButtonMainPage.clicked.connect(lambda: self.changePage(2))
        self.ui.rightButtonMainPage.clicked.connect(self.incrementerPage)
        self.ui.leftButtonMainPage.clicked.connect(self.decrementerPage)
        self.mettreAJourTextePage()

        self.populate_cocktail_carousel()

    def populate_cocktail_carousel(self):
        # self.ui.cocktailCarousel.clear()
        cocktail_recipes = machine.get_recipes()
        cocktails_per_page = 6
        num_pages = (len(cocktail_recipes) + cocktails_per_page - 1) // cocktails_per_page

        for page_index in range(num_pages):
            page = QFrame(self.ui.cocktailCarousel)  # Créez une nouvelle page
            layout = QGridLayout()  # Créez un QGridLayout pour la page
            page.setLayout(layout)

            # Déterminez les recettes pour cette page
            start_index = page_index * cocktails_per_page
            end_index = start_index + cocktails_per_page
            page_recipes = cocktail_recipes[start_index:end_index]

            for i, recipe in enumerate(page_recipes):
                card = CocktailCard(page)  # Créez une nouvelle carte de cocktail
                card.set_cocktail_data(recipe.get_name(), recipe.get_image())
                row, col = divmod(i, 3)  # Ajustez en fonction de la disposition souhaitée
                layout.addWidget(card, row, col)  # Ajoutez la carte au grid layout

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
    def __init__(self, parent=None):
        super(CocktailCard, self).__init__(parent)
        self.ui = Ui_cocktailCard()
        self.ui.setupUi(self)

    def set_cocktail_data(self, name, image_path):
        self.ui.cocktailCardName.setText(name)  # cocktailName doit correspondre au nom du QLabel dans Qt Designer
        self.ui.cocktailCardImage.setPixmap(QPixmap(image_path))


class ParameterPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setup(self, ui):
        ui.toolButtonParameterPage.clicked.connect(lambda: self.changePage(1))

    def changePage(self, pageIndex):
        stacked_widget = self.parent()
        stacked_widget.setCurrentIndex(pageIndex)
