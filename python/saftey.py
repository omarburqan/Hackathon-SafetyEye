# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saftey.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import threading
import time
import requests
import base64





class Ui_MainWindow(object):
    def __init__(self):
        self.images = {}
        self.tread_keep_alive = True
        self.counter = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 20, 501, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)

        self.add_images_to_list()

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.show_button)

        self.verticalLayout_2.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 200))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        x = threading.Thread(target=self.thread_function, args=())
        x.start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "show"))




    def add_images_to_list(self):
        for key,val in self.images.items():
            self.listWidget.addItem(key)

    def show_button(self):
        # print(self.listWidget.currentItem().text())
        pixmap = QPixmap(self.images[self.listWidget.currentItem().text()])
        self.label.setPixmap(pixmap)


    def add_image(self,imgname,img):
        self.images[imgname] = img
        self.listWidget.addItem(imgname)
        print("image added from server")

    def thread_function(self):
        while self.tread_keep_alive:
            response = requests.get("http://10.144.66.31:5000/newPic")
            if response.text == "true":
                response = requests.get("http://10.144.66.31:5000/getImage")
                pm = QtGui.QPixmap()
                pm.loadFromData(base64.b64decode(response.text))
                self.add_image("image " + str(self.counter),pm)
                self.counter += 1
            time.sleep(5)

    def kill_thread(self):
        self.tread_keep_alive = False

