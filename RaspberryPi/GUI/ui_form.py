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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpinBox,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

from landingPageWidgets import LandingPage
from mainPageWidgets import (CocktailCard, MainPage)
from parameterPageWidgets import (BottleParameter, DispenserControl, ParameterPage)

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
"QPushButton {\n"
"        border-radius: 10px;\n"
"        background-color: #FFF;\n"
"        color: black;\n"
"        font-size: 16px;\n"
"        border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"CoconPro"])
        self.centralwidget.setFont(font1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"background-color: #F79643;\n"
"font-family: \"CoconPro\";\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color : #FFF;\n"
"	color: black;\n"
"	font-size: 16px;\n"
"     border: none;\n"
"}")
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
        self.mainPage = MainPage()
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
        self.cocktailCarousel.setFrameShape(QFrame.NoFrame)
        self.cocktailPage1 = QWidget()
        self.cocktailPage1.setObjectName(u"cocktailPage1")
        self.layoutWidget = QWidget(self.cocktailPage1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 441, 321))
        self.gridCocktailLayout = QGridLayout(self.layoutWidget)
        self.gridCocktailLayout.setObjectName(u"gridCocktailLayout")
        self.gridCocktailLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(130, 130))
        self.frame_3.setMaximumSize(QSize(130, 130))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridCocktailLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.layoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(130, 130))
        self.frame_5.setMaximumSize(QSize(130, 130))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridCocktailLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.layoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(130, 130))
        self.frame_7.setMaximumSize(QSize(130, 130))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridCocktailLayout.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(130, 130))
        self.frame_6.setMaximumSize(QSize(130, 130))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridCocktailLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(130, 130))
        self.frame_4.setMaximumSize(QSize(130, 130))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridCocktailLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.cocktailCard = CocktailCard(self.layoutWidget)
        self.cocktailCard.setObjectName(u"cocktailCard")
        sizePolicy.setHeightForWidth(self.cocktailCard.sizePolicy().hasHeightForWidth())
        self.cocktailCard.setSizePolicy(sizePolicy)
        self.cocktailCard.setMinimumSize(QSize(130, 130))
        self.cocktailCard.setMaximumSize(QSize(130, 130))
        self.cocktailCard.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.cocktailCard.setFrameShape(QFrame.StyledPanel)
        self.cocktailCard.setFrameShadow(QFrame.Raised)
        self.cocktailCardName = QLabel(self.cocktailCard)
        self.cocktailCardName.setObjectName(u"cocktailCardName")
        self.cocktailCardName.setEnabled(True)
        self.cocktailCardName.setGeometry(QRect(20, 100, 91, 21))
        self.cocktailCardName.setFont(font1)
        self.cocktailCardName.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.cocktailCardName.setAlignment(Qt.AlignCenter)
        self.cocktailCardImage = QLabel(self.cocktailCard)
        self.cocktailCardImage.setObjectName(u"cocktailCardImage")
        self.cocktailCardImage.setEnabled(True)
        self.cocktailCardImage.setGeometry(QRect(40, 20, 51, 71))
        self.cocktailCardImage.setFont(font1)
        self.cocktailCardImage.setStyleSheet(u"color: black;\n"
"font-size: 16px;")
        self.cocktailCardImage.setPixmap(QPixmap(u"ressources/cocktail/spritz.png"))
        self.cocktailCardImage.setScaledContents(True)
        self.cocktailCardImage.setAlignment(Qt.AlignCenter)

        self.gridCocktailLayout.addWidget(self.cocktailCard, 0, 2, 1, 1)

        self.cocktailCarousel.addWidget(self.cocktailPage1)
        self.cocktailPage2 = QWidget()
        self.cocktailPage2.setObjectName(u"cocktailPage2")
        self.cocktailCarousel.addWidget(self.cocktailPage2)
        self.leftButtonMainPage = QPushButton(self.cocktailView)
        self.leftButtonMainPage.setObjectName(u"leftButtonMainPage")
        self.leftButtonMainPage.setGeometry(QRect(20, 220, 31, 51))
        font2 = QFont()
        font2.setFamilies([u"CoconPro"])
        font2.setKerning(True)
        self.leftButtonMainPage.setFont(font2)
        self.leftButtonMainPage.setStyleSheet(u"border: none; /* Supprime la bordure */")
        icon = QIcon()
        icon.addFile(u"ressources/generic/arrow_left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leftButtonMainPage.setIcon(icon)
        self.leftButtonMainPage.setIconSize(QSize(25, 25))
        self.rightButtonMainPage = QPushButton(self.cocktailView)
        self.rightButtonMainPage.setObjectName(u"rightButtonMainPage")
        self.rightButtonMainPage.setGeometry(QRect(540, 220, 31, 51))
        self.rightButtonMainPage.setFont(font2)
        self.rightButtonMainPage.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"ressources/generic/arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightButtonMainPage.setIcon(icon1)
        self.rightButtonMainPage.setIconSize(QSize(25, 25))
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
        self.cocktailReceipeArea = QFrame(self.mainPage)
        self.cocktailReceipeArea.setObjectName(u"cocktailReceipeArea")
        self.cocktailReceipeArea.setGeometry(QRect(600, 130, 171, 231))
        self.cocktailReceipeArea.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;")
        self.cocktailReceipeArea.setFrameShape(QFrame.NoFrame)
        self.cocktailReceipeArea.setFrameShadow(QFrame.Plain)
        self.cocktailReceipeArea.setLineWidth(3)
        self.cocktailReceipeArea.setMidLineWidth(3)
        self.receipeScrollArea = QScrollArea(self.cocktailReceipeArea)
        self.receipeScrollArea.setObjectName(u"receipeScrollArea")
        self.receipeScrollArea.setGeometry(QRect(10, 10, 141, 211))
        self.receipeScrollArea.setWidgetResizable(True)
        self.receipe = QWidget()
        self.receipe.setObjectName(u"receipe")
        self.receipe.setGeometry(QRect(0, 0, 141, 211))
        self.cocktailReceipe = QLabel(self.receipe)
        self.cocktailReceipe.setObjectName(u"cocktailReceipe")
        self.cocktailReceipe.setGeometry(QRect(10, 10, 131, 191))
        self.cocktailReceipe.setStyleSheet(u"color: black;\n"
"font-size: 10px;")
        self.cocktailReceipe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.receipeScrollArea.setWidget(self.receipe)
        self.cocktailImage = QLabel(self.mainPage)
        self.cocktailImage.setObjectName(u"cocktailImage")
        self.cocktailImage.setGeometry(QRect(620, 80, 26, 34))
        self.cocktailImage.setFont(font1)
        self.cocktailImage.setStyleSheet(u"font-size: 32px;")
        self.cocktailImage.setPixmap(QPixmap(u"ressources/cocktail/mojito.png"))
        self.cocktailImage.setScaledContents(True)
        self.cocktailName = QLabel(self.mainPage)
        self.cocktailName.setObjectName(u"cocktailName")
        self.cocktailName.setEnabled(True)
        self.cocktailName.setGeometry(QRect(660, 80, 111, 41))
        self.cocktailName.setFont(font1)
        self.cocktailName.setStyleSheet(u"")
        self.cocktailName.setTextFormat(Qt.AutoText)
        self.cocktailName.setScaledContents(False)
        self.cocktailName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.cocktailName.setWordWrap(True)
        self.toolButtonMainPage = QToolButton(self.mainPage)
        self.toolButtonMainPage.setObjectName(u"toolButtonMainPage")
        self.toolButtonMainPage.setGeometry(QRect(770, 450, 31, 31))
        self.toolButtonMainPage.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"ressources/generic/engrenage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonMainPage.setIcon(icon2)
        self.toolButtonMainPage.setIconSize(QSize(25, 25))
        self.modifyButton = QPushButton(self.mainPage)
        self.modifyButton.setObjectName(u"modifyButton")
        self.modifyButton.setGeometry(QRect(600, 380, 71, 31))
        self.modifyButton.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f0f0; /* Gris clair lorsqu'appuy\u00e9 */\n"
"}\n"
"")
        self.addButton = QPushButton(self.mainPage)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(680, 380, 91, 31))
        self.addButton.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f0f0; /* Gris clair lorsqu'appuy\u00e9 */\n"
