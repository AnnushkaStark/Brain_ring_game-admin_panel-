# Form implementation generated from reading ui file 'start_screen_qt.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from new_game_1 import Ui_nGame_1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 50, 161, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_singleGame = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_singleGame.setObjectName("btn_singleGame")
        self.verticalLayout.addWidget(self.btn_singleGame)
        self.btn_singleGame.clicked.connect(self.opn_new_game_1)
        self.btn_tournament = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_tournament.setObjectName("btn_tournament")
        self.verticalLayout.addWidget(self.btn_tournament)
        self.btn_rules = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_rules.setEnabled(True)
        self.btn_rules.setIconSize(QtCore.QSize(20, 20))
        self.btn_rules.setObjectName("btn_rules")
        self.verticalLayout.addWidget(self.btn_rules)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 300, 181, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_prepare = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btn_prepare.setObjectName("btn_prepare")
        self.verticalLayout_2.addWidget(self.btn_prepare)
        self.btn_settings = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout_2.addWidget(self.btn_settings)
        self.btn_quit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_quit.setGeometry(QtCore.QRect(560, 350, 93, 28))
        self.btn_quit.setObjectName("btn_quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_size(self):
        self.setGeometry(400, 500, 653, 430)

    def opn_new_game_1(self):
        self.nGame_1 = QtWidgets.QMainWindow()
        self.ui_nGame_1 = Ui_nGame_1()
        self.ui_nGame_1.setupUi(self.nGame_1)
        self.nGame_1.show()
        # self.wnd_wall = QtWidgets.QMainWindow()
        # self.ui_wndWall = Ui_wnd_wall()
        # self.ui_wndWall.setupUi(self.wnd_wall)
        # self.wnd_wall.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_singleGame.setText(_translate("MainWindow", "Одна игра"))
        self.btn_tournament.setText(_translate("MainWindow", "Турнир"))
        self.btn_rules.setText(_translate("MainWindow", "Правила"))
        self.btn_prepare.setText(_translate("MainWindow", "Подготовка"))
        self.btn_settings.setText(_translate("MainWindow", "Настройки"))
        self.btn_quit.setText(_translate("MainWindow", "Выход"))
