# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 480))
        self.entryScreen = QWidget()
        self.entryScreen.setObjectName(u"entryScreen")
        self.entryScreen.setStyleSheet(u"")
        self.loginButton = QPushButton(self.entryScreen)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(120, 260, 251, 141))
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet(u"background-color: rgb(78, 131, 255);")
        self.registerButton = QPushButton(self.entryScreen)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(430, 260, 251, 141))
        font1 = QFont()
        font1.setPointSize(38)
        font1.setBold(True)
        self.registerButton.setFont(font1)
        self.registerButton.setStyleSheet(u"background-color: rgb(78, 131, 255);")
        self.label = QLabel(self.entryScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 800, 480))
        self.label.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/entryScreen.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.powerOffButton = QPushButton(self.entryScreen)
        self.powerOffButton.setObjectName(u"powerOffButton")
        self.powerOffButton.setGeometry(QRect(0, 0, 131, 111))
        self.powerOffButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        icon = QIcon()
        icon.addFile(u"Assets/powerOffButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.powerOffButton.setIcon(icon)
        self.powerOffButton.setIconSize(QSize(64, 64))
        self.stackedWidget.addWidget(self.entryScreen)
        self.label.raise_()
        self.loginButton.raise_()
        self.registerButton.raise_()
        self.powerOffButton.raise_()
        self.loginScreen = QWidget()
        self.loginScreen.setObjectName(u"loginScreen")
        self.label_2 = QLabel(self.loginScreen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 800, 480))
        self.label_2.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.verticalLayoutWidget_2 = QWidget(self.loginScreen)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(230, 170, 321, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.usernameLoginInput = QLineEdit(self.verticalLayoutWidget_2)
        self.usernameLoginInput.setObjectName(u"usernameLoginInput")

        self.verticalLayout_2.addWidget(self.usernameLoginInput)

        self.passwordLoginInput = QLineEdit(self.verticalLayoutWidget_2)
        self.passwordLoginInput.setObjectName(u"passwordLoginInput")

        self.verticalLayout_2.addWidget(self.passwordLoginInput)

        self.loginSubmitButton = QPushButton(self.verticalLayoutWidget_2)
        self.loginSubmitButton.setObjectName(u"loginSubmitButton")

        self.verticalLayout_2.addWidget(self.loginSubmitButton)

        self.backButtonLogin = QPushButton(self.verticalLayoutWidget_2)
        self.backButtonLogin.setObjectName(u"backButtonLogin")

        self.verticalLayout_2.addWidget(self.backButtonLogin)

        self.powerOffButtonLogin = QPushButton(self.loginScreen)
        self.powerOffButtonLogin.setObjectName(u"powerOffButtonLogin")
        self.powerOffButtonLogin.setGeometry(QRect(0, 0, 131, 111))
        self.powerOffButtonLogin.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.powerOffButtonLogin.setIcon(icon)
        self.powerOffButtonLogin.setIconSize(QSize(64, 64))
        self.stackedWidget.addWidget(self.loginScreen)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.label_4 = QLabel(self.Dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 800, 480))
        self.label_4.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.powerOffButtonDashboard = QPushButton(self.Dashboard)
        self.powerOffButtonDashboard.setObjectName(u"powerOffButtonDashboard")
        self.powerOffButtonDashboard.setGeometry(QRect(0, 0, 131, 111))
        self.powerOffButtonDashboard.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"    border: none;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.powerOffButtonDashboard.setIcon(icon)
        self.powerOffButtonDashboard.setIconSize(QSize(64, 64))
        self.notificationButton = QPushButton(self.Dashboard)
        self.notificationButton.setObjectName(u"notificationButton")
        self.notificationButton.setGeometry(QRect(720, 0, 80, 80))
        self.notificationButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"Assets/notificationsButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationButton.setIcon(icon1)
        self.notificationButton.setIconSize(QSize(64, 64))
        self.resultsButton = QPushButton(self.Dashboard)
        self.resultsButton.setObjectName(u"resultsButton")
        self.resultsButton.setGeometry(QRect(720, 80, 80, 80))
        self.resultsButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Assets/resultsButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resultsButton.setIcon(icon2)
        self.resultsButton.setIconSize(QSize(64, 64))
        self.logoffButton = QPushButton(self.Dashboard)
        self.logoffButton.setObjectName(u"logoffButton")
        self.logoffButton.setGeometry(QRect(720, 350, 80, 80))
        self.logoffButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Assets/logoffButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoffButton.setIcon(icon3)
        self.logoffButton.setIconSize(QSize(64, 64))
        self.sampleButton = QPushButton(self.Dashboard)
        self.sampleButton.setObjectName(u"sampleButton")
        self.sampleButton.setGeometry(QRect(720, 160, 80, 80))
        self.sampleButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Assets/sampleButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sampleButton.setIcon(icon4)
        self.sampleButton.setIconSize(QSize(64, 64))
        self.notificationCountLabel = QLabel(self.Dashboard)
        self.notificationCountLabel.setObjectName(u"notificationCountLabel")
        self.notificationCountLabel.setGeometry(QRect(721, 0, 32, 32))
        self.notificationCountLabel.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;\n"
