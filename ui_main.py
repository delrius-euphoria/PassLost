# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainuiTOYrwH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(814, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 40, 791, 581))
        self.frame.setStyleSheet(u"\n"
"border-radius: 10px;\n"
"\n"
"\n"
"background-color: rgb(56, 58, 89)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stacked_wid = QStackedWidget(self.frame)
        self.stacked_wid.setObjectName(u"stacked_wid")
        self.opendb_page = QWidget()
        self.opendb_page.setObjectName(u"opendb_page")
        self.heading_page1 = QLabel(self.opendb_page)
        self.heading_page1.setObjectName(u"heading_page1")
        self.heading_page1.setGeometry(QRect(-10, 70, 771, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(24)
        self.heading_page1.setFont(font)
        self.heading_page1.setStyleSheet(u"color: rgb(254, 121, 199)")
        self.heading_page1.setAlignment(Qt.AlignCenter)
        self.choosedb_label = QLabel(self.opendb_page)
        self.choosedb_label.setObjectName(u"choosedb_label")
        self.choosedb_label.setGeometry(QRect(130, 160, 261, 51))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.choosedb_label.setFont(font1)
        self.choosedb_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.choosedb_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.choosefile_btn = QPushButton(self.opendb_page)
        self.choosefile_btn.setObjectName(u"choosefile_btn")
        self.choosefile_btn.setGeometry(QRect(440, 170, 161, 28))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.choosefile_btn.setFont(font2)
        self.choosefile_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.masterpw_label = QLabel(self.opendb_page)
        self.masterpw_label.setObjectName(u"masterpw_label")
        self.masterpw_label.setGeometry(QRect(130, 240, 261, 51))
        self.masterpw_label.setFont(font1)
        self.masterpw_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.masterpw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.massterpw_entry = QLineEdit(self.opendb_page)
        self.massterpw_entry.setObjectName(u"massterpw_entry")
        self.massterpw_entry.setGeometry(QRect(440, 250, 161, 31))
        self.massterpw_entry.setFont(font2)
        self.massterpw_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.massterpw_entry.setEchoMode(QLineEdit.Password)
        self.or_label = QLabel(self.opendb_page)
        self.or_label.setObjectName(u"or_label")
        self.or_label.setGeometry(QRect(260, 370, 261, 51))
        self.or_label.setFont(font1)
        self.or_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.or_label.setAlignment(Qt.AlignCenter)
        self.newdb_label = QLabel(self.opendb_page)
        self.newdb_label.setObjectName(u"newdb_label")
        self.newdb_label.setGeometry(QRect(130, 440, 261, 51))
        self.newdb_label.setFont(font1)
        self.newdb_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.newdb_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.create_btn = QPushButton(self.opendb_page)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setGeometry(QRect(440, 450, 161, 28))
        self.create_btn.setFont(font2)
        self.create_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.proceed_btn = QPushButton(self.opendb_page)
        self.proceed_btn.setObjectName(u"proceed_btn")
        self.proceed_btn.setGeometry(QRect(310, 310, 161, 28))
        self.proceed_btn.setFont(font2)
        self.proceed_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.stacked_wid.addWidget(self.opendb_page)
        self.createdb_page = QWidget()
        self.createdb_page.setObjectName(u"createdb_page")
        self.heading_page2 = QLabel(self.createdb_page)
        self.heading_page2.setObjectName(u"heading_page2")
        self.heading_page2.setGeometry(QRect(-10, 70, 781, 51))
        self.heading_page2.setFont(font)
        self.heading_page2.setStyleSheet(u"color: rgb(254, 121, 199)")
        self.heading_page2.setAlignment(Qt.AlignCenter)
        self.choosepath_label = QLabel(self.createdb_page)
        self.choosepath_label.setObjectName(u"choosepath_label")
        self.choosepath_label.setGeometry(QRect(130, 160, 261, 51))
        self.choosepath_label.setFont(font1)
        self.choosepath_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.choosepath_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.choosepath_btn = QPushButton(self.createdb_page)
        self.choosepath_btn.setObjectName(u"choosepath_btn")
        self.choosepath_btn.setGeometry(QRect(440, 170, 161, 28))
        self.choosepath_btn.setFont(font2)
        self.choosepath_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.masterpw_lbl = QLabel(self.createdb_page)
        self.masterpw_lbl.setObjectName(u"masterpw_lbl")
        self.masterpw_lbl.setGeometry(QRect(130, 240, 261, 51))
        self.masterpw_lbl.setFont(font1)
        self.masterpw_lbl.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.masterpw_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.masterpw2_entry = QLineEdit(self.createdb_page)
        self.masterpw2_entry.setObjectName(u"masterpw2_entry")
        self.masterpw2_entry.setGeometry(QRect(440, 250, 161, 31))
        self.masterpw2_entry.setFont(font2)
        self.masterpw2_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.masterpw2_entry.setEchoMode(QLineEdit.Password)
        self.confirmmasterpw_label = QLabel(self.createdb_page)
        self.confirmmasterpw_label.setObjectName(u"confirmmasterpw_label")
        self.confirmmasterpw_label.setGeometry(QRect(130, 320, 281, 51))
        self.confirmmasterpw_label.setFont(font1)
        self.confirmmasterpw_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.confirmmasterpw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confirmmasterpw2_entry = QLineEdit(self.createdb_page)
        self.confirmmasterpw2_entry.setObjectName(u"confirmmasterpw2_entry")
        self.confirmmasterpw2_entry.setGeometry(QRect(440, 330, 161, 31))
        self.confirmmasterpw2_entry.setFont(font2)
        self.confirmmasterpw2_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.confirmmasterpw2_entry.setEchoMode(QLineEdit.Password)
        self.createdb_btn_2 = QPushButton(self.createdb_page)
        self.createdb_btn_2.setObjectName(u"createdb_btn_2")
        self.createdb_btn_2.setGeometry(QRect(390, 430, 161, 28))
        self.createdb_btn_2.setFont(font2)
        self.createdb_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.back_btn = QPushButton(self.createdb_page)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setEnabled(True)
        self.back_btn.setGeometry(QRect(190, 430, 161, 28))
        self.back_btn.setFont(font2)
        self.back_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.stacked_wid.addWidget(self.createdb_page)
        self.display_page = QWidget()
        self.display_page.setObjectName(u"display_page")
        self.display_page.setAutoFillBackground(False)
        self.table = QTableWidget(self.display_page)
        if (self.table.rowCount() < 1):
            self.table.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(-10, 60, 771, 421))
        self.table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: white;\n"
"    font-size: 14pt;\n"
"    color: rgb(254, 121, 199);\n"
"}\n"
"QTableWidget::item{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"	padding: 10px\n"
"}")
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setProperty("showSortIndicator", True)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.back2_btn2 = QPushButton(self.display_page)
        self.back2_btn2.setObjectName(u"back2_btn2")
        self.back2_btn2.setGeometry(QRect(170, 520, 161, 28))
        self.back2_btn2.setFont(font2)
        self.back2_btn2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.add_btn = QPushButton(self.display_page)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(400, 520, 161, 28))
        self.add_btn.setFont(font2)
        self.add_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.stacked_wid.addWidget(self.display_page)
        self.addnew_page = QWidget()
        self.addnew_page.setObjectName(u"addnew_page")
        self.heading_page_4 = QLabel(self.addnew_page)
        self.heading_page_4.setObjectName(u"heading_page_4")
        self.heading_page_4.setGeometry(QRect(-10, 70, 771, 51))
        self.heading_page_4.setFont(font)
        self.heading_page_4.setStyleSheet(u"color: rgb(254, 121, 199)")
        self.heading_page_4.setAlignment(Qt.AlignCenter)
        self.username_entry = QLineEdit(self.addnew_page)
        self.username_entry.setObjectName(u"username_entry")
        self.username_entry.setGeometry(QRect(440, 170, 161, 31))
        self.username_entry.setFont(font2)
        self.username_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.username_entry.setEchoMode(QLineEdit.Normal)
        self.username_entry.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username_label = QLabel(self.addnew_page)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(130, 160, 261, 51))
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.username_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pw_entry = QLineEdit(self.addnew_page)
        self.pw_entry.setObjectName(u"pw_entry")
        self.pw_entry.setGeometry(QRect(440, 250, 161, 31))
        self.pw_entry.setFont(font2)
        self.pw_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.pw_entry.setEchoMode(QLineEdit.Password)
        self.pw_label = QLabel(self.addnew_page)
        self.pw_label.setObjectName(u"pw_label")
        self.pw_label.setGeometry(QRect(130, 240, 261, 51))
        self.pw_label.setFont(font1)
        self.pw_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.pw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confrimpw_entry = QLineEdit(self.addnew_page)
        self.confrimpw_entry.setObjectName(u"confrimpw_entry")
        self.confrimpw_entry.setGeometry(QRect(440, 330, 161, 31))
        self.confrimpw_entry.setFont(font2)
        self.confrimpw_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.confrimpw_entry.setEchoMode(QLineEdit.Password)
        self.confirmpw_label = QLabel(self.addnew_page)
        self.confirmpw_label.setObjectName(u"confirmpw_label")
        self.confirmpw_label.setGeometry(QRect(130, 320, 261, 51))
        self.confirmpw_label.setFont(font1)
        self.confirmpw_label.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.confirmpw_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.url_entry = QLineEdit(self.addnew_page)
        self.url_entry.setObjectName(u"url_entry")
        self.url_entry.setGeometry(QRect(440, 410, 161, 31))
        self.url_entry.setFont(font2)
        self.url_entry.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid rgb(254, 121, 199);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.url_entry.setEchoMode(QLineEdit.Normal)
        self.url_entry.setDragEnabled(False)
        self.url_entry.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.url_lbl = QLabel(self.addnew_page)
        self.url_lbl.setObjectName(u"url_lbl")
        self.url_lbl.setGeometry(QRect(130, 400, 261, 51))
        self.url_lbl.setFont(font1)
        self.url_lbl.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.url_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.submit_btn = QPushButton(self.addnew_page)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(400, 490, 161, 28))
        self.submit_btn.setFont(font2)
        self.submit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.back_btn3 = QPushButton(self.addnew_page)
        self.back_btn3.setObjectName(u"back_btn3")
        self.back_btn3.setGeometry(QRect(200, 490, 161, 28))
        self.back_btn3.setFont(font2)
        self.back_btn3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: rgb(254, 121, 199);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(254, 121, 199);\n"
