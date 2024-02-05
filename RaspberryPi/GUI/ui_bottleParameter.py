# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottleParameter.ui'
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

class Ui_bottleParameter(object):
    def setupUi(self, bottleParameter):
        if not bottleParameter.objectName():
            bottleParameter.setObjectName(u"bottleParameter")
        bottleParameter.resize(100, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bottleParameter.sizePolicy().hasHeightForWidth())
        bottleParameter.setSizePolicy(sizePolicy)
        bottleParameter.setMinimumSize(QSize(100, 100))
        bottleParameter.setMaximumSize(QSize(100, 100))
        bottleParameter.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF; /* Par exemple, fond blanc par d\u00e9faut */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:pressed {\n"
"    background-color: #EAEAEA; /* Fond gris clair lorsque le QFrame est appuy\u00e9 */\n"
"}")
        self.verticalLayout = QVBoxLayout(bottleParameter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(bottleParameter)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"CoconPro"])
        font.setUnderline(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.content = QLabel(bottleParameter)
        self.content.setObjectName(u"content")
        font1 = QFont()
        font1.setFamilies([u"CoconPro"])
        self.content.setFont(font1)
        self.content.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.content.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.content)

        self.quantity = QLabel(bottleParameter)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setFont(font1)
        self.quantity.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.quantity.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.quantity)


        self.retranslateUi(bottleParameter)

        QMetaObject.connectSlotsByName(bottleParameter)
    # setupUi

    def retranslateUi(self, bottleParameter):
        bottleParameter.setWindowTitle(QCoreApplication.translate("bottleParameter", u"Frame", None))
        self.title.setText(QCoreApplication.translate("bottleParameter", u"Bouteille 1", None))
        self.content.setText(QCoreApplication.translate("bottleParameter", u"Rhum Blanc", None))
        self.quantity.setText(QCoreApplication.translate("bottleParameter", u"100 ml", None))
    # retranslateUi

