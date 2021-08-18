# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py-dosoAhAue.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
##############################################################################
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(581, 604)
        MainWindow.setWindowFlags(Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        icon = QIcon()
        icon.addFile(u"./newlogo.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 0, 311, 41))
        font = QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(410, 10, 131, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 6, 44, 41))
        icon = QIcon()
        icon.addFile(u"./search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setFlat(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 50, 581, 521))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 55, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 15, 91, 24))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 250, 71, 31))
        self.label_2.setFont(font1)
        self.homebutton_1 = QPushButton(self.page)
        self.homebutton_1.setObjectName(u"pushButton_3")
        self.homebutton_1.setGeometry(QRect(60, 50, 201, 50))
        self.homebutton_2 = QPushButton(self.page)
        self.homebutton_2.setObjectName(u"pushButton_4")
        self.homebutton_2.setGeometry(QRect(320, 50, 201, 50))
        self.homebutton_4 = QPushButton(self.page)
        self.homebutton_4.setObjectName(u"pushButton_5")
        self.homebutton_4.setGeometry(QRect(320, 120, 201, 50))
        self.homebutton_3 = QPushButton(self.page)
        self.homebutton_3.setObjectName(u"pushButton_6")
        self.homebutton_3.setGeometry(QRect(60, 120, 201, 50))
        self.homebutton_5 = QPushButton(self.page)
        self.homebutton_5.setObjectName(u"pushButton_7")
        self.homebutton_5.setGeometry(QRect(60, 190, 201, 50))
        self.homebutton_6 = QPushButton(self.page)
        self.homebutton_6.setObjectName(u"pushButton_8")
        self.homebutton_6.setGeometry(QRect(320, 190, 201, 50))
        self.listWidget_2 = QListWidget(self.page)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(20, 280, 541, 201))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pushButton_9 = QPushButton(self.page_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(40, 20, 91, 24))
        self.listWidget_3 = QListWidget(self.page_2)
        font2 = QFont()
        font2.setPointSize(14)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem.setFont(font2);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem1.setFont(font2);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem2.setFont(font2);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem3.setFont(font2);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4.setFont(font2);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem5.setFont(font2);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem6.setFont(font2);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem7.setFont(font2);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem8.setFont(font2);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem9.setFont(font2);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem10.setFont(font2);
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(40, 50, 501, 431))
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_16 = QPushButton(self.page_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(434, 20, 111, 24))
        self.pushButton_16.setEnabled(False)

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 71, 31))
        self.label_4.setFont(font1)
        self.pushButton_10 = QPushButton(self.page_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 60, 131, 71))
        self.pushButton_11 = QPushButton(self.page_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(150, 60, 131, 71))
        self.pushButton_12 = QPushButton(self.page_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(290, 60, 131, 71))
        self.pushButton_13 = QPushButton(self.page_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(430, 60, 131, 71))
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(520, 540, 51, 41))
        icon1 = QIcon()
        icon1.addFile(u"E:/GUI/exit.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_14.setIcon(icon1)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 81, 31))
        self.label_5.setFont(font1)
        self.pushButton_15 = QPushButton(self.page_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 0, 75, 24))
        self.listWidget = QListWidget(self.page_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 210, 561, 271))
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi
        # ~~~无情的占位符~~~ #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # ~~~无情的占位符~~~ #
        # 信号/槽
        self.pushButton_2.clicked.connect(self.application)
        self.pushButton_9.clicked.connect(self.mainpage)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_15.clicked.connect(self.mainpage)
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.listWidget_3.itemClicked.connect(self.itemClick)
        # ~~~无情的占位符~~~ #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # ~~~无情的占位符~~~ #
    def application(self):
        self.stackedWidget.setCurrentIndex(1)

    def mainpage(self):
        self.stackedWidget.setCurrentIndex(0)

    def search(self):
        self.stackedWidget.setCurrentIndex(2)

    def itemClick(self):
        self.pushButton_16.setEnabled(True)

        # ~~~无情的占位符~~~ #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # ~~~无情的占位符~~~ #


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyKernel+", None))
        self.lineEdit.setText(
            QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\uff01\uff08\u793a\u4f8b\u6587\u672c\uff09", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u56fa\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u5e94\u7528    >", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u5e38\u7528", None))
        self.homebutton_1.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.homebutton_2.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.homebutton_4.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.homebutton_3.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.homebutton_5.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.homebutton_6.setText(QCoreApplication.translate("MainWindow", u"\u672a\u56fa\u5b9a", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u70ed\u95e8\u5e94\u7528", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u65e0", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", "", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u6b64\u9879\u56fa\u5b9a\u81f3\u9996\u9875", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c", None))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"PyKernel \u547d\u4ee4\u884c\u6a21\u5f0f", None));
        ___qlistwidgetitem1 = self.listWidget_3.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PyScreenShot \u622a\u5c4f", None));
        ___qlistwidgetitem2 = self.listWidget_3.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PyCal \u8ba1\u7b97\u5668", None));
        ___qlistwidgetitem3 = self.listWidget_3.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PySysInfo \u7cfb\u7edf\u4fe1\u606f", None));
        ___qlistwidgetitem4 = self.listWidget_3.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PyConfig \u63a7\u5236", None));
        ___qlistwidgetitem5 = self.listWidget_3.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PyCC \u8f6c\u6362", None));
        ___qlistwidgetitem6 = self.listWidget_3.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PyMusic \u97f3\u4e50", None));
        ___qlistwidgetitem7 = self.listWidget_3.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"PyRename \u91cd\u547d\u540d\u5de5\u5177", None));
        ___qlistwidgetitem8 = self.listWidget_3.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PyNote \u8bb0\u4e8b\u672c", None));
        ___qlistwidgetitem9 = self.listWidget_3.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PPkg \u5e94\u7528\u5e02\u573a", None));
        ___qlistwidgetitem10 = self.listWidget_3.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"PyRecorder \u5f55\u97f3\u673a", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        # retranslateUi


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
