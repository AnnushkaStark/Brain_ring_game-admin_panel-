# Form implementation generated from reading ui file 'app\ui\question_creator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(404, 348)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 361, 271))
        self.widget.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"")
        self.widget.setObjectName("widget")
        self.spinBox_limit = QtWidgets.QSpinBox(parent=self.widget)
        self.spinBox_limit.setGeometry(QtCore.QRect(60, 20, 111, 31))
        self.spinBox_limit.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-radius: 10px;")
        self.spinBox_limit.setObjectName("spinBox_limit")
        self.pushButton_back_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_back_2.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.pushButton_back_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(90, 60, 181, 20))
        self.label.setStyleSheet("color: rgb(170, 255, 0);")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 341, 71))
        self.plainTextEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_submit = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_submit.setGeometry(QtCore.QRect(170, 20, 111, 31))
        self.pushButton_submit.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton_submit.setObjectName("pushButton_submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 22))
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
        self.pushButton_back_2.setText(_translate("MainWindow", "Вопрос"))
        self.label.setText(_translate("MainWindow", "           Количество вопросов"))
        self.pushButton_submit.setText(_translate("MainWindow", "Применить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
