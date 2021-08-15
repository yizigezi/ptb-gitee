# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'installerDzLgIA.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6 import QtWidgets
from config import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(357, 175)
        MainWindow.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 10, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 60, 75, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 9, 151, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 40, 55, 16))
        self.label.setVisible(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 130, 171, 16))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 80, 91, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 55, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 61, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 90, 61, 16))
        self.label_5.setVisible(False)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 10, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.instdir)
        self.pushButton.clicked.connect(self.install)
        self.pushButton_3.clicked.connect(self.download)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", name + " 安装程序", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "安装", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "安装完成", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "取消", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", installer_name, None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", "下载" + name, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "注意:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "安装前请先", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "下载完成!", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", "选择路径", None))
    # retranslateUi

    def instdir(self):
        global reply
        import easygui as g
        reply = g.diropenbox()
        self.lineEdit.setText(reply)
    
    def download(self):
        self.label_5.setVisible(False)
        import requests
        url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/py-dos-win.zip"
        downloadfile = requests.get(url, headers=headers)
        with open(filename, "wb") as d:
            d.write(downloadfile.content)
        self.label_5.setVisible(True)

    def install(self):
        self.label_5.setVisible(False)
        import os
        import zipfile
        import webbrowser
        zip_file = zipfile.ZipFile(filename)
        zip_list = zip_file.namelist() # 得到压缩包里所有文件
        for f in zip_list:
            zip_file.extract(f, reply) # 循环解压文件到指定目录
        zip_file.close()
        if boot_filedir != "":
            os.system(command + reply + boot_filedir)
        self.label_5.setVisible(True)
        webbrowser.open(ourl)
        

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())