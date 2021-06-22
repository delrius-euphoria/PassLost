import sys, os, sqlite3, make, hash
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (QApplication, QMainWindow, QFileDialog, 
                QMessageBox, QTableWidgetItem, QHeaderView, QMenu)
from ui_splash_screen import Ui_Splash
from ui_main import Ui_MainWindow

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.count = 0

        self.show()

    def progress(self):
        self.ui.progress_bar.setValue(self.count)
        if self.count > 100:
            self.timer.stop()
            self.close()
            app = MainApplication()
            app.show()
        else:
            self.count += 1

class MainApplication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.back2_btn2.clicked.connect(lambda: self.ui.stacked_wid.setCurrentIndex(0))
        self.ui.create_btn.clicked.connect(lambda: self.ui.stacked_wid.setCurrentIndex(1))
        self.ui.back_btn.clicked.connect(lambda: self.ui.stacked_wid.setCurrentIndex(0))
        self.ui.add_btn.clicked.connect(lambda: self.ui.stacked_wid.setCurrentIndex(3))
        self.ui.back_btn3.clicked.connect(lambda: self.ui.stacked_wid.setCurrentIndex(2))
        self.ui.proceed_btn.clicked.connect(lambda: self.validation(self.ui.massterpw_entry.text()))
        
        self.ui.choosepath_btn.clicked.connect(self.create_db)
        self.ui.createdb_btn_2.clicked.connect(self.finalize_db)
        self.ui.choosefile_btn.clicked.connect(self.choose_db)
        self.ui.submit_btn.clicked.connect(self.add)
        
        self.ui.massterpw_entry.returnPressed.connect(lambda: self.validation(self.ui.massterpw_entry.text()))
        self.ui.confirmmasterpw2_entry.returnPressed.connect(self.finalize_db)
        self.ui.url_entry.returnPressed.connect(self.add)

        self.ui.close_lbl.mousePressEvent = lambda e: self.close()
        self.ui.min_lbl.mousePressEvent   = lambda e: self.showMinimized()

        self.file, self.filepath          = None, None
    
    def create_db(self):
        options         = QFileDialog.Options()
        self.filepath,_ = QFileDialog.getSaveFileName(self,"Choose a location to save","",
                    "PassLost Files (*.pl)", options=options)
        if self.filepath:
            self.file   = os.path.basename(self.filepath).split('.')[0]
        
        self.ui.masterpw2_entry.setFocus()

    def finalize_db(self):
        main = self.ui.masterpw2_entry.text()
        conf = self.ui.confirmmasterpw2_entry.text()
        if main == conf:
            self.k,salt = hash.pbkdf(main.encode('utf-8'))
            if self.filepath and self.file:
                make.create(self.filepath,self.file)
                make.update(self.filepath, self.k+salt)
                
                QMessageBox(QMessageBox.Information,'Success','Database has been created').exec_()
                
                self.refresh_page2()
                self.display()
                self.ui.stacked_wid.setCurrentIndex(2)
            else:
                QMessageBox(QMessageBox.Warning,'Error','Please select a path for database first').exec_()
        else:
            QMessageBox(QMessageBox.Warning,'Error','Those passwords do not match, try again').exec_()

    def choose_db(self):
        options         = QFileDialog.Options()
        self.filepath,_ = QFileDialog.getOpenFileName(self,"Choose a database to open","",
                    "PassLost Files (*.pl)", options=options)
        if self.filepath:
            self.file   = os.path.basename(self.filepath).split('.')[0]
            self.ui.choosefile_btn.setText(self.file+'.db')
        
        self.ui.massterpw_entry.setFocus()

    def display(self):
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(['Username','URL/Link'])

        self.ui.table.setRowCount(0)
        self.refresh_table()

        header = self.ui.table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        col    = self.ui.table.verticalHeader()
        col.setVisible(False)
        
        self.ui.table.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if(event.type() == QtCore.QEvent.MouseButtonPress and
           event.buttons() == QtCore.Qt.RightButton and
           source is self.ui.table.viewport()):

            item = self.ui.table.itemAt(event.pos())
            if item is not None:
                menu = QMenu()
                menu.addAction('Copy password',lambda: self.copy(item.row()))
                menu.addAction('Add new',lambda: self.ui.stacked_wid.setCurrentIndex(3))
                menu.exec_(event.globalPos())

        return super().eventFilter(source,event)
    
    def copy(self,pos):
        con = sqlite3.connect(self.filepath)
        c = con.cursor()
        c.execute('SELECT password FROM {} where oid=?'.format(self.file),(pos+1,))
        res = c.fetchone()
        
        pw = hash.unhasher(self.k,res[0])
        
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(pw.decode(),mode=cb.Clipboard)
        
        QMessageBox(QMessageBox.Information,'Success','The password has been copied').exec_()

    def validation(self,pw):
        if self.filepath and self.file:
            con = sqlite3.connect(self.filepath)
            c   = con.cursor()
            c.execute('SELECT * FROM password')
            res = c.fetchone()
            
            self.k,s = res[0][:32],res[0][32:]
            pw  = hash.pbkdf(pw.encode('utf-8'),s)
            
            if self.k == pw[0]:
                self.ui.stacked_wid.setCurrentIndex(2)
                self.refresh_page1()
                self.display()
            else:
                QMessageBox(QMessageBox.Warning,'Error','The master password is incorrect, try again').exec_()
        
        else:
            QMessageBox(QMessageBox.Warning,'Error','Please choose a database first').exec_()

    def add(self):
        user = self.ui.username_entry.text()
        pw   = self.ui.pw_entry.text()
        conf = self.ui.confrimpw_entry.text()
        url  = self.ui.url_entry.text()
        
        if pw == conf and user and url:
            con  = sqlite3.connect(self.filepath)    
            enc = hash.hasher(self.k,pw.encode('utf-8'))
            c = con.cursor()
            c.execute('INSERT INTO {} VALUES (?,?,?)'.format(self.file),(user,enc,url))
            con.commit()

            QMessageBox(QMessageBox.Information,'Success','Details have been entered onto the database').exec_()
            
            self.display()
            self.refresh_page4()
            self.ui.stacked_wid.setCurrentIndex(2)

    def refresh_table(self):
        con = sqlite3.connect(self.filepath)
        c = con.cursor()
        c.execute('SELECT username,url FROM {}'.format(self.file))
        res = c.fetchall()
        
        for row_count,row_data in enumerate(res):
            self.ui.table.insertRow(row_count)
            for column_number, data in enumerate(row_data):
                self.ui.table.setItem(row_count,column_number,QTableWidgetItem(str(data)))

        self.ui.table.setRowCount(len(res))
    
    def mousePressEvent(self, event):
        if event.button() == QtGui.Qt.LeftButton:
            self.m_flag     = True
            self.m_Position = event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QtGui.QCursor(QtGui.Qt.OpenHandCursor))  #Change mouse icon
            
    def mouseMoveEvent(self, QMouseEvent):
        if QtGui.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtGui.Qt.ArrowCursor))

    def refresh_page1(self):
        self.ui.massterpw_entry.setText('')
    
    def refresh_page2(self):
        self.ui.masterpw2_entry.setText('')
        self.ui.confirmmasterpw2_entry.setText('')
    
    def refresh_page4(self):
        self.ui.username_entry.setText('')
        self.ui.pw_entry.setText('')
        self.ui.confrimpw_entry.setText('')
        self.ui.url_entry.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    # window = MainApplication()
    window.show()
    sys.exit(app.exec_())