"    background-color: red;\n"
"    color: white;            /* Makes text white for contrast */\n"
"    border-radius: 16px;     /* Half of width/height = circle */\n"
"    min-width: 32px;\n"
"    min-height: 32px;\n"
"    max-width: 32px;\n"
"    max-height: 32px;\n"
"    qproperty-alignment: 'AlignCenter'; /* Optional, for centering */\n"
"}\n"
"")
        self.notificationCountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tomoFace = QLabel(self.Dashboard)
        self.tomoFace.setObjectName(u"tomoFace")
        self.tomoFace.setGeometry(QRect(0, 0, 800, 480))
        self.pairWatchButton = QPushButton(self.Dashboard)
        self.pairWatchButton.setObjectName(u"pairWatchButton")
        self.pairWatchButton.setGeometry(QRect(130, 20, 221, 71))
        font2 = QFont()
        font2.setPointSize(21)
        font2.setBold(True)
        self.pairWatchButton.setFont(font2)
        self.pairWatchButton.setStyleSheet(u"QObject {\n"
"    background: transparent;\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 12px;  /* Adjust px for more/less roundness */\n"
"}\n"
"\n"
"QObject:hover {\n"
"    background: #376487;  /* Darker blue */\n"
"    color: black;\n"
"    border-radius: 12px;\n"
"}\n"
"")
        self.heartRateButton = QPushButton(self.Dashboard)
        self.heartRateButton.setObjectName(u"heartRateButton")
        self.heartRateButton.setGeometry(QRect(720, 260, 80, 80))
        self.heartRateButton.setStyleSheet(u"QPushButton{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"Assets/heartRate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.heartRateButton.setIcon(icon5)
        self.heartRateButton.setIconSize(QSize(64, 64))
        self.stackedWidget.addWidget(self.Dashboard)
        self.label_4.raise_()
        self.tomoFace.raise_()
        self.powerOffButtonDashboard.raise_()
        self.logoffButton.raise_()
        self.notificationButton.raise_()
        self.resultsButton.raise_()
        self.sampleButton.raise_()
        self.notificationCountLabel.raise_()
        self.pairWatchButton.raise_()
        self.heartRateButton.raise_()
        self.heartRatePage = QWidget()
        self.heartRatePage.setObjectName(u"heartRatePage")
        self.label_24 = QLabel(self.heartRatePage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 800, 480))
        self.label_24.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.heartRateBackButton = QPushButton(self.heartRatePage)
        self.heartRateBackButton.setObjectName(u"heartRateBackButton")
        self.heartRateBackButton.setGeometry(QRect(720, 0, 80, 80))
        self.heartRateBackButton.setStyleSheet(u"QPushButton{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"Assets/backButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.heartRateBackButton.setIcon(icon6)
        self.heartRateBackButton.setIconSize(QSize(64, 64))
        self.heartRateGraph = QLabel(self.heartRatePage)
        self.heartRateGraph.setObjectName(u"heartRateGraph")
        self.heartRateGraph.setGeometry(QRect(30, 10, 671, 451))
        font3 = QFont()
        font3.setBold(True)
        self.heartRateGraph.setFont(font3)
        self.heartRateGraph.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.heartRatePage)
        self.newSensorPage = QWidget()
        self.newSensorPage.setObjectName(u"newSensorPage")
        self.label_28 = QLabel(self.newSensorPage)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 800, 480))
        self.label_28.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"")
        self.addSensorBackButton = QPushButton(self.newSensorPage)
        self.addSensorBackButton.setObjectName(u"addSensorBackButton")
        self.addSensorBackButton.setGeometry(QRect(720, 0, 80, 80))
        self.addSensorBackButton.setIcon(icon6)
        self.addSensorBackButton.setIconSize(QSize(64, 64))
        self.addSensorCamera = QLabel(self.newSensorPage)
        self.addSensorCamera.setObjectName(u"addSensorCamera")
        self.addSensorCamera.setGeometry(QRect(10, 10, 521, 351))
        self.addSensorAdd = QPushButton(self.newSensorPage)
        self.addSensorAdd.setObjectName(u"addSensorAdd")
        self.addSensorAdd.setGeometry(QRect(570, 190, 80, 24))
        self.addSensorLineEdit = QLineEdit(self.newSensorPage)
        self.addSensorLineEdit.setObjectName(u"addSensorLineEdit")
        self.addSensorLineEdit.setGeometry(QRect(560, 160, 113, 24))
        self.finalAddButton = QPushButton(self.newSensorPage)
        self.finalAddButton.setObjectName(u"finalAddButton")
        self.finalAddButton.setGeometry(QRect(570, 240, 80, 24))
        self.RGBLabel = QLabel(self.newSensorPage)
        self.RGBLabel.setObjectName(u"RGBLabel")
        self.RGBLabel.setGeometry(QRect(560, 300, 111, 121))
        self.RGBLabel.setWordWrap(True)
        self.stackedWidget.addWidget(self.newSensorPage)
        self.watchPairingPage = QWidget()
        self.watchPairingPage.setObjectName(u"watchPairingPage")
        self.label_26 = QLabel(self.watchPairingPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 800, 480))
        self.label_26.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.pairBackButton = QPushButton(self.watchPairingPage)
        self.pairBackButton.setObjectName(u"pairBackButton")
        self.pairBackButton.setGeometry(QRect(720, 0, 80, 80))
        self.pairBackButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.pairBackButton.setIcon(icon6)
        self.pairBackButton.setIconSize(QSize(64, 64))
        self.pairLineEdit = QLineEdit(self.watchPairingPage)
        self.pairLineEdit.setObjectName(u"pairLineEdit")
        self.pairLineEdit.setGeometry(QRect(120, 110, 501, 24))
        self.pairButton = QPushButton(self.watchPairingPage)
        self.pairButton.setObjectName(u"pairButton")
        self.pairButton.setGeometry(QRect(330, 170, 80, 24))
        self.stackedWidget.addWidget(self.watchPairingPage)
        self.notificationPage = QWidget()
        self.notificationPage.setObjectName(u"notificationPage")
        self.label_5 = QLabel(self.notificationPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 800, 480))
        self.label_5.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.homeButtonNotificationPage = QPushButton(self.notificationPage)
        self.homeButtonNotificationPage.setObjectName(u"homeButtonNotificationPage")
        self.homeButtonNotificationPage.setGeometry(QRect(720, 0, 80, 80))
        self.homeButtonNotificationPage.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"Assets/homeButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButtonNotificationPage.setIcon(icon7)
        self.homeButtonNotificationPage.setIconSize(QSize(64, 64))
        self.resultsButtonNotificationPage = QPushButton(self.notificationPage)
        self.resultsButtonNotificationPage.setObjectName(u"resultsButtonNotificationPage")
        self.resultsButtonNotificationPage.setGeometry(QRect(720, 80, 80, 80))
        self.resultsButtonNotificationPage.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.resultsButtonNotificationPage.setIcon(icon2)
        self.resultsButtonNotificationPage.setIconSize(QSize(64, 64))
        self.logoffButtonNotificationPage = QPushButton(self.notificationPage)
        self.logoffButtonNotificationPage.setObjectName(u"logoffButtonNotificationPage")
        self.logoffButtonNotificationPage.setGeometry(QRect(720, 160, 80, 80))
        self.logoffButtonNotificationPage.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.logoffButtonNotificationPage.setIcon(icon3)
        self.logoffButtonNotificationPage.setIconSize(QSize(64, 64))
        self.powerOffButtonNotificationPage = QPushButton(self.notificationPage)
        self.powerOffButtonNotificationPage.setObjectName(u"powerOffButtonNotificationPage")
        self.powerOffButtonNotificationPage.setGeometry(QRect(0, 0, 80, 80))
        self.powerOffButtonNotificationPage.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.powerOffButtonNotificationPage.setIcon(icon)
        self.powerOffButtonNotificationPage.setIconSize(QSize(64, 64))
        self.notificationsScrollArea = QScrollArea(self.notificationPage)
        self.notificationsScrollArea.setObjectName(u"notificationsScrollArea")
        self.notificationsScrollArea.setGeometry(QRect(80, 0, 631, 471))
        self.notificationsScrollArea.setStyleSheet(u"QScrollArea{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.notificationsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notificationsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notificationsScrollArea.setWidgetResizable(True)
        self.notificationsScrollAreaWidgetContents = QWidget()
        self.notificationsScrollAreaWidgetContents.setObjectName(u"notificationsScrollAreaWidgetContents")
        self.notificationsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 631, 471))
        self.notificationsScrollAreaWidgetContents.setStyleSheet(u"QWidget{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.notificationsScrollArea.setWidget(self.notificationsScrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.notificationPage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.tabWidget = QTabWidget(self.resultsPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 720, 480))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.Results = QWidget()
        self.Results.setObjectName(u"Results")
        self.Results.setStyleSheet(u"QWidget {\n"
"        background: transparent;\n"
"		border: none;\n"
"    }")
        self.resultsScrollArea = QScrollArea(self.Results)
        self.resultsScrollArea.setObjectName(u"resultsScrollArea")
        self.resultsScrollArea.setGeometry(QRect(0, 0, 711, 451))
        self.resultsScrollArea.setStyleSheet(u"QScrollArea {\n"
"        background: transparent;\n"
"        border: none;\n"
"    }")
        self.resultsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.resultsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.resultsScrollArea.setWidgetResizable(True)
        self.resultsScrollAreaWidgetContents = QWidget()
        self.resultsScrollAreaWidgetContents.setObjectName(u"resultsScrollAreaWidgetContents")
        self.resultsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 711, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsScrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.resultsScrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.resultsScrollAreaWidgetContents.setMinimumSize(QSize(709, 0))
        self.resultsScrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"        background: transparent;\n"
"    }")
        self.verticalLayout_4 = QVBoxLayout(self.resultsScrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.resultsScrollArea.setWidget(self.resultsScrollAreaWidgetContents)
        self.tabWidget.addTab(self.Results, "")
        self.Notes = QWidget()
        self.Notes.setObjectName(u"Notes")
        self.Notes.setStyleSheet(u"")
        self.notesScrollArea = QScrollArea(self.Notes)
        self.notesScrollArea.setObjectName(u"notesScrollArea")
        self.notesScrollArea.setGeometry(QRect(0, 0, 711, 441))
        self.notesScrollArea.setStyleSheet(u"")
        self.notesScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.notesScrollArea.setWidgetResizable(True)
        self.notesScrollAreaWidgetContents = QWidget()
        self.notesScrollAreaWidgetContents.setObjectName(u"notesScrollAreaWidgetContents")
        self.notesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 439))
        self.verticalLayout_3 = QVBoxLayout(self.notesScrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.addNoteButton = QPushButton(self.notesScrollAreaWidgetContents)
        self.addNoteButton.setObjectName(u"addNoteButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addNoteButton.sizePolicy().hasHeightForWidth())
        self.addNoteButton.setSizePolicy(sizePolicy1)
        self.addNoteButton.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"        border: none;\n"
"}\n"
"QPushButton:hover {\n"
"                background: #1976D2;\n"
"                color: white;\n"
"            }")
        icon8 = QIcon()
        icon8.addFile(u"Assets/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addNoteButton.setIcon(icon8)
        self.addNoteButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.addNoteButton)

        self.notesScrollArea.setWidget(self.notesScrollAreaWidgetContents)
        self.tabWidget.addTab(self.Notes, "")
        self.Resources = QWidget()
        self.Resources.setObjectName(u"Resources")
        self.Resources.setStyleSheet(u"QWidget {\n"
"        background: transparent;\n"
"        border: none;\n"
"    }")
        self.resourcesScrollArea = QScrollArea(self.Resources)
        self.resourcesScrollArea.setObjectName(u"resourcesScrollArea")
        self.resourcesScrollArea.setGeometry(QRect(0, 0, 711, 451))
        self.resourcesScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 711, 451))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.resourcesScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.Resources, "")
        self.homeButtonResultsPage = QPushButton(self.resultsPage)
        self.homeButtonResultsPage.setObjectName(u"homeButtonResultsPage")
        self.homeButtonResultsPage.setGeometry(QRect(720, 0, 80, 80))
        self.homeButtonResultsPage.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.homeButtonResultsPage.setIcon(icon7)
        self.homeButtonResultsPage.setIconSize(QSize(64, 64))
        self.label_16 = QLabel(self.resultsPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 800, 480))
        self.label_16.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.notificationButtonResults = QPushButton(self.resultsPage)
        self.notificationButtonResults.setObjectName(u"notificationButtonResults")
        self.notificationButtonResults.setGeometry(QRect(720, 80, 80, 80))
        self.notificationButtonResults.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.notificationButtonResults.setIcon(icon1)
        self.notificationButtonResults.setIconSize(QSize(64, 64))
        self.notificationCountLabelResults = QLabel(self.resultsPage)
        self.notificationCountLabelResults.setObjectName(u"notificationCountLabelResults")
        self.notificationCountLabelResults.setGeometry(QRect(720, 80, 32, 32))
        self.notificationCountLabelResults.setStyleSheet(u"QLabel {\n"
"    font-weight: bold;\n"
"    background-color: red;\n"
"    color: white;            /* Makes text white for contrast */\n"
"    border-radius: 16px;     /* Half of width/height = circle */\n"
"    min-width: 32px;\n"
"    min-height: 32px;\n"
"    max-width: 32px;\n"
"    max-height: 32px;\n"
"    qproperty-alignment: 'AlignCenter'; /* Optional, for centering */\n"
"}\n"
"")
        self.notificationCountLabelResults.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.resultsPage)
        self.label_16.raise_()
        self.tabWidget.raise_()
        self.homeButtonResultsPage.raise_()
        self.notificationButtonResults.raise_()
        self.notificationCountLabelResults.raise_()
        self.groundingSessionPage = QWidget()
        self.groundingSessionPage.setObjectName(u"groundingSessionPage")
        self.label_20 = QLabel(self.groundingSessionPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 800, 480))
        self.label_20.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.GroundingTitle = QLabel(self.groundingSessionPage)
        self.GroundingTitle.setObjectName(u"GroundingTitle")
        self.GroundingTitle.setGeometry(QRect(0, 0, 791, 61))
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(True)
        self.GroundingTitle.setFont(font4)
        self.GroundingTitle.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.GroundingTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groundingQuestionLabel = QLabel(self.groundingSessionPage)
        self.groundingQuestionLabel.setObjectName(u"groundingQuestionLabel")
        self.groundingQuestionLabel.setGeometry(QRect(20, 70, 771, 41))
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        self.groundingQuestionLabel.setFont(font5)
        self.groundingQuestionLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.groundingQuestionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groundingNextpushButton = QPushButton(self.groundingSessionPage)
        self.groundingNextpushButton.setObjectName(u"groundingNextpushButton")
        self.groundingNextpushButton.setGeometry(QRect(190, 360, 361, 121))
        self.verticalLayoutWidget_3 = QWidget(self.groundingSessionPage)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-1, 129, 801, 231))
        self.groundingEntry = QVBoxLayout(self.verticalLayoutWidget_3)
        self.groundingEntry.setObjectName(u"groundingEntry")
        self.groundingEntry.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.groundingSessionPage)
        self.boxBreathingPage = QWidget()
        self.boxBreathingPage.setObjectName(u"boxBreathingPage")
        self.label_22 = QLabel(self.boxBreathingPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 800, 480))
        self.label_22.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.boxBreathingBackButton = QPushButton(self.boxBreathingPage)
        self.boxBreathingBackButton.setObjectName(u"boxBreathingBackButton")
        self.boxBreathingBackButton.setGeometry(QRect(720, 0, 80, 80))
        self.boxBreathingBackButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.boxBreathingBackButton.setIcon(icon6)
        self.boxBreathingBackButton.setIconSize(QSize(64, 64))
        self.label_23 = QLabel(self.boxBreathingPage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 711, 91))
        font6 = QFont()
        font6.setPointSize(41)
        font6.setBold(True)
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boxBreathingScrollArea = QScrollArea(self.boxBreathingPage)
        self.boxBreathingScrollArea.setObjectName(u"boxBreathingScrollArea")
        self.boxBreathingScrollArea.setGeometry(QRect(0, 90, 721, 381))
        self.boxBreathingScrollArea.setStyleSheet(u"QScrollArea {\n"
"    background: rgba(255, 255, 255, 0.2);   /* semi-transparent white */\n"
"    border-radius: 20px;\n"
"    border: 1.5px solid rgba(255,255,255,0.5); /* white border with transparency */\n"
"}\n"
"\n"
"QScrollArea > QWidget > QVBoxLayout > * {\n"
"    background: transparent; /* make contents transparent */\n"
"}\n"
"\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"}\n"
"")
        self.boxBreathingScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.boxBreathingScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.boxBreathingScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 717, 377))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.boxBreathingScrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget.addWidget(self.boxBreathingPage)
        self.testResultDetailsPage = QWidget()
        self.testResultDetailsPage.setObjectName(u"testResultDetailsPage")
        self.testDetialsLabel = QLabel(self.testResultDetailsPage)
        self.testDetialsLabel.setObjectName(u"testDetialsLabel")
        self.testDetialsLabel.setGeometry(QRect(0, 10, 681, 81))
        self.testDetialsLabel.setFont(font5)
        self.testDetialsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.testDetialsLabel.setWordWrap(True)
        self.testResultDetailsScrollArea = QScrollArea(self.testResultDetailsPage)
        self.testResultDetailsScrollArea.setObjectName(u"testResultDetailsScrollArea")
        self.testResultDetailsScrollArea.setGeometry(QRect(0, 100, 731, 371))
        self.testResultDetailsScrollArea.setStyleSheet(u"QWidget {\n"
"    border: none;\n"
"	 border-radius: 16px;\n"
"    margin-bottom: 13px;\n"
"    /* Do NOT set background here or all widgets everywhere will get it */\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background: #20283666;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollArea > QWidget {\n"
"    background: #20283666;  /* Content widget is transparent */\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget {\n"
"    background-color: #20283666;  /* All direct child widgets = cards */\n"
"    border-radius: 16px;\n"
"    margin-bottom: 13px;\n"
"    border: 1.4px solid rgba(60,60,60,0.44); /* Optional: glass border */\n"
"}\n"
"\n"
"QScrollArea > QViewport {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.testResultDetailsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.testResultDetailsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.testResultDetailsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 705, 345))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"QWidget{\n"
"	background:transparent;\n"
"}")
        self.testResultDetailsScrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.label_25 = QLabel(self.testResultDetailsPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 800, 480))
        self.label_25.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.testResultsBackButton = QPushButton(self.testResultDetailsPage)
        self.testResultsBackButton.setObjectName(u"testResultsBackButton")
        self.testResultsBackButton.setGeometry(QRect(720, 0, 80, 80))
        self.testResultsBackButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.testResultsBackButton.setIcon(icon6)
        self.testResultsBackButton.setIconSize(QSize(64, 64))
        self.stackedWidget.addWidget(self.testResultDetailsPage)
        self.label_25.raise_()
        self.testDetialsLabel.raise_()
        self.testResultDetailsScrollArea.raise_()
        self.testResultsBackButton.raise_()
        self.DSMLevelTwoAnxiety = QWidget()
        self.DSMLevelTwoAnxiety.setObjectName(u"DSMLevelTwoAnxiety")
        self.label_11 = QLabel(self.DSMLevelTwoAnxiety)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 800, 480))
        self.label_11.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoAnxietyTitleLabel = QLabel(self.DSMLevelTwoAnxiety)
        self.dsmLevelTwoAnxietyTitleLabel.setObjectName(u"dsmLevelTwoAnxietyTitleLabel")
        self.dsmLevelTwoAnxietyTitleLabel.setGeometry(QRect(20, 9, 761, 71))
        font7 = QFont()
        font7.setPointSize(28)
        font7.setBold(True)
        self.dsmLevelTwoAnxietyTitleLabel.setFont(font7)
        self.dsmLevelTwoAnxietyTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoAnxietyTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoAnxietyLabel = QLabel(self.DSMLevelTwoAnxiety)
        self.dsmLevelTwoAnxietyLabel.setObjectName(u"dsmLevelTwoAnxietyLabel")
        self.dsmLevelTwoAnxietyLabel.setGeometry(QRect(19, 109, 761, 71))
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        self.dsmLevelTwoAnxietyLabel.setFont(font8)
        self.dsmLevelTwoAnxietyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_9 = QWidget(self.DSMLevelTwoAnxiety)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 190, 781, 201))
        self.dsmLevelTwoAnxietyQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.dsmLevelTwoAnxietyQuestionLayout.setObjectName(u"dsmLevelTwoAnxietyQuestionLayout")
        self.dsmLevelTwoAnxietyQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoAnxietyNextButton = QPushButton(self.DSMLevelTwoAnxiety)
        self.dsmLevelTwoAnxietyNextButton.setObjectName(u"dsmLevelTwoAnxietyNextButton")
        self.dsmLevelTwoAnxietyNextButton.setGeometry(QRect(10, 403, 781, 71))
        font9 = QFont()
        font9.setPointSize(44)
        font9.setBold(True)
        self.dsmLevelTwoAnxietyNextButton.setFont(font9)
        self.stackedWidget.addWidget(self.DSMLevelTwoAnxiety)
        self.DSMLevelTwoSomaticSymptoms = QWidget()
        self.DSMLevelTwoSomaticSymptoms.setObjectName(u"DSMLevelTwoSomaticSymptoms")
        self.label_12 = QLabel(self.DSMLevelTwoSomaticSymptoms)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 800, 480))
        self.label_12.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoSomaticSymptomTitleLabel = QLabel(self.DSMLevelTwoSomaticSymptoms)
        self.dsmLevelTwoSomaticSymptomTitleLabel.setObjectName(u"dsmLevelTwoSomaticSymptomTitleLabel")
        self.dsmLevelTwoSomaticSymptomTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoSomaticSymptomTitleLabel.setFont(font7)
        self.dsmLevelTwoSomaticSymptomTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoSomaticSymptomTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoSomaticSymptomLabel = QLabel(self.DSMLevelTwoSomaticSymptoms)
        self.dsmLevelTwoSomaticSymptomLabel.setObjectName(u"dsmLevelTwoSomaticSymptomLabel")
        self.dsmLevelTwoSomaticSymptomLabel.setGeometry(QRect(20, 80, 761, 61))
        self.dsmLevelTwoSomaticSymptomLabel.setFont(font5)
        self.dsmLevelTwoSomaticSymptomLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_10 = QWidget(self.DSMLevelTwoSomaticSymptoms)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 140, 781, 231))
        self.dsmLevelTwoSomaticSymptomQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_10)
        self.dsmLevelTwoSomaticSymptomQuestionLayout.setObjectName(u"dsmLevelTwoSomaticSymptomQuestionLayout")
        self.dsmLevelTwoSomaticSymptomQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoSomaticSymptomNextButton = QPushButton(self.DSMLevelTwoSomaticSymptoms)
        self.dsmLevelTwoSomaticSymptomNextButton.setObjectName(u"dsmLevelTwoSomaticSymptomNextButton")
        self.dsmLevelTwoSomaticSymptomNextButton.setGeometry(QRect(10, 380, 781, 91))
        self.dsmLevelTwoSomaticSymptomNextButton.setFont(font9)
        self.stackedWidget.addWidget(self.DSMLevelTwoSomaticSymptoms)
        self.DSMLevelTwoSleepDisturbance = QWidget()
        self.DSMLevelTwoSleepDisturbance.setObjectName(u"DSMLevelTwoSleepDisturbance")
        self.label_13 = QLabel(self.DSMLevelTwoSleepDisturbance)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 800, 480))
        self.label_13.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoSleepDisturbanceTitleLabel = QLabel(self.DSMLevelTwoSleepDisturbance)
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setObjectName(u"dsmLevelTwoSleepDisturbanceTitleLabel")
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setFont(font7)
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoSleepDisturbanceLabel = QLabel(self.DSMLevelTwoSleepDisturbance)
        self.dsmLevelTwoSleepDisturbanceLabel.setObjectName(u"dsmLevelTwoSleepDisturbanceLabel")
        self.dsmLevelTwoSleepDisturbanceLabel.setGeometry(QRect(20, 70, 761, 61))
        self.dsmLevelTwoSleepDisturbanceLabel.setFont(font5)
        self.dsmLevelTwoSleepDisturbanceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoSleepDisturbanceNextButton = QPushButton(self.DSMLevelTwoSleepDisturbance)
        self.dsmLevelTwoSleepDisturbanceNextButton.setObjectName(u"dsmLevelTwoSleepDisturbanceNextButton")
        self.dsmLevelTwoSleepDisturbanceNextButton.setGeometry(QRect(10, 360, 771, 111))
        self.dsmLevelTwoSleepDisturbanceNextButton.setFont(font9)
        self.verticalLayoutWidget_11 = QWidget(self.DSMLevelTwoSleepDisturbance)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(10, 140, 761, 211))
        self.dsmLevelTwoSleepDisturbanceQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_11)
        self.dsmLevelTwoSleepDisturbanceQuestionLayout.setObjectName(u"dsmLevelTwoSleepDisturbanceQuestionLayout")
        self.dsmLevelTwoSleepDisturbanceQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.DSMLevelTwoSleepDisturbance)
        self.DSMLevelTwoReptitiveThoughts = QWidget()
        self.DSMLevelTwoReptitiveThoughts.setObjectName(u"DSMLevelTwoReptitiveThoughts")
        self.label_14 = QLabel(self.DSMLevelTwoReptitiveThoughts)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 800, 480))
        self.label_14.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel = QLabel(self.DSMLevelTwoReptitiveThoughts)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setObjectName(u"dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setGeometry(QRect(20, 9, 761, 51))
        font10 = QFont()
        font10.setPointSize(18)
        font10.setBold(True)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setFont(font10)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton = QPushButton(self.DSMLevelTwoReptitiveThoughts)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setObjectName(u"dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setGeometry(QRect(19, 383, 771, 71))
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setFont(font9)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel = QLabel(self.DSMLevelTwoReptitiveThoughts)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setObjectName(u"dsmLevelTwoRepetitiveThoughtsBehaviorsLabel")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setGeometry(QRect(20, 70, 761, 50))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setFont(font11)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setWordWrap(True)
        self.verticalLayoutWidget_12 = QWidget(self.DSMLevelTwoReptitiveThoughts)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(20, 130, 771, 251))
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_12)
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.setObjectName(u"dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.DSMLevelTwoReptitiveThoughts)
        self.DSMLevelTwoSubstanceUse = QWidget()
        self.DSMLevelTwoSubstanceUse.setObjectName(u"DSMLevelTwoSubstanceUse")
        self.label_15 = QLabel(self.DSMLevelTwoSubstanceUse)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 800, 480))
        self.label_15.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoSubstanceUseTitleLabel = QLabel(self.DSMLevelTwoSubstanceUse)
        self.dsmLevelTwoSubstanceUseTitleLabel.setObjectName(u"dsmLevelTwoSubstanceUseTitleLabel")
        self.dsmLevelTwoSubstanceUseTitleLabel.setGeometry(QRect(9, -1, 771, 61))
        self.dsmLevelTwoSubstanceUseTitleLabel.setFont(font5)
        self.dsmLevelTwoSubstanceUseTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoSubstanceUseNextButton = QPushButton(self.DSMLevelTwoSubstanceUse)
        self.dsmLevelTwoSubstanceUseNextButton.setObjectName(u"dsmLevelTwoSubstanceUseNextButton")
        self.dsmLevelTwoSubstanceUseNextButton.setGeometry(QRect(19, 360, 771, 111))
        self.dsmLevelTwoSubstanceUseNextButton.setFont(font9)
        self.dsmLevelTwoSubstanceUseLabel = QLabel(self.DSMLevelTwoSubstanceUse)
        self.dsmLevelTwoSubstanceUseLabel.setObjectName(u"dsmLevelTwoSubstanceUseLabel")
        self.dsmLevelTwoSubstanceUseLabel.setGeometry(QRect(20, 70, 761, 50))
        font12 = QFont()
        font12.setPointSize(20)
        font12.setBold(True)
        self.dsmLevelTwoSubstanceUseLabel.setFont(font12)
        self.dsmLevelTwoSubstanceUseLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoSubstanceUseLabel.setWordWrap(True)
        self.verticalLayoutWidget_13 = QWidget(self.DSMLevelTwoSubstanceUse)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(10, 130, 781, 221))
        self.dsmLevelTwoSubstanceUseQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_13)
        self.dsmLevelTwoSubstanceUseQuestionLayout.setObjectName(u"dsmLevelTwoSubstanceUseQuestionLayout")
        self.dsmLevelTwoSubstanceUseQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.DSMLevelTwoSubstanceUse)
        self.DSMLevelTwoDepression = QWidget()
        self.DSMLevelTwoDepression.setObjectName(u"DSMLevelTwoDepression")
        self.label_7 = QLabel(self.DSMLevelTwoDepression)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 800, 480))
        self.label_7.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoDepressionTitleLabel = QLabel(self.DSMLevelTwoDepression)
        self.dsmLevelTwoDepressionTitleLabel.setObjectName(u"dsmLevelTwoDepressionTitleLabel")
        self.dsmLevelTwoDepressionTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoDepressionTitleLabel.setFont(font7)
        self.dsmLevelTwoDepressionTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoDepressionTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoDepressionLabel = QLabel(self.DSMLevelTwoDepression)
        self.dsmLevelTwoDepressionLabel.setObjectName(u"dsmLevelTwoDepressionLabel")
        self.dsmLevelTwoDepressionLabel.setGeometry(QRect(20, 70, 761, 61))
        self.dsmLevelTwoDepressionLabel.setFont(font5)
        self.dsmLevelTwoDepressionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_5 = QWidget(self.DSMLevelTwoDepression)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 130, 781, 241))
        self.dsmLevelTwoDepressionQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.dsmLevelTwoDepressionQuestionLayout.setObjectName(u"dsmLevelTwoDepressionQuestionLayout")
        self.dsmLevelTwoDepressionQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoDepressionNextButton = QPushButton(self.DSMLevelTwoDepression)
        self.dsmLevelTwoDepressionNextButton.setObjectName(u"dsmLevelTwoDepressionNextButton")
        self.dsmLevelTwoDepressionNextButton.setGeometry(QRect(10, 380, 781, 91))
        font13 = QFont()
        font13.setPointSize(45)
        font13.setBold(True)
        self.dsmLevelTwoDepressionNextButton.setFont(font13)
        self.stackedWidget.addWidget(self.DSMLevelTwoDepression)
        self.DSMLevelTwoIrritability = QWidget()
        self.DSMLevelTwoIrritability.setObjectName(u"DSMLevelTwoIrritability")
        self.label_10 = QLabel(self.DSMLevelTwoIrritability)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 800, 480))
        self.label_10.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoIrritabilityTitleLabel = QLabel(self.DSMLevelTwoIrritability)
        self.dsmLevelTwoIrritabilityTitleLabel.setObjectName(u"dsmLevelTwoIrritabilityTitleLabel")
        self.dsmLevelTwoIrritabilityTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoIrritabilityTitleLabel.setFont(font7)
        self.dsmLevelTwoIrritabilityTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoIrritabilityTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoIrritabilityLabel = QLabel(self.DSMLevelTwoIrritability)
        self.dsmLevelTwoIrritabilityLabel.setObjectName(u"dsmLevelTwoIrritabilityLabel")
        self.dsmLevelTwoIrritabilityLabel.setGeometry(QRect(20, 70, 761, 61))
        self.dsmLevelTwoIrritabilityLabel.setFont(font12)
        self.dsmLevelTwoIrritabilityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_8 = QWidget(self.DSMLevelTwoIrritability)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 130, 781, 241))
        self.dsmLevelTwoIrritabilityQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.dsmLevelTwoIrritabilityQuestionLayout.setObjectName(u"dsmLevelTwoIrritabilityQuestionLayout")
        self.dsmLevelTwoIrritabilityQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoIrritabilityNextButton = QPushButton(self.DSMLevelTwoIrritability)
        self.dsmLevelTwoIrritabilityNextButton.setObjectName(u"dsmLevelTwoIrritabilityNextButton")
        self.dsmLevelTwoIrritabilityNextButton.setGeometry(QRect(10, 380, 771, 91))
        self.dsmLevelTwoIrritabilityNextButton.setFont(font9)
        self.stackedWidget.addWidget(self.DSMLevelTwoIrritability)
        self.DSMLevelTwoAnger = QWidget()
        self.DSMLevelTwoAnger.setObjectName(u"DSMLevelTwoAnger")
        self.label_8 = QLabel(self.DSMLevelTwoAnger)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 800, 480))
        self.label_8.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoAngerTitleLabel = QLabel(self.DSMLevelTwoAnger)
        self.dsmLevelTwoAngerTitleLabel.setObjectName(u"dsmLevelTwoAngerTitleLabel")
        self.dsmLevelTwoAngerTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoAngerTitleLabel.setFont(font7)
        self.dsmLevelTwoAngerTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoAngerTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelTwoAngerLabel = QLabel(self.DSMLevelTwoAnger)
        self.dsmLevelTwoAngerLabel.setObjectName(u"dsmLevelTwoAngerLabel")
        self.dsmLevelTwoAngerLabel.setGeometry(QRect(20, 70, 761, 61))
        self.dsmLevelTwoAngerLabel.setFont(font5)
        self.dsmLevelTwoAngerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_6 = QWidget(self.DSMLevelTwoAnger)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 130, 771, 241))
        self.dsmLevelTwoAngerQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.dsmLevelTwoAngerQuestionLayout.setObjectName(u"dsmLevelTwoAngerQuestionLayout")
        self.dsmLevelTwoAngerQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoAngerNextButton = QPushButton(self.DSMLevelTwoAnger)
        self.dsmLevelTwoAngerNextButton.setObjectName(u"dsmLevelTwoAngerNextButton")
        self.dsmLevelTwoAngerNextButton.setGeometry(QRect(20, 380, 771, 91))
        self.stackedWidget.addWidget(self.DSMLevelTwoAnger)
        self.journalTextPage = QWidget()
        self.journalTextPage.setObjectName(u"journalTextPage")
        self.journalTextBack = QPushButton(self.journalTextPage)
        self.journalTextBack.setObjectName(u"journalTextBack")
        self.journalTextBack.setGeometry(QRect(720, 0, 80, 80))
        self.journalTextBack.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.journalTextBack.setIcon(icon6)
        self.journalTextBack.setIconSize(QSize(64, 64))
        self.label_17 = QLabel(self.journalTextPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 800, 480))
        self.label_17.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.journalTitle = QLabel(self.journalTextPage)
        self.journalTitle.setObjectName(u"journalTitle")
        self.journalTitle.setGeometry(QRect(100, 5, 611, 101))
        self.journalTitle.setFont(font4)
        self.scrollArea = QScrollArea(self.journalTextPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(100, 120, 601, 331))
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"                    border: none;\n"
"					background:transparent;\n"
"                }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 601, 331))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"                    border: 1.4px solid rgba(60,60,60,0.44);\n"
"                    border-radius: 22px;\n"
"                    background: rgba(32, 40, 54, 0.40); /* Translucent, glassy */\n"
"                    margin-bottom: 13px;\n"
"                    backdrop-filter: blur(8px);\n"
"                }")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.NoteTitle = QLabel(self.scrollAreaWidgetContents)
        self.NoteTitle.setObjectName(u"NoteTitle")
        self.NoteTitle.setFont(font5)
        self.NoteTitle.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.NoteTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.NoteTitle)

        self.journalNote = QLabel(self.scrollAreaWidgetContents)
        self.journalNote.setObjectName(u"journalNote")
        self.journalNote.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.journalNote.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.journalNote.setWordWrap(True)

        self.horizontalLayout.addWidget(self.journalNote)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.journalTextPage)
        self.label_17.raise_()
        self.journalTextBack.raise_()
        self.journalTitle.raise_()
        self.scrollArea.raise_()
        self.journalReccomendationpage = QWidget()
        self.journalReccomendationpage.setObjectName(u"journalReccomendationpage")
        self.backJournalRecomButton = QPushButton(self.journalReccomendationpage)
        self.backJournalRecomButton.setObjectName(u"backJournalRecomButton")
        self.backJournalRecomButton.setGeometry(QRect(720, 0, 80, 80))
        self.backJournalRecomButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.backJournalRecomButton.setIcon(icon6)
        self.backJournalRecomButton.setIconSize(QSize(64, 64))
        self.label_18 = QLabel(self.journalReccomendationpage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 800, 480))
        self.label_18.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.scrollArea_2 = QScrollArea(self.journalReccomendationpage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(100, 90, 611, 341))
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
"                    border: none;\n"
"					background:transparent;\n"
"                }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 611, 341))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"QWidget {\n"
"                    border: 1.4px solid rgba(60,60,60,0.44);\n"
"                    border-radius: 22px;\n"
"                    background: rgba(32, 40, 54, 0.40); /* Translucent, glassy */\n"
"                    margin-bottom: 13px;\n"
"                    backdrop-filter: blur(8px);\n"
"                }")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font12)
        self.label_19.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.label_19)

        self.journalRecomLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.journalRecomLabel.setObjectName(u"journalRecomLabel")
        self.journalRecomLabel.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	border:none;\n"
