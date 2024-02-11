# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingredientCardDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QSpinBox,
    QWidget)

class Ui_ingredientCardDialog(object):
    def setupUi(self, ingredientCardDialog):
        if not ingredientCardDialog.objectName():
            ingredientCardDialog.setObjectName(u"ingredientCardDialog")
        ingredientCardDialog.resize(443, 93)
        ingredientCardDialog.setStyleSheet(u"font-family: \"CoconPro\";\n"
"background-color: #F9F8F8;\n"
"border-radius: 15px;")
        self.label = QLabel(ingredientCardDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 58, 16))
        self.label.setStyleSheet(u"font-family: \"CoconPro\";\n"
"background-color: #F9F8F8;\n"
"border-radius: 15px;")
        self.bottleComboBox = QComboBox(ingredientCardDialog)
        self.bottleComboBox.setObjectName(u"bottleComboBox")
        self.bottleComboBox.setGeometry(QRect(30, 50, 141, 30))
        self.bottleComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #F9F8F8; /* Fond gris clair */\n"
"    color: #000000; /* Texte noir */\n"
"    font-size: 12px; /* Taille de la police 12 */\n"
"    border: 1px solid #707070; /* Bordure de 1px en noir */\n"
"    border-radius: 3px; /* Coins arrondis de 2px */\n"
"    padding: 2px; /* Espacement interne */\n"
"    selection-background-color: #FFA500; /* Fond d'\u00e9cran de s\u00e9lection orange */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #F79643; /* Couleur de fond de la fl\u00e8che d\u00e9roulante (m\u00eame que le fond) */\n"
"    border: 0px solid #707070; /* Bordure de la fl\u00e8che d\u00e9roulante en noir */\n"
"    width: 20px; /* Largeur de la fl\u00e8che d\u00e9roulante de 20px */\n"
"	margin-right: 0px; /* Marge \u00e0 droite de la fl\u00e8che d\u00e9roulante */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./ressources/generic/arrow_down.svg); /* Chemin relatif vers votre ic\u00f4ne SVG */\n"
"	color: #000000; /* Couleur de la fl\u00e8che en"
                        " noir */\n"
"}\n"
"\n"
"\n"
"")
        self.label_2 = QLabel(ingredientCardDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 20, 58, 16))
        self.label_2.setStyleSheet(u"font-family: \"CoconPro\";\n"
"background-color: #F9F8F8;\n"
"border-radius: 15px;")
        self.quantitySpinBox = QSpinBox(ingredientCardDialog)
        self.quantitySpinBox.setObjectName(u"quantitySpinBox")
        self.quantitySpinBox.setGeometry(QRect(190, 50, 121, 30))
        self.quantitySpinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #F9F8F8; /* Fond gris clair */\n"
"    color: #000000; /* Texte noir */\n"
"    font-size: 12px; /* Taille de la police 12 */\n"
"    border: 1px solid #707070; /* Bordure de 1px en noir */\n"
"    border-radius: 3px; /* Coins arrondis de 3px */\n"
"    padding: 2px; /* Espacement interne */\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #F79643; /* Couleur de fond des boutons d'incr\u00e9mentation/d\u00e9cr\u00e9mentation */\n"
"    width: 20px; /* Largeur des boutons */\n"
"    border: 0px solid #707070; /* Bordure des boutons en noir */\n"
"	margin: 0px; /* Marge des boutons */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QSpinBox::up-arrow{\n"
"    image: url(./ressources/generic/arrow_"
                        "up.svg); /* Chemin relatif vers votre ic\u00f4ne SVG */\n"
"    color: #000000; /* Couleur des fl\u00e8ches en noir */\n"
"}\n"
"QSpinBox::down-arrow {\n"
"    image: url(./ressources/generic/arrow_down.svg); /* Chemin relatif vers votre ic\u00f4ne SVG */\n"
"    color: #000000; /* Couleur des fl\u00e8ches en noir */\n"
"}\n"
"")
        self.quantitySpinBox.setFrame(False)
        self.quantitySpinBox.setMaximum(100)
        self.quantitySpinBox.setSingleStep(5)
        self.quantitySpinBox.setValue(100)
        self.quantitySpinBox.setDisplayIntegerBase(10)
        self.buttonBox = QDialogButtonBox(ingredientCardDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(340, 10, 91, 71))
        self.buttonBox.setStyleSheet(u"/* Style pour tous les boutons QDialogButton */\n"
"QDialogButtonBox {\n"
"    background-color: transparent; /* Fond transparent */\n"
"    border: none; /* Pas de bordure */\n"
"    spacing: 10px; /* Espacement entre les boutons */\n"
"}\n"
"\n"
"/* Style sp\u00e9cifique pour le bouton \"Valider\" */\n"
"QDialogButtonBox QPushButton:enabled {\n"
"    background-color: #F79643; /* Fond orange pour le bouton \"Valider\" */\n"
"    color: #FFFFFF; /* Texte en blanc */\n"
"    border: 1px solid #FFA500; /* Bordure orange */\n"
"    border-radius: 3px; /* Coins arrondis de 3px */\n"
"    padding: 5px 10px; /* Espacement interne */\n"
"    font-size: 12px; /* Taille de la police 12 */\n"
"}\n"
"\n"
"/* Style pour les autres boutons (Annuler, etc.) */\n"
"QDialogButtonBox QPushButton:enabled:hover {\n"
"    background-color: #F79643; /* Fond orange clair au survol */\n"
"    border: 1px solid #F79643; /* Bordure orange clair au survol */\n"
"}\n"
"\n"
"/* Style pour les boutons d\u00e9sactiv\u00e9s */\n"
"QDialogBu"
                        "ttonBox QPushButton:disabled {\n"
"    background-color: transparent; /* Fond transparent pour les boutons d\u00e9sactiv\u00e9s */\n"
"    color: #C0C0C0; /* Texte en gris pour les boutons d\u00e9sactiv\u00e9s */\n"
"    border: 1px solid #C0C0C0; /* Bordure grise pour les boutons d\u00e9sactiv\u00e9s */\n"
"}\n"
"")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.retranslateUi(ingredientCardDialog)

        QMetaObject.connectSlotsByName(ingredientCardDialog)
    # setupUi

    def retranslateUi(self, ingredientCardDialog):
        ingredientCardDialog.setWindowTitle(QCoreApplication.translate("ingredientCardDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ingredientCardDialog", u"Contenu", None))
        self.label_2.setText(QCoreApplication.translate("ingredientCardDialog", u"Quantit\u00e9", None))
    # retranslateUi

