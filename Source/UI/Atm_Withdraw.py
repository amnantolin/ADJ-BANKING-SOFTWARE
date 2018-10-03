# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Withdraw.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Withdraw(object):
    def setupUi(self, Atm_Withdraw):
        Atm_Withdraw.setObjectName("Atm_Withdraw")
        Atm_Withdraw.resize(650, 450)
        Atm_Withdraw.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Withdraw.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Withdraw.setWindowIcon(icon)
        Atm_Withdraw.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_Withdraw)
        self.label.setGeometry(QtCore.QRect(250, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.amount = QtWidgets.QLineEdit(Atm_Withdraw)
        self.amount.setGeometry(QtCore.QRect(180, 200, 300, 35))
        self.amount.setObjectName("amount")
        self.confirm = QtWidgets.QPushButton(Atm_Withdraw)
        self.confirm.setGeometry(QtCore.QRect(140, 310, 120, 35))
        self.confirm.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 30, 0);\n"
"color: white;\n"
"}")
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Atm_Withdraw)
        self.cancel.setGeometry(QtCore.QRect(390, 310, 120, 35))
        self.cancel.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.label_2 = QtWidgets.QLabel(Atm_Withdraw)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_2.setMinimumSize(QtCore.QSize(650, 450))
        self.label_2.setMaximumSize(QtCore.QSize(650, 450))
        self.label_2.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.amount.raise_()
        self.confirm.raise_()
        self.cancel.raise_()

        self.retranslateUi(Atm_Withdraw)
        QtCore.QMetaObject.connectSlotsByName(Atm_Withdraw)

    def retranslateUi(self, Atm_Withdraw):
        _translate = QtCore.QCoreApplication.translate
        Atm_Withdraw.setWindowTitle(_translate("Atm_Withdraw", "WITHDRAW"))
        self.label.setText(_translate("Atm_Withdraw", "<html><head/><body><p><span style=\" color:#ffffff;\">Enter Peso Amount</span></p></body></html>"))
        self.amount.setInputMask(_translate("Atm_Withdraw", "0000000000"))
        self.confirm.setText(_translate("Atm_Withdraw", "CONFIRM"))
        self.cancel.setText(_translate("Atm_Withdraw", "CANCEL"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Withdraw = QtWidgets.QWidget()
    ui = Ui_Atm_Withdraw()
    ui.setupUi(Atm_Withdraw)
    Atm_Withdraw.show()
    sys.exit(app.exec_())

