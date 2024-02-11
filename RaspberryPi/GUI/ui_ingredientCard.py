# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingredientCard.ui'
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
    QVBoxLayout, QWidget)

class Ui_ingredientCard(object):
    def setupUi(self, ingredientCard):
        if not ingredientCard.objectName():
            ingredientCard.setObjectName(u"ingredientCard")
        ingredientCard.resize(100, 40)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ingredientCard.sizePolicy().hasHeightForWidth())
        ingredientCard.setSizePolicy(sizePolicy)
        ingredientCard.setMinimumSize(QSize(100, 40))
        ingredientCard.setMaximumSize(QSize(100, 40))
        ingredientCard.setStyleSheet(u"font-family: \"CoconPro\";\n"
"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: white;\n"
"\n"
"")
        self.layoutWidget_8 = QWidget(ingredientCard)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 0, 81, 41))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bottle = QLabel(self.layoutWidget_8)
        self.bottle.setObjectName(u"bottle")
        self.bottle.setStyleSheet(u"font-size: 10px;\n"
"background-color: transparent;")
        self.bottle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.bottle)

        self.quantity = QLabel(self.layoutWidget_8)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setStyleSheet(u"font-size: 10px;\n"
"background-color: transparent;")
        self.quantity.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.quantity)


        self.retranslateUi(ingredientCard)

        QMetaObject.connectSlotsByName(ingredientCard)
    # setupUi

    def retranslateUi(self, ingredientCard):
        ingredientCard.setWindowTitle(QCoreApplication.translate("ingredientCard", u"Frame", None))
        self.bottle.setText(QCoreApplication.translate("ingredientCard", u"Schweppes", None))
        self.quantity.setText(QCoreApplication.translate("ingredientCard", u"100 ml", None))
    # retranslateUi