"}\n"
"")
        self.makeButton = QPushButton(self.mainPage)
        self.makeButton.setObjectName(u"makeButton")
        self.makeButton.setGeometry(QRect(600, 420, 171, 21))
        self.makeButton.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f0f0f0; /* Gris clair lorsqu'appuy\u00e9 */\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.mainPage)
        self.parameterPage = ParameterPage()
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
        self.parameterStack.setStyleSheet(u"border-radius: 15px; /* Bords arrondis de 5px */")
        self.parameterStack.setFrameShape(QFrame.StyledPanel)
        self.glassBottles = QWidget()
        self.glassBottles.setObjectName(u"glassBottles")
        font3 = QFont()
        font3.setFamilies([u"CoconPro"])
        font3.setKerning(False)
        self.glassBottles.setFont(font3)
        self.glassBottles.setStyleSheet(u"background-color : #F9F8F8;")
        self.layoutWidget2 = QWidget(self.glassBottles)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 471, 351))
        self.gridLayoutGlass = QGridLayout(self.layoutWidget2)
        self.gridLayoutGlass.setSpacing(0)
        self.gridLayoutGlass.setObjectName(u"gridLayoutGlass")
        self.gridLayoutGlass.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayoutGlass.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.layoutWidget2)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(100, 100))
        self.frame_14.setMaximumSize(QSize(100, 100))
        self.frame_14.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
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
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_12, 1, 2, 1, 1)

        self.glassBottle1 = BottleParameter(self.layoutWidget2)
        self.glassBottle1.setObjectName(u"glassBottle1")
        sizePolicy.setHeightForWidth(self.glassBottle1.sizePolicy().hasHeightForWidth())
        self.glassBottle1.setSizePolicy(sizePolicy)
        self.glassBottle1.setMinimumSize(QSize(100, 100))
        self.glassBottle1.setMaximumSize(QSize(100, 100))
        self.glassBottle1.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.glassBottle1.setFrameShape(QFrame.StyledPanel)
        self.glassBottle1.setFrameShadow(QFrame.Raised)
        self.title_2 = QLabel(self.glassBottle1)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(10, 10, 81, 31))
        font4 = QFont()
        font4.setFamilies([u"CoconPro"])
        font4.setUnderline(False)
        self.title_2.setFont(font4)
        self.title_2.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.title_2.setAlignment(Qt.AlignCenter)
        self.title_3 = QLabel(self.glassBottle1)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 40, 81, 31))
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.title_4 = QLabel(self.glassBottle1)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(10, 60, 81, 20))
        self.title_4.setFont(font1)
        self.title_4.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_4.setAlignment(Qt.AlignCenter)

        self.gridLayoutGlass.addWidget(self.glassBottle1, 0, 3, 1, 1)

        self.frame_13 = QFrame(self.layoutWidget2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(100, 100))
        self.frame_13.setMaximumSize(QSize(100, 100))
        self.frame_13.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
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
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayoutGlass.addWidget(self.frame_16, 1, 1, 1, 1)

        self.parameterStack.addWidget(self.glassBottles)
        self.plasticBottles = QWidget()
        self.plasticBottles.setObjectName(u"plasticBottles")
        self.plasticBottles.setStyleSheet(u"background-color : #F9F8F8;")
        self.layoutWidget2_2 = QWidget(self.plasticBottles)
        self.layoutWidget2_2.setObjectName(u"layoutWidget2_2")
        self.layoutWidget2_2.setGeometry(QRect(0, 0, 471, 351))
        self.gridLayoutPlastic = QGridLayout(self.layoutWidget2_2)
        self.gridLayoutPlastic.setSpacing(0)
        self.gridLayoutPlastic.setObjectName(u"gridLayoutPlastic")
        self.gridLayoutPlastic.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayoutPlastic.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.layoutWidget2_2)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QSize(100, 100))
        self.frame_23.setMaximumSize(QSize(100, 100))
        self.frame_23.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayoutPlastic.addWidget(self.frame_23, 1, 0, 1, 1)

        self.glassBottle1_3 = BottleParameter(self.layoutWidget2_2)
        self.glassBottle1_3.setObjectName(u"glassBottle1_3")
        sizePolicy.setHeightForWidth(self.glassBottle1_3.sizePolicy().hasHeightForWidth())
        self.glassBottle1_3.setSizePolicy(sizePolicy)
        self.glassBottle1_3.setMinimumSize(QSize(100, 100))
        self.glassBottle1_3.setMaximumSize(QSize(100, 100))
        self.glassBottle1_3.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.glassBottle1_3.setFrameShape(QFrame.StyledPanel)
        self.glassBottle1_3.setFrameShadow(QFrame.Raised)
        self.title_8 = QLabel(self.glassBottle1_3)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setGeometry(QRect(10, 10, 81, 31))
        self.title_8.setFont(font4)
        self.title_8.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.title_8.setAlignment(Qt.AlignCenter)
        self.title_9 = QLabel(self.glassBottle1_3)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setGeometry(QRect(10, 40, 81, 31))
        self.title_9.setFont(font1)
        self.title_9.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_9.setAlignment(Qt.AlignCenter)
        self.title_10 = QLabel(self.glassBottle1_3)
        self.title_10.setObjectName(u"title_10")
        self.title_10.setGeometry(QRect(10, 60, 81, 20))
        self.title_10.setFont(font1)
        self.title_10.setStyleSheet(u"font-size: 10px;\n"
"color: black;")
        self.title_10.setAlignment(Qt.AlignCenter)

        self.gridLayoutPlastic.addWidget(self.glassBottle1_3, 0, 1, 1, 1)

        self.frame_26 = QFrame(self.layoutWidget2_2)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(100, 100))
        self.frame_26.setMaximumSize(QSize(100, 100))
        self.frame_26.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.gridLayoutPlastic.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_27 = QFrame(self.layoutWidget2_2)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QSize(100, 100))
        self.frame_27.setMaximumSize(QSize(100, 100))
        self.frame_27.setStyleSheet(u"background-color: #FFFFFF; /* Couleur de fond blanc */\n"
"border-radius: 15px; /* Bords arrondis de 5px */\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.gridLayoutPlastic.addWidget(self.frame_27, 1, 1, 1, 1)

        self.parameterStack.addWidget(self.plasticBottles)
        self.machineParameter = QWidget()
        self.machineParameter.setObjectName(u"machineParameter")
        self.machineParameter.setStyleSheet(u"background-color : #F9F8F8;")
        self.machineParameterStack = QStackedWidget(self.machineParameter)
        self.machineParameterStack.setObjectName(u"machineParameterStack")
        self.machineParameterStack.setGeometry(QRect(30, 0, 411, 351))
        self.dispenserControl = QWidget()
        self.dispenserControl.setObjectName(u"dispenserControl")
        self.layoutWidget1 = QWidget(self.dispenserControl)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 20, 401, 311))
        self.dispenserGridLayout = QGridLayout(self.layoutWidget1)
        self.dispenserGridLayout.setObjectName(u"dispenserGridLayout")
        self.dispenserGridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.layoutWidget1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 71, 31))
        self.label_6.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.verticalSlider_6 = QSlider(self.frame_8)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setGeometry(QRect(20, 60, 31, 51))
        self.verticalSlider_6.setMaximum(1)
        self.verticalSlider_6.setOrientation(Qt.Vertical)

        self.dispenserGridLayout.addWidget(self.frame_8, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.layoutWidget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 71, 31))
        self.label_4.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.verticalSlider_4 = QSlider(self.frame_2)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setGeometry(QRect(30, 60, 31, 51))
        self.verticalSlider_4.setMaximum(1)
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.dispenserGridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_10 = DispenserControl(self.layoutWidget1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 71, 31))
        self.label_8.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.verticalSlider_8 = QSlider(self.frame_10)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setGeometry(QRect(30, 60, 31, 51))
        self.verticalSlider_8.setMaximum(1)
        self.verticalSlider_8.setOrientation(Qt.Vertical)

        self.dispenserGridLayout.addWidget(self.frame_10, 0, 3, 1, 1)

        self.frame = QFrame(self.layoutWidget1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 71, 31))
        self.label.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalSlider = QSlider(self.frame)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(20, 60, 31, 51))
        self.verticalSlider.setMaximum(1)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.dispenserGridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.layoutWidget1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 10, 71, 31))
        self.label_10.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.verticalSlider_10 = QSlider(self.frame_17)
        self.verticalSlider_10.setObjectName(u"verticalSlider_10")
        self.verticalSlider_10.setGeometry(QRect(20, 50, 31, 51))
        self.verticalSlider_10.setMaximum(1)
        self.verticalSlider_10.setOrientation(Qt.Vertical)

        self.dispenserGridLayout.addWidget(self.frame_17, 1, 0, 1, 1)

        self.machineParameterStack.addWidget(self.dispenserControl)
        self.otherControl = QWidget()
        self.otherControl.setObjectName(u"otherControl")
        self.layoutWidget_3 = QWidget(self.otherControl)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 20, 361, 318))
        self.otherControlGridLayout = QGridLayout(self.layoutWidget_3)
        self.otherControlGridLayout.setObjectName(u"otherControlGridLayout")
        self.otherControlGridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.layoutWidget_3)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QSize(100, 150))
        self.frame_25.setMaximumSize(QSize(100, 150))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(80, 30))
        self.label_13.setMaximumSize(QSize(80, 30))
        self.label_13.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.xStepperSlider = QSlider(self.frame_25)
        self.xStepperSlider.setObjectName(u"xStepperSlider")
        self.xStepperSlider.setGeometry(QRect(10, 60, 81, 51))
        self.xStepperSlider.setMinimum(-100)
        self.xStepperSlider.setMaximum(100)
        self.xStepperSlider.setOrientation(Qt.Horizontal)
        self.xStepperButton = QPushButton(self.frame_25)
        self.xStepperButton.setObjectName(u"xStepperButton")
        self.xStepperButton.setGeometry(QRect(6, 120, 90, 20))
        self.xStepperButton.setStyleSheet(u"QPushButton {\n"
"        border-radius: 5px;\n"
"        background-color: #F79643;\n"
"        color: white;\n"
"        font-size: 10px;\n"
"        border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFBC50; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")

        self.otherControlGridLayout.addWidget(self.frame_25, 0, 2, 1, 1)

        self.frame_28 = QFrame(self.layoutWidget_3)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QSize(100, 150))
        self.frame_28.setMaximumSize(QSize(100, 150))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(80, 30))
        self.label_15.setMaximumSize(QSize(80, 30))
        self.label_15.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.cylinderSlider = QSlider(self.frame_28)
        self.cylinderSlider.setObjectName(u"cylinderSlider")
        self.cylinderSlider.setGeometry(QRect(9, 60, 81, 51))
        self.cylinderSlider.setMinimum(-100)
        self.cylinderSlider.setMaximum(100)
        self.cylinderSlider.setOrientation(Qt.Horizontal)
        self.cylinderButton = QPushButton(self.frame_28)
        self.cylinderButton.setObjectName(u"cylinderButton")
        self.cylinderButton.setGeometry(QRect(6, 120, 90, 20))
        self.cylinderButton.setStyleSheet(u"QPushButton {\n"
"        border-radius: 5px;\n"
"        background-color: #F79643;\n"
"        color: white;\n"
"        font-size: 10px;\n"
"        border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFBC50; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")

        self.otherControlGridLayout.addWidget(self.frame_28, 0, 0, 1, 1)

        self.frame_30 = QFrame(self.layoutWidget_3)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QSize(100, 150))
        self.frame_30.setMaximumSize(QSize(100, 150))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(80, 30))
        self.label_17.setMaximumSize(QSize(80, 30))
        self.label_17.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.verticalSlider_17 = QSlider(self.frame_30)
        self.verticalSlider_17.setObjectName(u"verticalSlider_17")
        self.verticalSlider_17.setGeometry(QRect(30, 60, 40, 61))
        self.verticalSlider_17.setMaximum(1)
        self.verticalSlider_17.setOrientation(Qt.Vertical)

        self.otherControlGridLayout.addWidget(self.frame_30, 1, 1, 1, 1)

        self.frame_32 = QFrame(self.layoutWidget_3)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMinimumSize(QSize(100, 150))
        self.frame_32.setMaximumSize(QSize(100, 150))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_32)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(80, 30))
        self.label_18.setMaximumSize(QSize(80, 30))
        self.label_18.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.yStepperSlider = QSlider(self.frame_32)
        self.yStepperSlider.setObjectName(u"yStepperSlider")
        self.yStepperSlider.setGeometry(QRect(30, 50, 40, 61))
        self.yStepperSlider.setMinimum(-100)
        self.yStepperSlider.setMaximum(100)
        self.yStepperSlider.setOrientation(Qt.Vertical)
        self.yStepperButton = QPushButton(self.frame_32)
        self.yStepperButton.setObjectName(u"yStepperButton")
        self.yStepperButton.setGeometry(QRect(6, 120, 90, 20))
        self.yStepperButton.setStyleSheet(u"QPushButton {\n"
"        border-radius: 5px;\n"
"        background-color: #F79643;\n"
"        color: white;\n"
"        font-size: 10px;\n"
"        border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFBC50; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")

        self.otherControlGridLayout.addWidget(self.frame_32, 0, 1, 1, 1)

        self.frame_29 = QFrame(self.layoutWidget_3)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QSize(100, 150))
        self.frame_29.setMaximumSize(QSize(100, 150))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_29)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(80, 30))
        self.label_14.setMaximumSize(QSize(80, 30))
        self.label_14.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.verticalSlider_14 = QSlider(self.frame_29)
        self.verticalSlider_14.setObjectName(u"verticalSlider_14")
        self.verticalSlider_14.setGeometry(QRect(20, 60, 71, 61))
        self.verticalSlider_14.setMinimum(-1)
        self.verticalSlider_14.setMaximum(1)
        self.verticalSlider_14.setPageStep(1)
        self.verticalSlider_14.setValue(0)
        self.verticalSlider_14.setOrientation(Qt.Horizontal)

        self.otherControlGridLayout.addWidget(self.frame_29, 1, 0, 1, 1)

        self.frame_31 = QFrame(self.layoutWidget_3)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setMinimumSize(QSize(100, 150))
        self.frame_31.setMaximumSize(QSize(100, 150))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 80, 30))
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(80, 30))
        self.label_16.setMaximumSize(QSize(80, 30))
        self.label_16.setStyleSheet(u"color: black;\n"
"font-size: 10px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.verticalSlider_16 = QSlider(self.frame_31)
        self.verticalSlider_16.setObjectName(u"verticalSlider_16")
        self.verticalSlider_16.setGeometry(QRect(30, 60, 40, 61))
        self.verticalSlider_16.setMaximum(100)
        self.verticalSlider_16.setValue(100)
        self.verticalSlider_16.setOrientation(Qt.Vertical)
        self.verticalSlider_16.setInvertedControls(True)

        self.otherControlGridLayout.addWidget(self.frame_31, 1, 2, 1, 1)

        self.machineParameterStack.addWidget(self.otherControl)
        self.softControl = QWidget()
        self.softControl.setObjectName(u"softControl")
        self.layoutWidget_2 = QWidget(self.softControl)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 110, 401, 141))
        self.softGridLayout = QGridLayout(self.layoutWidget_2)
        self.softGridLayout.setObjectName(u"softGridLayout")
        self.softGridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.layoutWidget_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 71, 31))
        self.label_9.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.verticalSlider_9 = QSlider(self.frame_20)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setGeometry(QRect(30, 60, 31, 51))
        self.verticalSlider_9.setMaximum(1)
        self.verticalSlider_9.setOrientation(Qt.Vertical)

        self.softGridLayout.addWidget(self.frame_20, 0, 3, 1, 1)

        self.frame_18 = QFrame(self.layoutWidget_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 71, 31))
        self.label_7.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.verticalSlider_7 = QSlider(self.frame_18)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setGeometry(QRect(20, 60, 31, 51))
        self.verticalSlider_7.setMaximum(1)
        self.verticalSlider_7.setOrientation(Qt.Vertical)

        self.softGridLayout.addWidget(self.frame_18, 0, 2, 1, 1)

        self.frame_19 = QFrame(self.layoutWidget_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 31))
        self.label_5.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.verticalSlider_5 = QSlider(self.frame_19)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setGeometry(QRect(30, 60, 31, 51))
        self.verticalSlider_5.setMaximum(1)
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.softGridLayout.addWidget(self.frame_19, 0, 1, 1, 1)

        self.frame_21 = QFrame(self.layoutWidget_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_21)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 71, 31))
        self.label_2.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.verticalSlider_2 = QSlider(self.frame_21)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setGeometry(QRect(20, 60, 31, 51))
        self.verticalSlider_2.setMaximum(1)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.softGridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

        self.machineParameterStack.addWidget(self.softControl)
        self.ledControl = QWidget()
        self.ledControl.setObjectName(u"ledControl")
        self.ledStripComboBox = QComboBox(self.ledControl)
        self.ledStripComboBox.setObjectName(u"ledStripComboBox")
        self.ledStripComboBox.setGeometry(QRect(70, 120, 100, 30))
        self.ledStripComboBox.setStyleSheet(u"QComboBox {\n"
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
        self.ledStripSpeedSpinBox = QSpinBox(self.ledControl)
        self.ledStripSpeedSpinBox.setObjectName(u"ledStripSpeedSpinBox")
        self.ledStripSpeedSpinBox.setGeometry(QRect(70, 200, 100, 30))
        self.ledStripSpeedSpinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.ledStripColorButton = QPushButton(self.ledControl)
        self.ledStripColorButton.setObjectName(u"ledStripColorButton")
        self.ledStripColorButton.setGeometry(QRect(240, 160, 100, 100))
        self.ledStripColorButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 50px; /* Coins arrondis de 3px */\n"
"	background-color: #F79643;\n"
"	border: 1px solid #707070; /* Bordure de 1px en noir */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFBC50; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")
        self.label_3 = QLabel(self.ledControl)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 100, 61, 16))
        self.label_3.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.ledControl)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 180, 71, 16))
        self.label_11.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.ledControl)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(260, 130, 61, 16))
        self.label_12.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.ledControl)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 40, 71, 31))
        self.label_19.setStyleSheet(u"color: black;\n"
"font-size: 12px;\n"
"border-radius: 8px;\n"
"background-color: #A0ACB0;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.ledStripBrightnessSpinBox = QSpinBox(self.ledControl)
        self.ledStripBrightnessSpinBox.setObjectName(u"ledStripBrightnessSpinBox")
        self.ledStripBrightnessSpinBox.setGeometry(QRect(70, 280, 100, 30))
        self.ledStripBrightnessSpinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.label_20 = QLabel(self.ledControl)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 260, 71, 16))
        self.label_20.setStyleSheet(u"font-size: 12px;\n"
"color: black;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.machineParameterStack.addWidget(self.ledControl)
        self.rightButtonControl = QPushButton(self.machineParameter)
        self.rightButtonControl.setObjectName(u"rightButtonControl")
        self.rightButtonControl.setGeometry(QRect(440, 150, 31, 51))
        self.rightButtonControl.setFont(font2)
        self.rightButtonControl.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        self.rightButtonControl.setIcon(icon1)
        self.rightButtonControl.setIconSize(QSize(25, 25))
        self.leftButtonControl = QPushButton(self.machineParameter)
        self.leftButtonControl.setObjectName(u"leftButtonControl")
        self.leftButtonControl.setGeometry(QRect(0, 150, 31, 51))
        self.leftButtonControl.setFont(font2)
        self.leftButtonControl.setStyleSheet(u"border: none; /* Supprime la bordure */")
        self.leftButtonControl.setIcon(icon)
        self.leftButtonControl.setIconSize(QSize(25, 25))
        self.parameterStack.addWidget(self.machineParameter)
        self.parameterRightPannel = QFrame(self.parameterPage)
        self.parameterRightPannel.setObjectName(u"parameterRightPannel")
        self.parameterRightPannel.setGeometry(QRect(570, 0, 231, 481))
        self.parameterRightPannel.setStyleSheet(u"background-color : #F9F8F8;\n"
"")
        self.parameterRightPannel.setFrameShape(QFrame.StyledPanel)
        self.parameterRightPannel.setFrameShadow(QFrame.Raised)
        self.titleParameter = QLabel(self.parameterRightPannel)
        self.titleParameter.setObjectName(u"titleParameter")
        self.titleParameter.setGeometry(QRect(30, 20, 171, 31))
        self.titleParameter.setFont(font1)
        self.titleParameter.setStyleSheet(u"font-size: 32px;\n"
"color: black;")
        self.toolButtonParameterPage = QToolButton(self.parameterRightPannel)
        self.toolButtonParameterPage.setObjectName(u"toolButtonParameterPage")
        self.toolButtonParameterPage.setGeometry(QRect(200, 450, 31, 31))
        self.toolButtonParameterPage.setStyleSheet(u"border: none; /* Supprime la bordure */\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"ressources/generic/engrenage_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonParameterPage.setIcon(icon3)
        self.toolButtonParameterPage.setIconSize(QSize(25, 25))
        self.verticalLayoutWidget = QWidget(self.parameterRightPannel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 110, 184, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonBottleParameter = QPushButton(self.verticalLayoutWidget)
        self.pushButtonBottleParameter.setObjectName(u"pushButtonBottleParameter")
        font5 = QFont()
        font5.setFamilies([u"CoconPro"])
        font5.setStrikeOut(False)
        self.pushButtonBottleParameter.setFont(font5)
        self.pushButtonBottleParameter.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonBottleParameter.setAutoFillBackground(False)
        self.pushButtonBottleParameter.setStyleSheet(u"QPushButton {\n"
"        border-radius: 10px;\n"
"        background-color: #FFF;\n"
"        color: black;\n"
"        font-size: 16px;\n"
"        border: none;\n"
"	   text-align: left;\n"
"	   padding-left: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #EAEAEA; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"ressources/generic/bouteille.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonBottleParameter.setIcon(icon4)
        self.pushButtonBottleParameter.setIconSize(QSize(16, 40))
        self.pushButtonBottleParameter.setCheckable(True)
        self.pushButtonBottleParameter.setChecked(True)
        self.pushButtonBottleParameter.setAutoExclusive(True)
        self.pushButtonBottleParameter.setFlat(False)

        self.verticalLayout.addWidget(self.pushButtonBottleParameter)

        self.pushButtonSoftParameter = QPushButton(self.verticalLayoutWidget)
        self.pushButtonSoftParameter.setObjectName(u"pushButtonSoftParameter")
        self.pushButtonSoftParameter.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonSoftParameter.setStyleSheet(u"QPushButton {\n"
"        border-radius: 10px;\n"
"        background-color: #FFF;\n"
"        color: black;\n"
"        font-size: 16px;\n"
"        border: none;\n"
"	   text-align: left;\n"
"	   padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #EAEAEA; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"ressources/generic/soft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSoftParameter.setIcon(icon5)
        self.pushButtonSoftParameter.setIconSize(QSize(40, 40))
        self.pushButtonSoftParameter.setCheckable(True)
        self.pushButtonSoftParameter.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButtonSoftParameter)

        self.pushButtonMachineParameter = QPushButton(self.verticalLayoutWidget)
        self.pushButtonMachineParameter.setObjectName(u"pushButtonMachineParameter")
        self.pushButtonMachineParameter.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonMachineParameter.setAutoFillBackground(False)
        self.pushButtonMachineParameter.setStyleSheet(u"QPushButton {\n"
"        border-radius: 10px;\n"
"        background-color: #FFF;\n"
"        color: black;\n"
"        font-size: 16px;\n"
"        border: none;\n"
"	   text-align: left;\n"
"	   padding-left: 0px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #EAEAEA; /* Fond gris clair pour les boutons enfonc\u00e9s */\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"ressources/generic/outil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMachineParameter.setIcon(icon6)
        self.pushButtonMachineParameter.setIconSize(QSize(40, 50))
        self.pushButtonMachineParameter.setCheckable(True)
        self.pushButtonMachineParameter.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButtonMachineParameter)

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

        self.stackedWidget.setCurrentIndex(2)
        self.parameterStack.setCurrentIndex(2)
        self.pushButtonBottleParameter.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imlanding_page.setText("")
        self.tagline.setText(QCoreApplication.translate("MainWindow", u"Un verre d'avance", None))
        self.geerings.setText("")
        self.logo.setText("")
        self.logo_2.setText("")
        self.cocktailCardName.setText(QCoreApplication.translate("MainWindow", u"Mojito", None))
        self.cocktailCardImage.setText("")
        self.leftButtonMainPage.setText("")
        self.rightButtonMainPage.setText("")
        self.pageCount.setText(QCoreApplication.translate("MainWindow", u"Page 1/3", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Cocktail", None))
        self.cocktailReceipe.setText(QCoreApplication.translate("MainWindow", u"2 cl de rhum blanc\n"
"1 cl de sirop de sucre de canne\n"
"4 tranche de citron vert\n"
"3 feuilles de menthe\n"
"1/2 verre d\u2019eau\n"
"gla\u00e7on", None))
        self.cocktailImage.setText("")
        self.cocktailName.setText(QCoreApplication.translate("MainWindow", u"Mojito", None))
        self.toolButtonMainPage.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.modifyButton.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Suppl\u00e9ment", None))
        self.makeButton.setText(QCoreApplication.translate("MainWindow", u"Make !", None))
        self.logo2.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Rhum Blanc", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"100 ml", None))
        self.title_8.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.title_9.setText(QCoreApplication.translate("MainWindow", u"Rhum Blanc", None))
        self.title_10.setText(QCoreApplication.translate("MainWindow", u"100 ml", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bouteille 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Plateau X", None))
        self.xStepperButton.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 l'origine", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Verrin", None))
        self.cylinderButton.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 l'origine", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Bol \u00e0 citron", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Plateau Y", None))
        self.yStepperButton.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 l'origine", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Pile glace", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Rampe \u00e0 citron", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Soft 1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Soft 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Soft 3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soft 4", None))
        self.ledStripColorButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Vitesse", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Couleur", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"LedStrip", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Luminosit\u00e9", None))
        self.rightButtonControl.setText("")
        self.leftButtonControl.setText("")
        self.titleParameter.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.toolButtonParameterPage.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButtonBottleParameter.setText(QCoreApplication.translate("MainWindow", u"     Bouteilles", None))
        self.pushButtonSoftParameter.setText(QCoreApplication.translate("MainWindow", u"   Soft", None))
        self.pushButtonMachineParameter.setText(QCoreApplication.translate("MainWindow", u"  Machine", None))
    # retranslateUi

