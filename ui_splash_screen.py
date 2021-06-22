# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screentUaLZy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Splash(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.shadow = QFrame(self.centralwidget)
        self.shadow.setObjectName(u"shadow")
        self.shadow.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px\n"
"}")
        self.shadow.setFrameShape(QFrame.StyledPanel)
        self.shadow.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.shadow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 130, 751, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(254, 121, 199)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.shadow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 210, 751, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progress_bar = QProgressBar(self.shadow)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(50, 350, 651, 23))
        self.progress_bar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200,200,200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.483, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	border-style: none;\n"
"	border-radius: 8px\n"
"}")
        self.progress_bar.setValue(24)
        self.label_3 = QLabel(self.shadow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 420, 751, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.shadow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<strong>Pass</strong>Lost", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Simple</span> password manager</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Created by <span style=\" font-weight:600;\">NihaalNz</span></p></body></html>", None))
    # retranslateUi

