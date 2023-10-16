# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPageESYOZf.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1748, 889)
        MainWindow.setMinimumSize(QSize(0, 224))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#mainBodyContainer{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#mainBodyContainer #headerContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#nouvelleOperation #annulerOperationBtn, #historiqueOperations #supprimerFiltresBtn{\n"
"	padding: 5px 20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	background-color: red;\n"
"}\n"
"\n"
"#nouvelleOperation #validerOperationBtn, #historiqueOperations #validerFiltresBtn{\n"
"	padding: 5px 20px;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	backg"
                        "round-color: green;\n"
"}\n"
"\n"
"/*\n"
"Dark: #16191d\n"
"Accent_1: #1f232a\n"
"Accent_2: #2c313c\n"
"Accent_3: #343b47\n"
"Text_1: #fff\n"
"Text_2: #838ea2\n"
"*/\n"
"\n"
"QTextEdit, QLineEdit, QComboBox, QDoubleSpinBox, QDateEdit{\n"
"	background-color: #16191d;\n"
"	border: 1px solid #343b47;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(icons/chevron-down.svg);\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 3px solid #343b47;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0, 0, 0, 10%);\n"
"	padding: 5px;\n"
"	background-color: #16191d;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left: 5px;\n"
"	background_color: #16191d;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover{\n"
"	background-color: #343b47;\n"
"}\n"
"\n"
"QComboBox QListView::item:selected{\n"
"	background-col"
                        "or: #343b47;\n"
