# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Deposit.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Deposit(object):
    def setupUi(self, Atm_Deposit):
        Atm_Deposit.setObjectName("Atm_Deposit")
        Atm_Deposit.resize(650, 450)
        Atm_Deposit.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Deposit.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Deposit.setWindowIcon(icon)
        Atm_Deposit.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: transparent;\n"
"background-color: rgb(30, 30, 30);\n"
"border: 2px solid white;\n"
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
        self.confirm = QtWidgets.QPushButton(Atm_Deposit)
        self.confirm.setGeometry(QtCore.QRect(160, 310, 120, 35))
        self.confirm.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(0, 30, 0);\n"
"color: white;\n"
"}")
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Atm_Deposit)
        self.cancel.setGeometry(QtCore.QRect(390, 310, 120, 35))
        self.cancel.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.amount = QtWidgets.QLineEdit(Atm_Deposit)
        self.amount.setGeometry(QtCore.QRect(180, 190, 300, 35))
        self.amount.setObjectName("amount")
        self.label = QtWidgets.QLabel(Atm_Deposit)
        self.label.setGeometry(QtCore.QRect(260, 130, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Deposit)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_2.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.confirm.raise_()
        self.cancel.raise_()
        self.amount.raise_()
        self.label.raise_()

        self.retranslateUi(Atm_Deposit)
        QtCore.QMetaObject.connectSlotsByName(Atm_Deposit)

    def retranslateUi(self, Atm_Deposit):
        _translate = QtCore.QCoreApplication.translate
        Atm_Deposit.setWindowTitle(_translate("Atm_Deposit", "DEPOSIT"))
        self.confirm.setText(_translate("Atm_Deposit", "CONFIRM"))
        self.cancel.setText(_translate("Atm_Deposit", "CANCEL"))
        self.amount.setInputMask(_translate("Atm_Deposit", "0000000000"))
        self.label.setText(_translate("Atm_Deposit", "<html><head/><body><p><span style=\" color:#ffffff;\">Enter Peso Amount</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Deposit = QtWidgets.QWidget()
    ui = Ui_Atm_Deposit()
    ui.setupUi(Atm_Deposit)
    Atm_Deposit.show()
    sys.exit(app.exec_())

