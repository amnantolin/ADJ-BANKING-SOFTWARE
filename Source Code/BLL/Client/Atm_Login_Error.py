# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Login_Error.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Login_Error(object):
    def setupUi(self, Atm_Login_Error):
        Atm_Login_Error.setObjectName("Atm_Login_Error")
        Atm_Login_Error.resize(650, 450)
        Atm_Login_Error.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Login_Error.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Login_Error.setWindowIcon(icon)
        Atm_Login_Error.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_Login_Error)
        self.label.setGeometry(QtCore.QRect(200, 140, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ok = QtWidgets.QPushButton(Atm_Login_Error)
        self.ok.setGeometry(QtCore.QRect(270, 300, 110, 35))
        self.ok.setObjectName("ok")
        self.label_3 = QtWidgets.QLabel(Atm_Login_Error)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbgErr.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Atm_Login_Error)
        self.label_2.setGeometry(QtCore.QRect(270, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3.raise_()
        self.label.raise_()
        self.ok.raise_()
        self.label_2.raise_()

        self.retranslateUi(Atm_Login_Error)
        QtCore.QMetaObject.connectSlotsByName(Atm_Login_Error)

    def retranslateUi(self, Atm_Login_Error):
        _translate = QtCore.QCoreApplication.translate
        Atm_Login_Error.setWindowTitle(_translate("Atm_Login_Error", "LOGIN ERROR"))
        self.label.setText(_translate("Atm_Login_Error", "<html><head/><body><p><span style=\" color:#ffffff;\">Invalid CARD NUMBER and/or PIN!</span></p></body></html>"))
        self.ok.setText(_translate("Atm_Login_Error", "OK"))
        self.label_2.setText(_translate("Atm_Login_Error", "<html><head/><body><p><span style=\" color:#ffffff;\">Please Try Again</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Login_Error = QtWidgets.QWidget()
    ui = Ui_Atm_Login_Error()
    ui.setupUi(Atm_Login_Error)
    Atm_Login_Error.show()
    sys.exit(app.exec_())

