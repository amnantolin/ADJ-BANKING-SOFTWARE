# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Login_Error_Max.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Login_Error_Max(object):
    def setupUi(self, Atm_Login_Error_Max):
        Atm_Login_Error_Max.setObjectName("Atm_Login_Error_Max")
        Atm_Login_Error_Max.resize(650, 450)
        Atm_Login_Error_Max.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Login_Error_Max.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Login_Error_Max.setWindowIcon(icon)
        Atm_Login_Error_Max.setStyleSheet("QPushButton{\n"
"background: transparent;\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 30, 30);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Atm_Login_Error_Max)
        self.label.setGeometry(QtCore.QRect(110, 160, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Login_Error_Max)
        self.label_2.setGeometry(QtCore.QRect(250, 240, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.okay = QtWidgets.QPushButton(Atm_Login_Error_Max)
        self.okay.setGeometry(QtCore.QRect(270, 320, 110, 35))
        self.okay.setObjectName("okay")
        self.label_3 = QtWidgets.QLabel(Atm_Login_Error_Max)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbgErr.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.okay.raise_()

        self.retranslateUi(Atm_Login_Error_Max)
        QtCore.QMetaObject.connectSlotsByName(Atm_Login_Error_Max)

    def retranslateUi(self, Atm_Login_Error_Max):
        _translate = QtCore.QCoreApplication.translate
        Atm_Login_Error_Max.setWindowTitle(_translate("Atm_Login_Error_Max", "MAX LOGIN ERROR ATTEMPTS"))
        self.label.setText(_translate("Atm_Login_Error_Max", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">You have exceeded the maximum number of LOGIN attempts!</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_Login_Error_Max", "<html><head/><body><p><span style=\" color:#ffffff;\">Session is terminated</span></p></body></html>"))
        self.okay.setText(_translate("Atm_Login_Error_Max", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Login_Error_Max = QtWidgets.QWidget()
    ui = Ui_Atm_Login_Error_Max()
    ui.setupUi(Atm_Login_Error_Max)
    Atm_Login_Error_Max.show()
    sys.exit(app.exec_())

