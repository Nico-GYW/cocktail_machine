# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cocktailCard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_cocktailCard(object):
    def setupUi(self, cocktailCard):
        if not cocktailCard.objectName():
            cocktailCard.setObjectName(u"cocktailCard")
        cocktailCard.resize(130, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cocktailCard.sizePolicy().hasHeightForWidth())
        cocktailCard.setSizePolicy(sizePolicy)
        cocktailCard.setMinimumSize(QSize(130, 130))
        cocktailCard.setMaximumSize(QSize(130, 130))
        cocktailCard.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */")
        self.cocktailCardImage = QLabel(cocktailCard)
        self.cocktailCardImage.setObjectName(u"cocktailCardImage")
        self.cocktailCardImage.setEnabled(True)
        self.cocktailCardImage.setGeometry(QRect(40, 10, 51, 71))
        font = QFont()
        font.setFamilies([u"CoconPro"])
        self.cocktailCardImage.setFont(font)
        self.cocktailCardImage.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.cocktailCardImage.setPixmap(QPixmap(u"ressources/cocktail/spritz.png"))
        self.cocktailCardImage.setScaledContents(True)
        self.cocktailCardImage.setAlignment(Qt.AlignCenter)
        self.cocktailCardName = QLabel(cocktailCard)
        self.cocktailCardName.setObjectName(u"cocktailCardName")
        self.cocktailCardName.setEnabled(True)
        self.cocktailCardName.setGeometry(QRect(20, 100, 91, 21))
        self.cocktailCardName.setFont(font)
        self.cocktailCardName.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.cocktailCardName.setAlignment(Qt.AlignCenter)

        self.retranslateUi(cocktailCard)

        QMetaObject.connectSlotsByName(cocktailCard)
    # setupUi

    def retranslateUi(self, cocktailCard):
        cocktailCard.setWindowTitle(QCoreApplication.translate("cocktailCard", u"Frame", None))
        self.cocktailCardImage.setText("")
        self.cocktailCardName.setText(QCoreApplication.translate("cocktailCard", u"Mojito", None))
    # retranslateUi

