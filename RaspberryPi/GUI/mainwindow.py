# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase, QFont

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside6-uic cocktailCard.ui -o ui_cocktailCard.py
#     pyside6-uic bottleParameter.ui -o ui_bottleParameter.py
#     pyside6-uic bottleDialog.ui -o ui_bottleDialog.py
#     pyside6-uic dispenserControl.ui -o ui_dispenserControl.py

from ui_form import Ui_MainWindow

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Charger la police
        #fontId = QFontDatabase.addApplicationFont("./ressources/font/CoconPro-Regular Regular.ttf")
        #fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
        #QApplication.setFont(QFont(fontFamilies[0]))
        
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.mainPage.setup(self.ui)
        self.ui.extraPage.setup(self.ui)
        self.ui.parameterPage.setup(self.ui)
        self.ui.barmanPage.setup(self.ui)
        self.ui.processPage.setup(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())