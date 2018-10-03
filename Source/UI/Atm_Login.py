# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Login.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Login(object):
    def setupUi(self, Atm_Login):
        Atm_Login.setObjectName("Atm_Login")
        Atm_Login.resize(650, 450)
        Atm_Login.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Login.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Login.setWindowIcon(icon)
        Atm_Login.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: transparent;\n"
"background-color: rgb(30, 30, 30);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 0, 30);\n"
"color: white;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Atm_Login)
        self.label.setGeometry(QtCore.QRect(100, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Login)
        self.label_2.setGeometry(QtCore.QRect(100, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.card = QtWidgets.QLineEdit(Atm_Login)
        self.card.setGeometry(QtCore.QRect(260, 220, 300, 30))
        self.card.setMaxLength(16)
        self.card.setObjectName("card")
        self.pin = QtWidgets.QLineEdit(Atm_Login)
        self.pin.setGeometry(QtCore.QRect(260, 270, 300, 30))
        self.pin.setMaxLength(6)
        self.pin.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pin.setObjectName("pin")
        self.log = QtWidgets.QPushButton(Atm_Login)
        self.log.setGeometry(QtCore.QRect(260, 370, 120, 40))
        self.log.setObjectName("log")
        self.label_3 = QtWidgets.QLabel(Atm_Login)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbglog.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Atm_Login)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 101, 111))
        self.label_4.setStyleSheet("image: url(:/images/logo.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.card.raise_()
        self.pin.raise_()
        self.log.raise_()
        self.label_4.raise_()

        self.retranslateUi(Atm_Login)
        QtCore.QMetaObject.connectSlotsByName(Atm_Login)

    def retranslateUi(self, Atm_Login):
        _translate = QtCore.QCoreApplication.translate
        Atm_Login.setWindowTitle(_translate("Atm_Login", "ATM LOGIN"))
        self.label.setText(_translate("Atm_Login", "<html><head/><body><p><span style=\" color:#ffffff;\">CARD NUMBER</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_Login", "<html><head/><body><p><span style=\" color:#ffffff;\">PIN</span></p></body></html>"))
        self.card.setInputMask(_translate("Atm_Login", "9999999999999999"))
        self.pin.setInputMask(_translate("Atm_Login", "000000"))
        self.log.setText(_translate("Atm_Login", "LOGIN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Login = QtWidgets.QWidget()
    ui = Ui_Atm_Login()
    ui.setupUi(Atm_Login)
    Atm_Login.show()
    sys.exit(app.exec_())

