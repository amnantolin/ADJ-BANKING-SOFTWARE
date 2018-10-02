from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer

import sys
import reso
import time
class cssden(QMainWindow):
    def __init__(self):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.WindowStaysOnTopHint)

        # label
        self.lbl = QLabel(self)
        self.lbl.setStyleSheet("image: url(:/images/sp_screen.png);")
        self.lbl.setGeometry(10, 10, 535, 550)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        #size
        self.setFixedSize(550, 550)
        #self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setStyleSheet("background-color: transparent;")
        self.center

        self.show()





        QtCore.QTimer.singleShot(5000, self.close)



    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())
