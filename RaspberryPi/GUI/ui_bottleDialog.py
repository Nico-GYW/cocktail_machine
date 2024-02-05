# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottleDialog.ui'
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

class Ui_bottleDialog(object):
    def setupUi(self, bottleDialog):
        if not bottleDialog.objectName():
            bottleDialog.setObjectName(u"bottleDialog")
        bottleDialog.resize(350, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bottleDialog.sizePolicy().hasHeightForWidth())
        bottleDialog.setSizePolicy(sizePolicy)
        bottleDialog.setMinimumSize(QSize(350, 200))
        bottleDialog.setMaximumSize(QSize(350, 200))
        bottleDialog.setStyleSheet(u"background-color: #FFFFFF;\n"
"font-family: \"CoconPro\";\n"
"color: black;\n"
"font-size: 12pt;\n"
"")
        self.buttonBox = QDialogButtonBox(bottleDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 140, 241, 51))
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
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.bottleComboBox = QComboBox(bottleDialog)
        self.bottleComboBox.setObjectName(u"bottleComboBox")
        self.bottleComboBox.setGeometry(QRect(150, 60, 150, 30))
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
        self.title = QLabel(bottleDialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(110, 20, 121, 21))
        self.title.setStyleSheet(u"font-size: 20px;")
        self.title.setAlignment(Qt.AlignCenter)
        self.label = QLabel(bottleDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 58, 16))
        self.label_2 = QLabel(bottleDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 58, 16))
        self.quantitySpinBox = QSpinBox(bottleDialog)
        self.quantitySpinBox.setObjectName(u"quantitySpinBox")
        self.quantitySpinBox.setGeometry(QRect(150, 100, 150, 30))
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
        self.quantitySpinBox.setMaximum(1000)
        self.quantitySpinBox.setSingleStep(50)
        self.quantitySpinBox.setValue(750)
        self.quantitySpinBox.setDisplayIntegerBase(10)

        self.retranslateUi(bottleDialog)
        self.buttonBox.accepted.connect(bottleDialog.accept)
        self.buttonBox.rejected.connect(bottleDialog.reject)

        QMetaObject.connectSlotsByName(bottleDialog)
    # setupUi

    def retranslateUi(self, bottleDialog):
        bottleDialog.setWindowTitle(QCoreApplication.translate("bottleDialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("bottleDialog", u"Bottle Name", None))
        self.label.setText(QCoreApplication.translate("bottleDialog", u"Contenu", None))
        self.label_2.setText(QCoreApplication.translate("bottleDialog", u"Quantit\u00e9", None))
    # retranslateUi