"}")
        self.journalRecomLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.journalRecomLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.journalRecomLabel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.journalReccomendationpage)
        self.label_18.raise_()
        self.backJournalRecomButton.raise_()
        self.scrollArea_2.raise_()
        self.takeSamplePage = QWidget()
        self.takeSamplePage.setObjectName(u"takeSamplePage")
        font14 = QFont()
        font14.setPointSize(9)
        self.takeSamplePage.setFont(font14)
        self.cameraLabel = QLabel(self.takeSamplePage)
        self.cameraLabel.setObjectName(u"cameraLabel")
        self.cameraLabel.setGeometry(QRect(60, 10, 521, 351))
        font15 = QFont()
        font15.setPointSize(43)
        font15.setBold(True)
        self.cameraLabel.setFont(font15)
        self.cameraLabel.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.cameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cameraLabel.setWordWrap(False)
        self.sampleBackButton = QPushButton(self.takeSamplePage)
        self.sampleBackButton.setObjectName(u"sampleBackButton")
        self.sampleBackButton.setGeometry(QRect(710, 0, 80, 80))
        self.sampleBackButton.setFont(font15)
        self.sampleBackButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent; /* Optional: if you want to remove default background too */\n"
"}\n"
"")
        self.sampleBackButton.setIcon(icon6)
        self.sampleBackButton.setIconSize(QSize(64, 64))
        self.label_21 = QLabel(self.takeSamplePage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 800, 480))
        font16 = QFont()
        font16.setPointSize(20)
        self.label_21.setFont(font16)
        self.label_21.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.label_21.setWordWrap(True)
        self.captureButton = QPushButton(self.takeSamplePage)
        self.captureButton.setObjectName(u"captureButton")
        self.captureButton.setGeometry(QRect(340, 390, 80, 24))
        self.sampleLabel = QLabel(self.takeSamplePage)
        self.sampleLabel.setObjectName(u"sampleLabel")
        self.sampleLabel.setGeometry(QRect(610, 270, 181, 81))
        self.sampleLabel.setFont(font12)
        self.addSensorButton = QPushButton(self.takeSamplePage)
        self.addSensorButton.setObjectName(u"addSensorButton")
        self.addSensorButton.setGeometry(QRect(720, 170, 80, 80))
        font17 = QFont()
        font17.setPointSize(9)
        font17.setBold(True)
        self.addSensorButton.setFont(font17)
        self.stackedWidget.addWidget(self.takeSamplePage)
        self.label_21.raise_()
        self.cameraLabel.raise_()
        self.sampleBackButton.raise_()
        self.captureButton.raise_()
        self.sampleLabel.raise_()
        self.addSensorButton.raise_()
        self.recalibratePage = QWidget()
        self.recalibratePage.setObjectName(u"recalibratePage")
        self.label_27 = QLabel(self.recalibratePage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 800, 480))
        self.label_27.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"")
        self.calibrateButton = QPushButton(self.recalibratePage)
        self.calibrateButton.setObjectName(u"calibrateButton")
        self.calibrateButton.setGeometry(QRect(640, 300, 80, 24))
        self.calibrateButton.setFont(font3)
        self.stackedWidget.addWidget(self.recalibratePage)
        self.DSMLevelTwoMania = QWidget()
        self.DSMLevelTwoMania.setObjectName(u"DSMLevelTwoMania")
        self.dsmLevelTwoManiaTitleLabel = QLabel(self.DSMLevelTwoMania)
        self.dsmLevelTwoManiaTitleLabel.setObjectName(u"dsmLevelTwoManiaTitleLabel")
        self.dsmLevelTwoManiaTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelTwoManiaTitleLabel.setFont(font7)
        self.dsmLevelTwoManiaTitleLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dsmLevelTwoManiaTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.DSMLevelTwoMania)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 800, 480))
        self.label_9.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelTwoManiaLabel = QLabel(self.DSMLevelTwoMania)
        self.dsmLevelTwoManiaLabel.setObjectName(u"dsmLevelTwoManiaLabel")
        self.dsmLevelTwoManiaLabel.setGeometry(QRect(20, 70, 761, 61))
        self.dsmLevelTwoManiaLabel.setFont(font10)
        self.dsmLevelTwoManiaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_7 = QWidget(self.DSMLevelTwoMania)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 140, 781, 231))
        self.dsmLevelTwoManiaQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.dsmLevelTwoManiaQuestionLayout.setObjectName(u"dsmLevelTwoManiaQuestionLayout")
        self.dsmLevelTwoManiaQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.dsmLevelTwoManiaNextButton = QPushButton(self.DSMLevelTwoMania)
        self.dsmLevelTwoManiaNextButton.setObjectName(u"dsmLevelTwoManiaNextButton")
        self.dsmLevelTwoManiaNextButton.setGeometry(QRect(10, 380, 781, 91))
        self.dsmLevelTwoManiaNextButton.setFont(font9)
        self.stackedWidget.addWidget(self.DSMLevelTwoMania)
        self.label_9.raise_()
        self.dsmLevelTwoManiaTitleLabel.raise_()
        self.dsmLevelTwoManiaLabel.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.dsmLevelTwoManiaNextButton.raise_()
        self.takeDSMLevelOnePage = QWidget()
        self.takeDSMLevelOnePage.setObjectName(u"takeDSMLevelOnePage")
        self.label_6 = QLabel(self.takeDSMLevelOnePage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 800, 480))
        self.label_6.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.dsmLevelOneLabel = QLabel(self.takeDSMLevelOnePage)
        self.dsmLevelOneLabel.setObjectName(u"dsmLevelOneLabel")
        self.dsmLevelOneLabel.setGeometry(QRect(10, 60, 781, 61))
        self.dsmLevelOneLabel.setFont(font8)
        self.dsmLevelOneLabel.setStyleSheet(u"QLabel{\n"
"	font-weight: bold;\n"
"}")
        self.dsmLevelOneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dsmLevelOneLabel.setWordWrap(True)
        self.dsmLevelOneNext = QPushButton(self.takeDSMLevelOnePage)
        self.dsmLevelOneNext.setObjectName(u"dsmLevelOneNext")
        self.dsmLevelOneNext.setGeometry(QRect(10, 380, 781, 91))
        self.dsmLevelOneTitleLabel = QLabel(self.takeDSMLevelOnePage)
        self.dsmLevelOneTitleLabel.setObjectName(u"dsmLevelOneTitleLabel")
        self.dsmLevelOneTitleLabel.setGeometry(QRect(10, 10, 781, 50))
        self.dsmLevelOneTitleLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	 font-weight: bold;\n"