"	color: white;	\n"
"}")
        self.stacked_wid.addWidget(self.addnew_page)

        self.verticalLayout_2.addWidget(self.stacked_wid)

        self.close_panel = QFrame(self.centralwidget)
        self.close_panel.setObjectName(u"close_panel")
        self.close_panel.setGeometry(QRect(10, 20, 791, 41))
        self.close_panel.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	border-radius: 10px\n"
"}")
        self.close_panel.setFrameShape(QFrame.StyledPanel)
        self.close_panel.setFrameShadow(QFrame.Raised)
        self.close_lbl = QLabel(self.close_panel)
        self.close_lbl.setObjectName(u"close_lbl")
        self.close_lbl.setGeometry(QRect(750, 10, 21, 31))
        font3 = QFont()
        font3.setPointSize(15)
        self.close_lbl.setFont(font3)
        self.close_lbl.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"}\n"
"QLabel:hover{\n"
"color: rgb(254, 121, 199);\n"
"}")
        self.min_lbl = QLabel(self.close_panel)
        self.min_lbl.setObjectName(u"min_lbl")
        self.min_lbl.setGeometry(QRect(720, 10, 21, 31))
        self.min_lbl.setFont(font3)
        self.min_lbl.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"}\n"
"QLabel:hover{\n"
"color: rgb(254, 121, 199);\n"
"}")
        self.title_lbl = QLabel(self.close_panel)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(40, 10, 91, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        self.title_lbl.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_wid.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.heading_page1.setText(QCoreApplication.translate("MainWindow", u"<strong>Select</strong> Database", None))
        self.choosedb_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Choose</span> Database:</p></body></html>", None))
        self.choosefile_btn.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.masterpw_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Master</span> Password:</p></body></html>", None))
        self.massterpw_entry.setText("")
        self.or_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">OR</span></p></body></html>", None))
        self.newdb_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Create</span> New Database?</p></body></html>", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"Create ", None))
        self.proceed_btn.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.heading_page2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Create</span> Database</p></body></html>", None))
        self.choosepath_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Choose</span> Path:</p></body></html>", None))
        self.choosepath_btn.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.masterpw_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Master</span> Password: </p></body></html>", None))
        self.masterpw2_entry.setText("")
        self.confirmmasterpw_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Confirm</span> Master Password: </p></body></html>", None))
        self.confirmmasterpw2_entry.setText("")
        self.createdb_btn_2.setText(QCoreApplication.translate("MainWindow", u"Create Database", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.back2_btn2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.heading_page_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Add</span> New</p></body></html>", None))
        self.username_entry.setInputMask("")
        self.username_entry.setText("")
        self.username_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"johndave12", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Username</span>:</p></body></html>", None))
        self.pw_entry.setText("")
        self.pw_entry.setPlaceholderText("")
        self.pw_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Password</span>:</p></body></html>", None))
        self.confrimpw_entry.setText("")
        self.confirmpw_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Confirm</span> Password:</p></body></html>", None))
        self.url_entry.setText("")
        self.url_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"instagram.com", None))
        self.url_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">URL</span>/Link:</p></body></html>", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.back_btn3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.close_lbl.setText(QCoreApplication.translate("MainWindow", u"<p>&#x2715;</p>", None))
        self.min_lbl.setText(QCoreApplication.translate("MainWindow", u"<p>&minus;</p>", None))
        self.title_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#fe79c7;\">Pass</span><span style=\" color:#fe79c7;\">Lost</span></p></body></html>", None))
    # retranslateUi

