# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Transactions.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Transactions(object):
    def setupUi(self, Atm_Transactions):
        Atm_Transactions.setObjectName("Atm_Transactions")
        Atm_Transactions.resize(650, 450)
        Atm_Transactions.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Transactions.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Transactions.setWindowIcon(icon)
        Atm_Transactions.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: white;\n"
"background-color: rgb(30, 0, 50);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(40, 40, 40);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.deposit = QtWidgets.QPushButton(Atm_Transactions)
        self.deposit.setGeometry(QtCore.QRect(240, 100, 160, 45))
        self.deposit.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.deposit.setObjectName("deposit")
        self.withdraw = QtWidgets.QPushButton(Atm_Transactions)
        self.withdraw.setGeometry(QtCore.QRect(240, 160, 160, 45))
        self.withdraw.setObjectName("withdraw")
        self.balance = QtWidgets.QPushButton(Atm_Transactions)
        self.balance.setGeometry(QtCore.QRect(240, 220, 160, 45))
        self.balance.setObjectName("balance")
        self.changepin = QtWidgets.QPushButton(Atm_Transactions)
        self.changepin.setGeometry(QtCore.QRect(240, 280, 160, 45))
        self.changepin.setObjectName("changepin")
        self.logout = QtWidgets.QPushButton(Atm_Transactions)
        self.logout.setGeometry(QtCore.QRect(40, 380, 130, 30))
        self.logout.setStyleSheet("QPushButton{\n"
"color: black;\n"
"background: gray;\n"
"background-color: gray;\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.logout.setObjectName("logout")
        self.label = QtWidgets.QLabel(Atm_Transactions)
        self.label.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label.setMinimumSize(QtCore.QSize(650, 450))
        self.label.setMaximumSize(QtCore.QSize(650, 450))
        self.label.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.deposit.raise_()
        self.withdraw.raise_()
        self.balance.raise_()
        self.changepin.raise_()
        self.logout.raise_()

        self.retranslateUi(Atm_Transactions)
        QtCore.QMetaObject.connectSlotsByName(Atm_Transactions)

    def retranslateUi(self, Atm_Transactions):
        _translate = QtCore.QCoreApplication.translate
        Atm_Transactions.setWindowTitle(_translate("Atm_Transactions", "ATM TRANSACTIONS"))
        self.deposit.setText(_translate("Atm_Transactions", "DEPOSIT"))
        self.withdraw.setText(_translate("Atm_Transactions", "WITHDRAW"))
        self.balance.setText(_translate("Atm_Transactions", "BALANCE INQUIRY"))
        self.changepin.setText(_translate("Atm_Transactions", "CHANGE PIN"))
        self.logout.setText(_translate("Atm_Transactions", "LOGOUT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Transactions = QtWidgets.QWidget()
    ui = Ui_Atm_Transactions()
    ui.setupUi(Atm_Transactions)
    Atm_Transactions.show()
    sys.exit(app.exec_())