"	 font-size: 40px;\n"
"}")
        self.dsmLevelOneTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_4 = QWidget(self.takeDSMLevelOnePage)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 130, 781, 241))
        self.dsmLevelOneQuestionLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.dsmLevelOneQuestionLayout.setObjectName(u"dsmLevelOneQuestionLayout")
        self.dsmLevelOneQuestionLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.takeDSMLevelOnePage)
        self.registerScreen = QWidget()
        self.registerScreen.setObjectName(u"registerScreen")
        self.label_3 = QLabel(self.registerScreen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 800, 480))
        self.label_3.setStyleSheet(u"QWidget {\n"
"    background-image: url(Assets/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"")
        self.label_3.setScaledContents(False)
        self.verticalLayoutWidget = QWidget(self.registerScreen)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 0, 321, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 9, 0, 9)
        self.firstNameInput = QLineEdit(self.verticalLayoutWidget)
        self.firstNameInput.setObjectName(u"firstNameInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.firstNameInput.sizePolicy().hasHeightForWidth())
        self.firstNameInput.setSizePolicy(sizePolicy2)
        self.firstNameInput.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.firstNameInput)

        self.lastNameInput = QLineEdit(self.verticalLayoutWidget)
        self.lastNameInput.setObjectName(u"lastNameInput")

        self.verticalLayout.addWidget(self.lastNameInput)

        self.usernameInput = QLineEdit(self.verticalLayoutWidget)
        self.usernameInput.setObjectName(u"usernameInput")

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.verticalLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")

        self.verticalLayout.addWidget(self.passwordInput)

        self.ageInput = QLineEdit(self.verticalLayoutWidget)
        self.ageInput.setObjectName(u"ageInput")

        self.verticalLayout.addWidget(self.ageInput)

        self.genderComboBox = QComboBox(self.verticalLayoutWidget)
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.verticalLayout.addWidget(self.genderComboBox)

        self.submitButtonRegister = QPushButton(self.registerScreen)
        self.submitButtonRegister.setObjectName(u"submitButtonRegister")
        self.submitButtonRegister.setGeometry(QRect(290, 330, 251, 81))
        self.backButtonRegister = QPushButton(self.registerScreen)
        self.backButtonRegister.setObjectName(u"backButtonRegister")
        self.backButtonRegister.setGeometry(QRect(60, 20, 80, 24))
        self.stackedWidget.addWidget(self.registerScreen)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label.setText("")
        self.powerOffButton.setText("")
        self.label_2.setText("")
        self.usernameLoginInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLoginInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginSubmitButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.backButtonLogin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.powerOffButtonLogin.setText("")
        self.label_4.setText("")
        self.powerOffButtonDashboard.setText("")
        self.notificationButton.setText("")
        self.resultsButton.setText("")
        self.logoffButton.setText("")
        self.sampleButton.setText("")
        self.notificationCountLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tomoFace.setText("")
        self.pairWatchButton.setText(QCoreApplication.translate("MainWindow", u"PAIR WATCH", None))
        self.heartRateButton.setText("")
        self.label_24.setText("")
        self.heartRateBackButton.setText("")
        self.heartRateGraph.setText("")
        self.label_28.setText("")
        self.addSensorBackButton.setText("")
        self.addSensorCamera.setText("")
        self.addSensorAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.finalAddButton.setText(QCoreApplication.translate("MainWindow", u"Add Sensor", None))
        self.RGBLabel.setText("")
        self.label_26.setText("")
        self.pairBackButton.setText("")
        self.pairButton.setText(QCoreApplication.translate("MainWindow", u"PAIR", None))
        self.label_5.setText("")
        self.homeButtonNotificationPage.setText("")
        self.resultsButtonNotificationPage.setText("")
        self.logoffButtonNotificationPage.setText("")
        self.powerOffButtonNotificationPage.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), QCoreApplication.translate("MainWindow", u"Results", None))
        self.addNoteButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Notes), QCoreApplication.translate("MainWindow", u"Notes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resources), QCoreApplication.translate("MainWindow", u"Resources", None))
        self.homeButtonResultsPage.setText("")
        self.label_16.setText("")
        self.notificationButtonResults.setText("")
        self.notificationCountLabelResults.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText("")
        self.GroundingTitle.setText(QCoreApplication.translate("MainWindow", u"Ground Session", None))
        self.groundingQuestionLabel.setText("")
        self.groundingNextpushButton.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.label_22.setText("")
        self.boxBreathingBackButton.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Box Breathing Tecnique", None))
        self.testDetialsLabel.setText(QCoreApplication.translate("MainWindow", u"Test Results", None))
        self.label_25.setText("")
        self.testResultsBackButton.setText("")
        self.label_11.setText("")
        self.dsmLevelTwoAnxietyTitleLabel.setText("")
        self.dsmLevelTwoAnxietyLabel.setText("")
        self.dsmLevelTwoAnxietyNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_12.setText("")
        self.dsmLevelTwoSomaticSymptomTitleLabel.setText("")
        self.dsmLevelTwoSomaticSymptomLabel.setText("")
        self.dsmLevelTwoSomaticSymptomNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_13.setText("")
        self.dsmLevelTwoSleepDisturbanceTitleLabel.setText("")
        self.dsmLevelTwoSleepDisturbanceLabel.setText("")
        self.dsmLevelTwoSleepDisturbanceNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_14.setText("")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsTitleLabel.setText("")
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.dsmLevelTwoRepetitiveThoughtsBehaviorsLabel.setText("")
        self.label_15.setText("")
        self.dsmLevelTwoSubstanceUseTitleLabel.setText("")
        self.dsmLevelTwoSubstanceUseNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.dsmLevelTwoSubstanceUseLabel.setText("")
        self.label_7.setText("")
        self.dsmLevelTwoDepressionTitleLabel.setText("")
        self.dsmLevelTwoDepressionLabel.setText("")
        self.dsmLevelTwoDepressionNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_10.setText("")
        self.dsmLevelTwoIrritabilityTitleLabel.setText("")
        self.dsmLevelTwoIrritabilityLabel.setText("")
        self.dsmLevelTwoIrritabilityNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_8.setText("")
        self.dsmLevelTwoAngerTitleLabel.setText("")
        self.dsmLevelTwoAngerLabel.setText("")
        self.dsmLevelTwoAngerNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.journalTextBack.setText("")
        self.label_17.setText("")
        self.journalTitle.setText("")
        self.NoteTitle.setText(QCoreApplication.translate("MainWindow", u"Note:", None))
        self.journalNote.setText("")
        self.backJournalRecomButton.setText("")
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Reccomendation: ", None))
        self.journalRecomLabel.setText("")
        self.cameraLabel.setText(QCoreApplication.translate("MainWindow", u"1.32 mg/ml", None))
        self.sampleBackButton.setText("")
        self.label_21.setText("")
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))
        self.sampleLabel.setText("")
        self.addSensorButton.setText(QCoreApplication.translate("MainWindow", u"Add Sensor", None))
        self.label_27.setText("")
        self.calibrateButton.setText(QCoreApplication.translate("MainWindow", u"CALIBRATE", None))
        self.dsmLevelTwoManiaTitleLabel.setText("")
        self.label_9.setText("")
        self.dsmLevelTwoManiaLabel.setText("")
        self.dsmLevelTwoManiaNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_6.setText("")
        self.dsmLevelOneLabel.setText("")
        self.dsmLevelOneNext.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.dsmLevelOneTitleLabel.setText("")
        self.label_3.setText("")
        self.firstNameInput.setText("")
        self.firstNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lastNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ageInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Female", None))
        self.genderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Non Binary", None))
        self.genderComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Prefer not to say", None))

        self.submitButtonRegister.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.backButtonRegister.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
    # retranslateUi

