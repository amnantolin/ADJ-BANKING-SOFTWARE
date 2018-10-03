# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_ChangePin.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_ChangePin(object):
    def setupUi(self, Atm_ChangePin):
        Atm_ChangePin.setObjectName("Atm_ChangePin")
        Atm_ChangePin.resize(650, 450)
        Atm_ChangePin.setMinimumSize(QtCore.QSize(650, 450))
        Atm_ChangePin.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_ChangePin.setWindowIcon(icon)
        Atm_ChangePin.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: white;\n"
"background-color: rgb(30, 30, 30);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 30, 30);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Atm_ChangePin)
        self.label.setGeometry(QtCore.QRect(260, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_ChangePin)
        self.label_2.setGeometry(QtCore.QRect(250, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pin = QtWidgets.QLineEdit(Atm_ChangePin)
        self.pin.setGeometry(QtCore.QRect(190, 160, 280, 30))
        self.pin.setText("")
        self.pin.setMaxLength(6)
        self.pin.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pin.setPlaceholderText("")
        self.pin.setObjectName("pin")
        self.repin = QtWidgets.QLineEdit(Atm_ChangePin)
        self.repin.setGeometry(QtCore.QRect(190, 270, 280, 30))
        self.repin.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.repin.setObjectName("repin")
        self.confirm = QtWidgets.QPushButton(Atm_ChangePin)
        self.confirm.setGeometry(QtCore.QRect(110, 360, 150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 60, 0);\n"
"color: white;\n"
"}")
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Atm_ChangePin)
        self.cancel.setGeometry(QtCore.QRect(400, 360, 150, 40))
        self.cancel.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.label_3 = QtWidgets.QLabel(Atm_ChangePin)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pin.raise_()
        self.repin.raise_()
        self.confirm.raise_()
        self.cancel.raise_()

        self.retranslateUi(Atm_ChangePin)
        QtCore.QMetaObject.connectSlotsByName(Atm_ChangePin)

    def retranslateUi(self, Atm_ChangePin):
        _translate = QtCore.QCoreApplication.translate
        Atm_ChangePin.setWindowTitle(_translate("Atm_ChangePin", "CHANGE PIN"))
        self.label.setText(_translate("Atm_ChangePin", "<html><head/><body><p><span style=\" color:#ffffff;\">Enter your new PIN</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_ChangePin", "<html><head/><body><p><span style=\" color:#ffffff;\">Re-enter your new PIN</span></p></body></html>"))
        self.pin.setInputMask(_translate("Atm_ChangePin", "999999"))
        self.repin.setInputMask(_translate("Atm_ChangePin", "999999"))
        self.confirm.setText(_translate("Atm_ChangePin", "CONFIRM"))
        self.cancel.setText(_translate("Atm_ChangePin", "CANCEL"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_ChangePin = QtWidgets.QWidget()
    ui = Ui_Atm_ChangePin()
    ui.setupUi(Atm_ChangePin)
    Atm_ChangePin.show()
    sys.exit(app.exec_())

