# Form implementation generated from reading ui file 'app\ui\Raiting_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(664, 540)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 651, 301))
        self.tableWidget.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 85, 127);")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.pushButton_Singe_Game = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Singe_Game.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.pushButton_Singe_Game.setStyleSheet("color: rgb(206, 0, 103);\n"
"color: rgb(85, 255, 0);\n"
"background-color: rgb(214, 0, 107);\n"
"")
        self.pushButton_Singe_Game.setObjectName("pushButton_Singe_Game")
        self.pushButton_Toutnier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Toutnier.setGeometry(QtCore.QRect(460, 20, 191, 31))
        self.pushButton_Toutnier.setStyleSheet("color: rgb(206, 0, 103);\n"
"color: rgb(85, 255, 0);\n"
"background-color: rgb(214, 0, 107);")
        self.pushButton_Toutnier.setObjectName("pushButton_Toutnier")
        self.pushButton_change_single_game = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_change_single_game.setGeometry(QtCore.QRect(40, 400, 191, 31))
        self.pushButton_change_single_game.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 85, 0);\n"
"")
        self.pushButton_change_single_game.setObjectName("pushButton_change_single_game")
        self.pushButton_change_tourner = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_change_tourner.setGeometry(QtCore.QRect(400, 400, 191, 31))
        self.pushButton_change_tourner.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 85, 0);\n"
"")
        self.pushButton_change_tourner.setObjectName("pushButton_change_tourner")
        self.lineEdit_single_team = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_single_team.setGeometry(QtCore.QRect(40, 451, 191, 31))
        self.lineEdit_single_team.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_single_team.setObjectName("lineEdit_single_team")
        self.lineEdit_2_tournert = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2_tournert.setGeometry(QtCore.QRect(400, 450, 191, 31))
        self.lineEdit_2_tournert.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_2_tournert.setObjectName("lineEdit_2_tournert")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 430, 191, 16))
        self.label.setStyleSheet("color: rgb(0, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 430, 191, 16))
        self.label_2.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Количество побед"))
        self.pushButton_Singe_Game.setText(_translate("MainWindow", "SingleGame"))
        self.pushButton_Toutnier.setText(_translate("MainWindow", "Tournier"))
        self.pushButton_change_single_game.setText(_translate("MainWindow", "Одиночная игра    +1"))
        self.pushButton_change_tourner.setText(_translate("MainWindow", "Турнир  +1"))
        self.label.setText(_translate("MainWindow", "            Название команды"))
        self.label_2.setText(_translate("MainWindow", "            Название команды"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
