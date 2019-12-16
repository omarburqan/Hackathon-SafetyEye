import sys



from PyQt5.QtWidgets import QApplication, QMainWindow

# from saftey import Ui_MainWindow
from newgui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.kill_thread()
        event.accept()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    self.ui = Ui_MainWindow()

    self.ui.setupUi(self)