# Form implementation generated from reading ui file 'app\ui\commands.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(442, 469)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 210, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 141, 20))
        self.label.setStyleSheet("color: rgb(170, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 260, 141, 20))
        self.label_2.setStyleSheet("color: rgb(170, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_team_single = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_team_single.setGeometry(QtCore.QRect(20, 70, 191, 22))
        self.lineEdit_team_single.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_team_single.setObjectName("lineEdit_team_single")
        self.lineEdit_team_tournier = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_team_tournier.setGeometry(QtCore.QRect(30, 320, 191, 22))
        self.lineEdit_team_tournier.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_team_tournier.setObjectName("lineEdit_team_tournier")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 171, 20))
        self.label_3.setStyleSheet("color: rgb(170, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 171, 20))
        self.label_4.setStyleSheet("color: rgb(170, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.pushButton_add_single = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add_single.setGeometry(QtCore.QRect(20, 110, 121, 41))
        self.pushButton_add_single.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_add_single.setObjectName("pushButton_add_single")
        self.pushButton_change_single = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_change_single.setGeometry(QtCore.QRect(280, 110, 121, 41))
        self.pushButton_change_single.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_change_single.setObjectName("pushButton_change_single")
        self.pushButton_delet_single = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_delet_single.setGeometry(QtCore.QRect(150, 110, 121, 41))
        self.pushButton_delet_single.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_delet_single.setObjectName("pushButton_delet_single")
        self.pushButton_add_tournier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add_tournier.setGeometry(QtCore.QRect(20, 360, 121, 41))
        self.pushButton_add_tournier.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_add_tournier.setObjectName("pushButton_add_tournier")
        self.pushButton_change_tournier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_change_tournier.setGeometry(QtCore.QRect(280, 360, 121, 41))
        self.pushButton_change_tournier.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_change_tournier.setObjectName("pushButton_change_tournier")
        self.pushButton_delet_tournier = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_delet_tournier.setGeometry(QtCore.QRect(150, 360, 121, 41))
        self.pushButton_delet_tournier.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 170, 0);")
        self.pushButton_delet_tournier.setObjectName("pushButton_delet_tournier")
        self.lineEdit_team_single_2_new = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_team_single_2_new.setGeometry(QtCore.QRect(220, 70, 191, 22))
        self.lineEdit_team_single_2_new.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_team_single_2_new.setObjectName("lineEdit_team_single_2_new")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 40, 171, 20))
        self.label_5.setStyleSheet("color: rgb(170, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_team_tournier_2_new = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_team_tournier_2_new.setGeometry(QtCore.QRect(230, 320, 191, 22))
        self.lineEdit_team_tournier_2_new.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit_team_tournier_2_new.setObjectName("lineEdit_team_tournier_2_new")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 290, 171, 20))
        self.label_6.setStyleSheet("color: rgb(170, 255, 0);")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 22))
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
        self.label.setText(_translate("MainWindow", "        Одиночная игра"))
        self.label_2.setText(_translate("MainWindow", "              Турнир"))
        self.label_3.setText(_translate("MainWindow", "        Название команды"))
        self.label_4.setText(_translate("MainWindow", "        Название команды"))
        self.pushButton_add_single.setText(_translate("MainWindow", "Добавить "))
        self.pushButton_change_single.setText(_translate("MainWindow", "Изменить название"))
        self.pushButton_delet_single.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_add_tournier.setText(_translate("MainWindow", "Добавить "))
        self.pushButton_change_tournier.setText(_translate("MainWindow", "Изменить название"))
        self.pushButton_delet_tournier.setText(_translate("MainWindow", "Удалить"))
        self.label_5.setText(_translate("MainWindow", "            Новое название"))
        self.label_6.setText(_translate("MainWindow", "        Новое название"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
