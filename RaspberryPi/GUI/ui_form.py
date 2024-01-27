# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QStackedWidget, QToolButton, QWidget)

from pompetteWidgets import LandingPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 480)
        font = QFont()
        font.setFamilies([u"CoconPro"])
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"color: white;\n"
"font-size: 24px;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"CoconPro"])
        self.centralwidget.setFont(font1)
        self.centralwidget.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget.setStyleSheet(u"background-color: #F79643;\n"
"font-family: \"CoconPro\";")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 480))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(800, 480))
        self.stackedWidget.setMaximumSize(QSize(800, 480))
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.landingPage = LandingPage()
        self.landingPage.setObjectName(u"landingPage")
        self.landingPage.setMinimumSize(QSize(800, 0))
        self.imlanding_page = QLabel(self.landingPage)
        self.imlanding_page.setObjectName(u"imlanding_page")
        self.imlanding_page.setGeometry(QRect(690, 0, 111, 481))
        self.imlanding_page.setPixmap(QPixmap(u"ressources/landingPage/filling_glass.png"))
        self.imlanding_page.setScaledContents(True)
        self.tagline = QLabel(self.landingPage)
        self.tagline.setObjectName(u"tagline")
        self.tagline.setGeometry(QRect(290, 390, 201, 51))
        self.tagline.setFont(font)
        self.tagline.setStyleSheet(u"")
        self.tagline.setAlignment(Qt.AlignCenter)
        self.geerings = QLabel(self.landingPage)
        self.geerings.setObjectName(u"geerings")
        self.geerings.setGeometry(QRect(0, 390, 91, 91))
        self.geerings.setPixmap(QPixmap(u"ressources/landingPage/engrenage.png"))
        self.geerings.setScaledContents(True)
        self.logo = QLabel(self.landingPage)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(170, 190, 441, 111))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setPixmap(QPixmap(u"ressources/generic/pompette_blanc.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.stackedWidget.addWidget(self.landingPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMinimumSize(QSize(800, 0))
        self.cocktailView = QFrame(self.mainPage)
        self.cocktailView.setObjectName(u"cocktailView")
        self.cocktailView.setGeometry(QRect(-10, -10, 581, 491))
        self.cocktailView.setStyleSheet(u"background-color: #F9F8F8;")
        self.cocktailView.setFrameShape(QFrame.StyledPanel)
        self.cocktailView.setFrameShadow(QFrame.Raised)
        self.logo_2 = QLabel(self.cocktailView)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(240, 460, 91, 21))
        self.logo_2.setPixmap(QPixmap(u"ressources/generic/pompette_noir.png"))
        self.logo_2.setScaledContents(True)
        self.cocktailCarousel = QStackedWidget(self.cocktailView)
        self.cocktailCarousel.setObjectName(u"cocktailCarousel")
        self.cocktailCarousel.setGeometry(QRect(60, 70, 471, 351))
        self.cocktailCarousel.setFrameShape(QFrame.StyledPanel)
        self.cocktailPage1 = QWidget()
        self.cocktailPage1.setObjectName(u"cocktailPage1")
        self.layoutWidget = QWidget(self.cocktailPage1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 441, 321))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(130, 130))
        self.frame_3.setMaximumSize(QSize(130, 130))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.layoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(130, 130))
        self.frame_5.setMaximumSize(QSize(130, 130))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.layoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(130, 130))
        self.frame_7.setMaximumSize(QSize(130, 130))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(130, 130))
        self.frame_6.setMaximumSize(QSize(130, 130))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(130, 130))
        self.frame_4.setMaximumSize(QSize(130, 130))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.layoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(130, 130))
        self.frame_8.setMaximumSize(QSize(130, 130))
        self.frame_8.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(20, 100, 91, 21))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 40, 61, 51))
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QRect(40, 20, 51, 71))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.label_9.setPixmap(QPixmap(u"ressources/cocktail/spritz.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame_8, 0, 2, 1, 1)

        self.cocktailCarousel.addWidget(self.cocktailPage1)
        self.cocktailPage2 = QWidget()
        self.cocktailPage2.setObjectName(u"cocktailPage2")
        self.cocktailCarousel.addWidget(self.cocktailPage2)
        self.leftButton = QPushButton(self.cocktailView)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setGeometry(QRect(20, 220, 31, 51))
        font2 = QFont()
        font2.setFamilies([u"CoconPro"])
        font2.setKerning(True)
        self.leftButton.setFont(font2)
        self.leftButton.setStyleSheet(u"border: none; /* Supprime la bordure */")
        icon = QIcon()
        icon.addFile(u"ressources/generic/arrow_left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftButton.setIcon(icon)
        self.leftButton.setIconSize(QSize(25, 25))
        self.rightButton = QPushButton(self.cocktailView)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setGeometry(QRect(540, 220, 31, 51))
        self.rightButton.setFont(font2)
        self.rightButton.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"ressources/generic/arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightButton.setIcon(icon1)
        self.rightButton.setIconSize(QSize(25, 25))
        self.pageCount = QLabel(self.cocktailView)
        self.pageCount.setObjectName(u"pageCount")
        self.pageCount.setEnabled(True)
        self.pageCount.setGeometry(QRect(240, 430, 91, 21))
        self.pageCount.setFont(font1)
        self.pageCount.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.pageCount.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.mainPage)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(620, 20, 141, 31))
        self.title.setFont(font1)
        self.title.setStyleSheet(u"font-size: 32px;")
        self.cocktailReceipe = QFrame(self.mainPage)
        self.cocktailReceipe.setObjectName(u"cocktailReceipe")
        self.cocktailReceipe.setGeometry(QRect(600, 130, 171, 231))
        self.cocktailReceipe.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.cocktailReceipe.setFrameShape(QFrame.NoFrame)
        self.cocktailReceipe.setFrameShadow(QFrame.Plain)
        self.cocktailReceipe.setLineWidth(3)
        self.cocktailReceipe.setMidLineWidth(3)
        self.receipeScrollArea = QScrollArea(self.cocktailReceipe)
        self.receipeScrollArea.setObjectName(u"receipeScrollArea")
        self.receipeScrollArea.setGeometry(QRect(10, 10, 141, 211))
        self.receipeScrollArea.setWidgetResizable(True)
        self.receipe = QWidget()
        self.receipe.setObjectName(u"receipe")
        self.receipe.setGeometry(QRect(0, 0, 141, 211))
        self.label = QLabel(self.receipe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 191))
        self.label.setStyleSheet(u"color: black;\n"
"font-size: 10px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.receipeScrollArea.setWidget(self.receipe)
        self.cocktailImage = QLabel(self.mainPage)
        self.cocktailImage.setObjectName(u"cocktailImage")
        self.cocktailImage.setGeometry(QRect(630, 80, 26, 34))
        self.cocktailImage.setFont(font1)
        self.cocktailImage.setStyleSheet(u"font-size: 32px;")
        self.cocktailImage.setPixmap(QPixmap(u"ressources/cocktail/mojito.png"))
        self.cocktailImage.setScaledContents(True)
        self.cocktailName = QLabel(self.mainPage)
        self.cocktailName.setObjectName(u"cocktailName")
        self.cocktailName.setEnabled(True)
        self.cocktailName.setGeometry(QRect(670, 90, 91, 21))
        self.cocktailName.setFont(font1)
        self.cocktailName.setStyleSheet(u"")
        self.toolButton = QToolButton(self.mainPage)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(770, 450, 31, 31))
        self.toolButton.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"ressources/generic/engrenage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QSize(25, 25))
        self.modifyButton = QPushButton(self.mainPage)
        self.modifyButton.setObjectName(u"modifyButton")
        self.modifyButton.setGeometry(QRect(600, 380, 71, 32))
        self.modifyButton.setStyleSheet(u"color: black;\n"
"font-size: 12px;")
        self.addButton = QPushButton(self.mainPage)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(680, 380, 91, 32))
        self.addButton.setStyleSheet(u"color: black;\n"
"font-size: 12px;")
        self.makeButton = QPushButton(self.mainPage)
        self.makeButton.setObjectName(u"makeButton")
        self.makeButton.setGeometry(QRect(600, 410, 171, 32))
        self.makeButton.setStyleSheet(u"color: black;\n"
"font-size: 12px;")
        self.stackedWidget.addWidget(self.mainPage)
        self.parameterPage = QWidget()
        self.parameterPage.setObjectName(u"parameterPage")
        self.parameterPage.setMinimumSize(QSize(800, 0))
        self.parameterPage.setStyleSheet(u"")
        self.parameterView = QFrame(self.parameterPage)
        self.parameterView.setObjectName(u"parameterView")
        self.parameterView.setGeometry(QRect(-10, -10, 581, 491))
        self.parameterView.setStyleSheet(u"background-color: #F79643;")
        self.parameterView.setFrameShape(QFrame.StyledPanel)
        self.parameterView.setFrameShadow(QFrame.Raised)
        self.logo2 = QLabel(self.parameterView)
        self.logo2.setObjectName(u"logo2")
        self.logo2.setGeometry(QRect(240, 460, 91, 21))
        self.logo2.setPixmap(QPixmap(u"ressources/generic/pompette_noir.png"))
        self.logo2.setScaledContents(True)
        self.parameterStack = QStackedWidget(self.parameterView)
        self.parameterStack.setObjectName(u"parameterStack")
        self.parameterStack.setGeometry(QRect(60, 70, 471, 351))
        self.parameterStack.setStyleSheet(u"")
        self.parameterStack.setFrameShape(QFrame.StyledPanel)
        self.glassBottles = QWidget()
        self.glassBottles.setObjectName(u"glassBottles")
        self.glassBottles.setStyleSheet(u"background-color : #F9F8F8;")
        self.layoutWidget2 = QWidget(self.glassBottles)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 471, 351))
        self.gridLayoutGlass = QGridLayout(self.layoutWidget2)
        self.gridLayoutGlass.setSpacing(0)
        self.gridLayoutGlass.setObjectName(u"gridLayoutGlass")
        self.gridLayoutGlass.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.layoutWidget2)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(100, 100))
        self.frame_14.setMaximumSize(QSize(100, 100))
        self.frame_14.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.layoutWidget2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(100, 100))
        self.frame_11.setMaximumSize(QSize(100, 100))
        self.frame_11.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_11, 0, 2, 1, 1)

        self.frame_12 = QFrame(self.layoutWidget2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(100, 100))
        self.frame_12.setMaximumSize(QSize(100, 100))
        self.frame_12.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_12, 1, 2, 1, 1)

        self.frame_10 = QFrame(self.layoutWidget2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QSize(100, 100))
        self.frame_10.setMaximumSize(QSize(100, 100))
        self.frame_10.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.title_2 = QLabel(self.frame_10)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(10, 10, 81, 31))
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.title_2.setAlignment(Qt.AlignCenter)
        self.title_3 = QLabel(self.frame_10)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 40, 81, 31))
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.title_4 = QLabel(self.frame_10)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(10, 60, 81, 20))
        self.title_4.setFont(font1)
        self.title_4.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_4.setAlignment(Qt.AlignCenter)

        self.gridLayoutGlass.addWidget(self.frame_10, 0, 3, 1, 1)

        self.frame_13 = QFrame(self.layoutWidget2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(100, 100))
        self.frame_13.setMaximumSize(QSize(100, 100))
        self.frame_13.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.layoutWidget2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(100, 100))
        self.frame_9.setMaximumSize(QSize(100, 100))
        self.frame_9.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_9, 1, 3, 1, 1)

        self.frame_15 = QFrame(self.layoutWidget2)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QSize(100, 100))
        self.frame_15.setMaximumSize(QSize(100, 100))
        self.frame_15.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_15, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.layoutWidget2)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QSize(100, 100))
        self.frame_16.setMaximumSize(QSize(100, 100))
        self.frame_16.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.4); /* Ombre port\u00e9e */\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_16, 1, 1, 1, 1)

        self.parameterStack.addWidget(self.glassBottles)
        self.plasticBottles = QWidget()
        self.plasticBottles.setObjectName(u"plasticBottles")
        self.plasticBottles.setStyleSheet(u"background-color : #F9F8F8;")
        self.parameterStack.addWidget(self.plasticBottles)
        self.frame = QFrame(self.parameterPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(570, 0, 231, 481))
        self.frame.setStyleSheet(u"background-color : #F9F8F8;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.titleParameter = QLabel(self.frame)
        self.titleParameter.setObjectName(u"titleParameter")
        self.titleParameter.setGeometry(QRect(30, 20, 171, 31))
        self.titleParameter.setFont(font1)
        self.titleParameter.setStyleSheet(u"font-size: 32px;\n"
"color: black;")
        self.toolButtonParameter = QToolButton(self.frame)
        self.toolButtonParameter.setObjectName(u"toolButtonParameter")
        self.toolButtonParameter.setGeometry(QRect(200, 450, 31, 31))
        self.toolButtonParameter.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"ressources/generic/engrenage_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonParameter.setIcon(icon3)
        self.toolButtonParameter.setIconSize(QSize(25, 25))
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 120, 151, 61))
        font3 = QFont()
        font3.setFamilies([u"CoconPro"])
        font3.setStrikeOut(False)
        self.radioButton.setFont(font3)
        self.radioButton.setLayoutDirection(Qt.LeftToRight)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	border-radius: 10px;\n"
