# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dispenserControl.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_dispenserControl(object):
    def setupUi(self, dispenserControl):
        if not dispenserControl.objectName():
            dispenserControl.setObjectName(u"dispenserControl")
        dispenserControl.resize(100, 110)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dispenserControl.sizePolicy().hasHeightForWidth())
        dispenserControl.setSizePolicy(sizePolicy)
        dispenserControl.setMinimumSize(QSize(100, 100))
        dispenserControl.setStyleSheet(u"font-family: \"CoconPro\";")
        self.titleLabel = QLabel(dispenserControl)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QSize(80, 30))
        self.titleLabel.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(dispenserControl)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 60, 41, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 20px;\n"
"	background-color: #F79643;\n"
"	border: 5px solid #707070; /* Bordure de 1px en noir */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFBC50; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")

        self.retranslateUi(dispenserControl)

        QMetaObject.connectSlotsByName(dispenserControl)
    # setupUi

    def retranslateUi(self, dispenserControl):
        dispenserControl.setWindowTitle(QCoreApplication.translate("dispenserControl", u"Frame", None))
        self.titleLabel.setText(QCoreApplication.translate("dispenserControl", u"Bouteille 1", None))
        self.pushButton.setText("")
    # retranslateUi