"}\n"
"\n"
"QToolTip{\n"
"	background-color: #343b47;\n"
"	color: #fff; /* Ne fonctionne pas, j'ai du passer par du css directement dans le tooltip */\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_9 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setEnabled(True)
        self.menuBtn.setMinimumSize(QSize(0, 48))
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.menuBtn, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.homeBtn)

        self.nouvelleOperationBtn = QPushButton(self.frame_2)
        self.nouvelleOperationBtn.setObjectName(u"nouvelleOperationBtn")
        self.nouvelleOperationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nouvelleOperationBtn.setIcon(icon2)
        self.nouvelleOperationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.nouvelleOperationBtn)

        self.historiqueOperationBtn = QPushButton(self.frame_2)
        self.historiqueOperationBtn.setObjectName(u"historiqueOperationBtn")
        self.historiqueOperationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.historiqueOperationBtn.setIcon(icon3)
        self.historiqueOperationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.historiqueOperationBtn)


        self.verticalLayout_9.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 10, 0, 10)
        self.parametreBtn = QPushButton(self.frame_3)
        self.parametreBtn.setObjectName(u"parametreBtn")
        self.parametreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.parametreBtn.setIcon(icon4)
        self.parametreBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.parametreBtn)


        self.verticalLayout_9.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMinimumSize(QSize(0, 58))
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 40))
        self.label.setPixmap(QPixmap(u"logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.minimizeBtn = QPushButton(self.frame_5)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon5)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimizeBtn)

        self.fullScreenBtn = QPushButton(self.frame_5)
        self.fullScreenBtn.setObjectName(u"fullScreenBtn")
        self.fullScreenBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fullScreenBtn.setIcon(icon6)
        self.fullScreenBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.fullScreenBtn)

        self.closeBtn = QPushButton(self.frame_5)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon7)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 0)
        self.mainPages = QStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.accueil = QWidget()
        self.accueil.setObjectName(u"accueil")
        self.horizontalLayout_11 = QHBoxLayout(self.accueil)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.accueilLeftContainer = QWidget(self.accueil)
        self.accueilLeftContainer.setObjectName(u"accueilLeftContainer")
        self.verticalLayout_13 = QVBoxLayout(self.accueilLeftContainer)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(50, 50, 0, 0)
        self.soldeContainer = QWidget(self.accueilLeftContainer)
        self.soldeContainer.setObjectName(u"soldeContainer")
        self.horizontalLayout_12 = QHBoxLayout(self.soldeContainer)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 20)
        self.soldeLabel = QLabel(self.soldeContainer)
        self.soldeLabel.setObjectName(u"soldeLabel")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.soldeLabel.setFont(font1)

        self.horizontalLayout_12.addWidget(self.soldeLabel)

        self.soldeMontant = QLabel(self.soldeContainer)
        self.soldeMontant.setObjectName(u"soldeMontant")
        font2 = QFont()
        font2.setPointSize(16)
        self.soldeMontant.setFont(font2)

        self.horizontalLayout_12.addWidget(self.soldeMontant)


        self.verticalLayout_13.addWidget(self.soldeContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.soldePrevisionnelContainer = QWidget(self.accueilLeftContainer)
        self.soldePrevisionnelContainer.setObjectName(u"soldePrevisionnelContainer")
        self.horizontalLayout_13 = QHBoxLayout(self.soldePrevisionnelContainer)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.soldePrevisionnelLabel = QLabel(self.soldePrevisionnelContainer)
        self.soldePrevisionnelLabel.setObjectName(u"soldePrevisionnelLabel")
        self.soldePrevisionnelLabel.setFont(font1)

        self.horizontalLayout_13.addWidget(self.soldePrevisionnelLabel)

        self.soldePrevisionnelMontant = QLabel(self.soldePrevisionnelContainer)
        self.soldePrevisionnelMontant.setObjectName(u"soldePrevisionnelMontant")
        self.soldePrevisionnelMontant.setFont(font2)

        self.horizontalLayout_13.addWidget(self.soldePrevisionnelMontant)


        self.verticalLayout_13.addWidget(self.soldePrevisionnelContainer, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.accueilLeftContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.accueilRightContainer = QWidget(self.accueil)
        self.accueilRightContainer.setObjectName(u"accueilRightContainer")
        sizePolicy1.setHeightForWidth(self.accueilRightContainer.sizePolicy().hasHeightForWidth())
        self.accueilRightContainer.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.accueilRightContainer)

        self.mainPages.addWidget(self.accueil)
        self.nouvelleOperation = QWidget()
        self.nouvelleOperation.setObjectName(u"nouvelleOperation")
        self.nouvelleOperation.setMinimumSize(QSize(459, 532))
        self.verticalLayout_12 = QVBoxLayout(self.nouvelleOperation)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.nouvelleOperationContainer = QWidget(self.nouvelleOperation)
        self.nouvelleOperationContainer.setObjectName(u"nouvelleOperationContainer")
        self.verticalLayout_5 = QVBoxLayout(self.nouvelleOperationContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titreNouvelleOperation = QLabel(self.nouvelleOperationContainer)
        self.titreNouvelleOperation.setObjectName(u"titreNouvelleOperation")
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.titreNouvelleOperation.setFont(font3)

        self.verticalLayout_5.addWidget(self.titreNouvelleOperation)

        self.TypeOperationContainer = QWidget(self.nouvelleOperationContainer)
        self.TypeOperationContainer.setObjectName(u"TypeOperationContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.TypeOperationContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 40, 0, 20)
        self.typeOperationLabel = QLabel(self.TypeOperationContainer)
        self.typeOperationLabel.setObjectName(u"typeOperationLabel")
        self.typeOperationLabel.setFont(font2)

        self.horizontalLayout_6.addWidget(self.typeOperationLabel, 0, Qt.AlignLeft)

        self.typeOperationInput = QComboBox(self.TypeOperationContainer)
        self.typeOperationInput.addItem("")
        self.typeOperationInput.addItem("")
        self.typeOperationInput.setObjectName(u"typeOperationInput")
        sizePolicy.setHeightForWidth(self.typeOperationInput.sizePolicy().hasHeightForWidth())
        self.typeOperationInput.setSizePolicy(sizePolicy)
        self.typeOperationInput.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.typeOperationInput)


        self.verticalLayout_5.addWidget(self.TypeOperationContainer)

        self.etatOperationContainer = QWidget(self.nouvelleOperationContainer)
        self.etatOperationContainer.setObjectName(u"etatOperationContainer")
        self.horizontalLayout_7 = QHBoxLayout(self.etatOperationContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.etatOperationLabel = QLabel(self.etatOperationContainer)
        self.etatOperationLabel.setObjectName(u"etatOperationLabel")
        self.etatOperationLabel.setFont(font2)

        self.horizontalLayout_7.addWidget(self.etatOperationLabel, 0, Qt.AlignLeft)

        self.etatOperationInput = QComboBox(self.etatOperationContainer)
        self.etatOperationInput.addItem("")
        self.etatOperationInput.addItem("")
        self.etatOperationInput.setObjectName(u"etatOperationInput")
        sizePolicy.setHeightForWidth(self.etatOperationInput.sizePolicy().hasHeightForWidth())
        self.etatOperationInput.setSizePolicy(sizePolicy)
        self.etatOperationInput.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_7.addWidget(self.etatOperationInput)


        self.verticalLayout_5.addWidget(self.etatOperationContainer)

        self.montantOperationContainer = QWidget(self.nouvelleOperationContainer)
        self.montantOperationContainer.setObjectName(u"montantOperationContainer")
        self.horizontalLayout_9 = QHBoxLayout(self.montantOperationContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 20)
        self.montantOperationLabel = QLabel(self.montantOperationContainer)
        self.montantOperationLabel.setObjectName(u"montantOperationLabel")
        self.montantOperationLabel.setFont(font2)

        self.horizontalLayout_9.addWidget(self.montantOperationLabel, 0, Qt.AlignLeft)

        self.montantOperationInput = QDoubleSpinBox(self.montantOperationContainer)
        self.montantOperationInput.setObjectName(u"montantOperationInput")
        sizePolicy.setHeightForWidth(self.montantOperationInput.sizePolicy().hasHeightForWidth())
        self.montantOperationInput.setSizePolicy(sizePolicy)
        self.montantOperationInput.setMinimumSize(QSize(200, 0))
        self.montantOperationInput.setMaximum(1000000000000000000000.000000000000000)

        self.horizontalLayout_9.addWidget(self.montantOperationInput)


        self.verticalLayout_5.addWidget(self.montantOperationContainer)

        self.libelleOperationContainer = QWidget(self.nouvelleOperationContainer)
        self.libelleOperationContainer.setObjectName(u"libelleOperationContainer")
        self.horizontalLayout_8 = QHBoxLayout(self.libelleOperationContainer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 40)
        self.libelleOperationLabel = QLabel(self.libelleOperationContainer)
        self.libelleOperationLabel.setObjectName(u"libelleOperationLabel")
        self.libelleOperationLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.libelleOperationLabel, 0, Qt.AlignLeft|Qt.AlignTop)

        self.libelleOperationInput = QTextEdit(self.libelleOperationContainer)
        self.libelleOperationInput.setObjectName(u"libelleOperationInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.libelleOperationInput.sizePolicy().hasHeightForWidth())
        self.libelleOperationInput.setSizePolicy(sizePolicy3)
        self.libelleOperationInput.setMinimumSize(QSize(200, 40))
        self.libelleOperationInput.setMaximumSize(QSize(600, 200))

        self.horizontalLayout_8.addWidget(self.libelleOperationInput, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.libelleOperationContainer)

        self.boutonOperationContainer = QWidget(self.nouvelleOperationContainer)
        self.boutonOperationContainer.setObjectName(u"boutonOperationContainer")
        self.horizontalLayout_10 = QHBoxLayout(self.boutonOperationContainer)
        self.horizontalLayout_10.setSpacing(70)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.annulerOperationBtn = QPushButton(self.boutonOperationContainer)
        self.annulerOperationBtn.setObjectName(u"annulerOperationBtn")
        self.annulerOperationBtn.setMinimumSize(QSize(113, 38))
        self.annulerOperationBtn.setFont(font2)
        self.annulerOperationBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.annulerOperationBtn)

        self.validerOperationBtn = QPushButton(self.boutonOperationContainer)
        self.validerOperationBtn.setObjectName(u"validerOperationBtn")
        self.validerOperationBtn.setMinimumSize(QSize(113, 38))
        self.validerOperationBtn.setFont(font2)
        self.validerOperationBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.validerOperationBtn)


        self.verticalLayout_5.addWidget(self.boutonOperationContainer, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.nouvelleOperationContainer, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.nouvelleOperation)
        self.historiqueOperations = QWidget()
        self.historiqueOperations.setObjectName(u"historiqueOperations")
        self.horizontalLayout_14 = QHBoxLayout(self.historiqueOperations)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.historiqueOperationContainer = QWidget(self.historiqueOperations)
        self.historiqueOperationContainer.setObjectName(u"historiqueOperationContainer")
        self.verticalLayout_6 = QVBoxLayout(self.historiqueOperationContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.titreHistoriqueOperation = QLabel(self.historiqueOperationContainer)
        self.titreHistoriqueOperation.setObjectName(u"titreHistoriqueOperation")
        self.titreHistoriqueOperation.setFont(font3)

        self.verticalLayout_6.addWidget(self.titreHistoriqueOperation, 0, Qt.AlignHCenter)

        self.filtreContainer = QWidget(self.historiqueOperationContainer)
        self.filtreContainer.setObjectName(u"filtreContainer")
        self.horizontalLayout_15 = QHBoxLayout(self.filtreContainer)
        self.horizontalLayout_15.setSpacing(40)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 40, 0, 40)
        self.filtreLabel = QLabel(self.filtreContainer)
        self.filtreLabel.setObjectName(u"filtreLabel")
        self.filtreLabel.setFont(font1)

        self.horizontalLayout_15.addWidget(self.filtreLabel, 0, Qt.AlignBottom)

        self.filtreDateContainer = QWidget(self.filtreContainer)
        self.filtreDateContainer.setObjectName(u"filtreDateContainer")
        self.verticalLayout_14 = QVBoxLayout(self.filtreDateContainer)
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.filtreDateLabel = QLabel(self.filtreDateContainer)
        self.filtreDateLabel.setObjectName(u"filtreDateLabel")
        self.filtreDateLabel.setFont(font1)

        self.verticalLayout_14.addWidget(self.filtreDateLabel)

        self.filtreDateInput = QDateEdit(self.filtreDateContainer)
        self.filtreDateInput.setObjectName(u"filtreDateInput")
        self.filtreDateInput.setCalendarPopup(True)
        self.filtreDateInput.setDate(QDate(2000, 1, 1))

        self.verticalLayout_14.addWidget(self.filtreDateInput)


        self.horizontalLayout_15.addWidget(self.filtreDateContainer)

        self.filtreEtatContainer = QWidget(self.filtreContainer)
        self.filtreEtatContainer.setObjectName(u"filtreEtatContainer")
        self.verticalLayout_16 = QVBoxLayout(self.filtreEtatContainer)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.filtreEtatLabel = QLabel(self.filtreEtatContainer)
        self.filtreEtatLabel.setObjectName(u"filtreEtatLabel")
        self.filtreEtatLabel.setFont(font1)

        self.verticalLayout_16.addWidget(self.filtreEtatLabel)

        self.filtreEtatInput = QComboBox(self.filtreEtatContainer)
        self.filtreEtatInput.addItem("")
        self.filtreEtatInput.addItem("")
        self.filtreEtatInput.addItem("")
        self.filtreEtatInput.addItem("")
        self.filtreEtatInput.setObjectName(u"filtreEtatInput")

        self.verticalLayout_16.addWidget(self.filtreEtatInput)


        self.horizontalLayout_15.addWidget(self.filtreEtatContainer)

        self.filtreMontantContainer = QWidget(self.filtreContainer)
        self.filtreMontantContainer.setObjectName(u"filtreMontantContainer")
        self.verticalLayout_15 = QVBoxLayout(self.filtreMontantContainer)
        self.verticalLayout_15.setSpacing(20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.filtreMontantLabel = QLabel(self.filtreMontantContainer)
        self.filtreMontantLabel.setObjectName(u"filtreMontantLabel")
        self.filtreMontantLabel.setFont(font1)

        self.verticalLayout_15.addWidget(self.filtreMontantLabel)

        self.filtreMontantInput = QDoubleSpinBox(self.filtreMontantContainer)
        self.filtreMontantInput.setObjectName(u"filtreMontantInput")
        self.filtreMontantInput.setMaximum(100000000000000004764729344.000000000000000)

        self.verticalLayout_15.addWidget(self.filtreMontantInput)


        self.horizontalLayout_15.addWidget(self.filtreMontantContainer)

        self.filtreLibelleContainer = QWidget(self.filtreContainer)
        self.filtreLibelleContainer.setObjectName(u"filtreLibelleContainer")
        self.verticalLayout_4 = QVBoxLayout(self.filtreLibelleContainer)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.filtreLibelleLabel = QLabel(self.filtreLibelleContainer)
        self.filtreLibelleLabel.setObjectName(u"filtreLibelleLabel")
        self.filtreLibelleLabel.setFont(font1)

        self.verticalLayout_4.addWidget(self.filtreLibelleLabel)

        self.filtreLibelleInput = QLineEdit(self.filtreLibelleContainer)
        self.filtreLibelleInput.setObjectName(u"filtreLibelleInput")

        self.verticalLayout_4.addWidget(self.filtreLibelleInput)


        self.horizontalLayout_15.addWidget(self.filtreLibelleContainer)


        self.verticalLayout_6.addWidget(self.filtreContainer)

        self.boutonsFiltresContainer = QWidget(self.historiqueOperationContainer)
        self.boutonsFiltresContainer.setObjectName(u"boutonsFiltresContainer")
        self.horizontalLayout_16 = QHBoxLayout(self.boutonsFiltresContainer)
        self.horizontalLayout_16.setSpacing(70)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 40)
        self.supprimerFiltresBtn = QPushButton(self.boutonsFiltresContainer)
        self.supprimerFiltresBtn.setObjectName(u"supprimerFiltresBtn")
        self.supprimerFiltresBtn.setFont(font2)
        self.supprimerFiltresBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.supprimerFiltresBtn)

        self.validerFiltresBtn = QPushButton(self.boutonsFiltresContainer)
        self.validerFiltresBtn.setObjectName(u"validerFiltresBtn")
        self.validerFiltresBtn.setMinimumSize(QSize(223, 0))
        self.validerFiltresBtn.setFont(font2)
        self.validerFiltresBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.validerFiltresBtn)


        self.verticalLayout_6.addWidget(self.boutonsFiltresContainer, 0, Qt.AlignHCenter)

        self.tableauHistoriqueOperations = QTableWidget(self.historiqueOperationContainer)
        if (self.tableauHistoriqueOperations.columnCount() < 6):
            self.tableauHistoriqueOperations.setColumnCount(6)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem.setForeground(brush);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem1.setForeground(brush1);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem2.setForeground(brush2);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem3.setForeground(brush3);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem4.setForeground(brush4);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setBackground(QColor(22, 25, 29));
        __qtablewidgetitem5.setForeground(brush5);
        self.tableauHistoriqueOperations.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableauHistoriqueOperations.setObjectName(u"tableauHistoriqueOperations")
        self.tableauHistoriqueOperations.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableauHistoriqueOperations.setSortingEnabled(True)
        self.tableauHistoriqueOperations.horizontalHeader().setCascadingSectionResizes(True)
        self.tableauHistoriqueOperations.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableauHistoriqueOperations.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tableauHistoriqueOperations)


        self.horizontalLayout_14.addWidget(self.historiqueOperationContainer, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.historiqueOperations)
        self.parametres = QWidget()
        self.parametres.setObjectName(u"parametres")
        self.verticalLayout_7 = QVBoxLayout(self.parametres)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.parametres)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.mainPages.addWidget(self.parametres)

        self.verticalLayout_3.addWidget(self.mainPages)


        self.verticalLayout_2.addWidget(self.mainBodyContent)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.verticalLayout_8 = QVBoxLayout(self.footerContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.footerContainer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Menu</font>", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Accueil</font>", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
#if QT_CONFIG(tooltip)
        self.nouvelleOperationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Nouvelle op\u00e9ration</font>", None))
#endif // QT_CONFIG(tooltip)
        self.nouvelleOperationBtn.setText(QCoreApplication.translate("MainWindow", u"Nouvelle op\u00e9ration", None))
#if QT_CONFIG(tooltip)
        self.historiqueOperationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Historique des op\u00e9rations</font>", None))
#endif // QT_CONFIG(tooltip)
        self.historiqueOperationBtn.setText(QCoreApplication.translate("MainWindow", u"Historique des op\u00e9rations", None))
#if QT_CONFIG(tooltip)
        self.parametreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Param\u00e8tres</font>", None))
#endif // QT_CONFIG(tooltip)
        self.parametreBtn.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Application comptable", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Minimiser la page</font>", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.fullScreenBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Mettre la page en plein \u00e9cran</font>", None))
#endif // QT_CONFIG(tooltip)
        self.fullScreenBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<font color=\"white\">Fermer la page</font>", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.soldeLabel.setText(QCoreApplication.translate("MainWindow", u"Solde:", None))
        self.soldeMontant.setText(QCoreApplication.translate("MainWindow", u"0 \u20ac", None))
        self.soldePrevisionnelLabel.setText(QCoreApplication.translate("MainWindow", u"Solde pr\u00e9visionnel:", None))
        self.soldePrevisionnelMontant.setText(QCoreApplication.translate("MainWindow", u"0 \u20ac", None))
        self.titreNouvelleOperation.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer une nouvelle op\u00e9ration", None))
        self.typeOperationLabel.setText(QCoreApplication.translate("MainWindow", u"Type d'op\u00e9ration:", None))
        self.typeOperationInput.setItemText(0, QCoreApplication.translate("MainWindow", u"DEBIT", None))
        self.typeOperationInput.setItemText(1, QCoreApplication.translate("MainWindow", u"CREDIT", None))

        self.etatOperationLabel.setText(QCoreApplication.translate("MainWindow", u"Etat de l'op\u00e9ration:", None))
        self.etatOperationInput.setItemText(0, QCoreApplication.translate("MainWindow", u"EN ATTENTE", None))
        self.etatOperationInput.setItemText(1, QCoreApplication.translate("MainWindow", u"ACCEPTEE", None))

        self.montantOperationLabel.setText(QCoreApplication.translate("MainWindow", u"Montant:", None))
        self.montantOperationInput.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self.libelleOperationLabel.setText(QCoreApplication.translate("MainWindow", u"Libelle de l'op\u00e9ration:", None))
        self.annulerOperationBtn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.validerOperationBtn.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.titreHistoriqueOperation.setText(QCoreApplication.translate("MainWindow", u"HISTORIQUE DES OPERATIONS", None))
        self.filtreLabel.setText(QCoreApplication.translate("MainWindow", u"Filtres:", None))
        self.filtreDateLabel.setText(QCoreApplication.translate("MainWindow", u"Entrez une date:", None))
        self.filtreEtatLabel.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionner un \u00e9tat:", None))
        self.filtreEtatInput.setItemText(0, "")
        self.filtreEtatInput.setItemText(1, QCoreApplication.translate("MainWindow", u"ACCEPTEE", None))
        self.filtreEtatInput.setItemText(2, QCoreApplication.translate("MainWindow", u"REFUSEE", None))
        self.filtreEtatInput.setItemText(3, QCoreApplication.translate("MainWindow", u"EN ATTENTE", None))

        self.filtreMontantLabel.setText(QCoreApplication.translate("MainWindow", u"Entrez un montant:", None))
        self.filtreMontantInput.setSuffix(QCoreApplication.translate("MainWindow", u" \u20ac", None))
        self.filtreLibelleLabel.setText(QCoreApplication.translate("MainWindow", u"Recherche dans le libelle:", None))
        self.supprimerFiltresBtn.setText(QCoreApplication.translate("MainWindow", u"Supprimer les filtres", None))
        self.validerFiltresBtn.setText(QCoreApplication.translate("MainWindow", u"Valider les filtres", None))
        ___qtablewidgetitem = self.tableauHistoriqueOperations.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Horodatage", None));
        ___qtablewidgetitem1 = self.tableauHistoriqueOperations.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableauHistoriqueOperations.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Etat", None));
        ___qtablewidgetitem3 = self.tableauHistoriqueOperations.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"D\u00e9bit", None));
        ___qtablewidgetitem4 = self.tableauHistoriqueOperations.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9dit", None));
        ___qtablewidgetitem5 = self.tableauHistoriqueOperations.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Libelle", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PARAMETRES", None))
    # retranslateUi

