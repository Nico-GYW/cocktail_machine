# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cocktailStep1Button.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cocktailStep1Button(object):
    def setupUi(self, cocktailStep1Button):
        cocktailStep1Button.setObjectName("cocktailStep1Button")
        cocktailStep1Button.resize(700, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cocktailStep1Button.sizePolicy().hasHeightForWidth())
        cocktailStep1Button.setSizePolicy(sizePolicy)
        cocktailStep1Button.setMinimumSize(QtCore.QSize(700, 200))
        cocktailStep1Button.setMaximumSize(QtCore.QSize(700, 200))
        self.subtitle = QtWidgets.QLabel(cocktailStep1Button)
        self.subtitle.setGeometry(QtCore.QRect(0, 40, 700, 30))
        font = QtGui.QFont()
        font.setFamily("CoconPro")
        font.setPointSize(-1)
        self.subtitle.setFont(font)
        self.subtitle.setStyleSheet("font-size: 20px;\n"
"color: black;")
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")
        self.stepTitle = QtWidgets.QLabel(cocktailStep1Button)
        self.stepTitle.setGeometry(QtCore.QRect(0, 0, 700, 40))
        font = QtGui.QFont()
        font.setFamily("CoconPro")
        font.setPointSize(-1)
        self.stepTitle.setFont(font)
        self.stepTitle.setStyleSheet("font-size: 30px;\n"
"color: black;")
        self.stepTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.stepTitle.setObjectName("stepTitle")
        self.button_1 = QtWidgets.QPushButton(cocktailStep1Button)
        self.button_1.setGeometry(QtCore.QRect(310, 80, 60, 30))
        self.button_1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background-color: #F79643;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f0f0; /* Gris clair lorsqu\'appuyé */\n"
"}\n"
"")
        self.button_1.setObjectName("button_1")

        self.retranslateUi(cocktailStep1Button)
        QtCore.QMetaObject.connectSlotsByName(cocktailStep1Button)

    def retranslateUi(self, cocktailStep1Button):
        _translate = QtCore.QCoreApplication.translate
        self.subtitle.setText(_translate("cocktailStep1Button", "Déposez un verre sur la machine"))
        self.stepTitle.setText(_translate("cocktailStep1Button", "Étape 1 : Mettre un verre"))
        self.button_1.setText(_translate("cocktailStep1Button", "Fait !"))