"	background-color : #FFF;\n"
"	color: black;\n"
"	font-size: 16px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"ressources/generic/bouteille.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton.setIcon(icon4)
        self.radioButton.setIconSize(QSize(16, 40))
        self.radioButton.setCheckable(False)
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(40, 200, 151, 61))
        self.radioButton_2.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	border-radius: 10px;\n"
"	background-color : #FFF;\n"
"	color: black;\n"
"	font-size: 16px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"ressources/generic/soft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_2.setIcon(icon5)
        self.radioButton_2.setIconSize(QSize(40, 40))
        self.radioButton_2.setCheckable(False)
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 280, 151, 61))
        self.radioButton_3.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_3.setAutoFillBackground(False)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"	border-radius: 10px;\n"
"	background-color : #FFF;\n"
"	color: black;\n"
"	font-size: 16px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"ressources/generic/outil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_3.setIcon(icon6)
        self.radioButton_3.setIconSize(QSize(50, 50))
        self.radioButton_3.setCheckable(False)
        self.stackedWidget.addWidget(self.parameterPage)
        self.barManPage = QWidget()
        self.barManPage.setObjectName(u"barManPage")
        self.barManPage.setMinimumSize(QSize(800, 0))
        self.stackedWidget.addWidget(self.barManPage)
        self.processingPage = QWidget()
        self.processingPage.setObjectName(u"processingPage")
        self.processingPage.setMinimumSize(QSize(800, 0))
        self.stackedWidget.addWidget(self.processingPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.parameterStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imlanding_page.setText("")
        self.tagline.setText(QCoreApplication.translate("MainWindow", u"Un verre d'avance", None))
        self.geerings.setText("")
        self.logo.setText("")
        self.logo_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mojito", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.leftButton.setText("")
        self.rightButton.setText("")
        self.pageCount.setText(QCoreApplication.translate("MainWindow", u"Page 1/3", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Cocktail", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"2 cl de rhum blanc\n"
"1 cl de sirop de sucre de canne\n"
"4 tranche de citron vert\n"
"3 feuilles de menthe\n"
"1/2 verre d\u2019eau\n"
"gla\u00e7on", None))
        self.cocktailImage.setText("")
        self.cocktailName.setText(QCoreApplication.translate("MainWindow", u"Mojito", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.modifyButton.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Suppl\u00e9ment", None))
        self.makeButton.setText(QCoreApplication.translate("MainWindow", u"Make !", None))
        self.logo2.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Rhum Blanc", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"100 ml", None))
        self.titleParameter.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.toolButtonParameter.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Bouteilles", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Soft", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
    # retranslateUi

