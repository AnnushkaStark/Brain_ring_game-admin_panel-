import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


from UI.start_screen import Ui_MainWindow

# Создайте класс окна, наследующийся от QMainWindow и Ui_MainWindow
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #self.change_size()
        # Инициализируйте интерфейс из класса Ui_MainWindow
        self.setupUi(self)



# Создайте экземпляр приложения QApplication
app = QApplication(sys.argv)

# Создайте экземпляр вашего окна
window = MyWindow()

# Покажите окно
window.show()

# Запустите главный цикл приложения
sys.exit(app.exec())
