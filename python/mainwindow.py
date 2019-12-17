import sys



from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import threading
import time
import requests
import base64
# from saftey import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from app_gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.images = {"ee" : "Elec.png"}
        self.tread_keep_alive = True
        self.counter = 0
        self.add_images_to_list()
        self.ui.pushButton.clicked.connect(self.show_button)
        x = threading.Thread(target=self.thread_function, args=())
        x.start()

    def closeEvent(self, event):
        self.kill_thread()
        event.accept()

    def add_images_to_list(self):
        for key,val in self.images.items():
            self.ui.listWidget.addItem(key)

    def show_button(self):
        # print(self.listWidget.currentItem().text())
        pixmap = QPixmap(self.images[self.ui.listWidget.currentItem().text()])

        pixmap = pixmap.scaled(800, 800, QtCore.Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap)


    def add_image(self,imgname,img):
        self.images[imgname] = img
        self.ui.listWidget.addItem(imgname)
        print("image added from server")

    def thread_function(self):
        while self.tread_keep_alive:
            try:
                response = requests.get("http://10.144.66.31:5000/newPic")
                if response.text == "true":
                    response = requests.get("http://10.144.66.31:5000/getImage")
                    data = response.json()
                    print(data)
                    pm = QtGui.QPixmap()
                    decoded = base64.b64decode(data["image"])
                    # print(decoded)
                    pm.loadFromData(decoded)
                    self.add_image(f'Time: {data["time"]} , Location: {data["location"]}',pm)
                    self.counter += 1
                time.sleep(2)
            except:
                pass

    def kill_thread(self):
        self.tread_keep_alive = False





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    self.ui = Ui_MainWindow()

    self.ui.setupUi(self)