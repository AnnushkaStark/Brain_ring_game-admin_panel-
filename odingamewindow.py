# Form implementation generated from reading ui file 'odingamewindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_odingameWindow(object):
    def setupUi(self, odingameWindow):
        odingameWindow.setObjectName("odingameWindow")
        odingameWindow.resize(550, 330)
        self.centralwidget = QtWidgets.QWidget(parent=odingameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 70, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 110, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 110, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 290, 110, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        odingameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(odingameWindow)
        QtCore.QMetaObject.connectSlotsByName(odingameWindow)

    def retranslateUi(self, odingameWindow):
        _translate = QtCore.QCoreApplication.translate
        odingameWindow.setWindowTitle(_translate("odingameWindow", "Начало одиночной игры"))
        self.label.setText(_translate("odingameWindow", "Название команды №1"))
        self.label_2.setText(_translate("odingameWindow", "Название команды №2"))
        self.pushButton.setText(_translate("odingameWindow", "Изменить правила"))
        self.pushButton_2.setText(_translate("odingameWindow", "Начало игры"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    odingameWindow = QtWidgets.QMainWindow()
    ui = Ui_odingameWindow()
    ui.setupUi(odingameWindow)
    odingameWindow.show()
    sys.exit(app.exec())
