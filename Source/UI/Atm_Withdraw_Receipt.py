# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Withdraw_Receipt.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Withdraw_Receipt(object):
    def setupUi(self, Atm_Withdraw_Receipt):
        Atm_Withdraw_Receipt.setObjectName("Atm_Withdraw_Receipt")
        Atm_Withdraw_Receipt.resize(650, 450)
        Atm_Withdraw_Receipt.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Withdraw_Receipt.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Withdraw_Receipt.setWindowIcon(icon)
        Atm_Withdraw_Receipt.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_Withdraw_Receipt)
        self.label.setGeometry(QtCore.QRect(80, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Withdraw_Receipt)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.amnt = QtWidgets.QLineEdit(Atm_Withdraw_Receipt)
        self.amnt.setGeometry(QtCore.QRect(260, 160, 300, 35))
        self.amnt.setReadOnly(True)
        self.amnt.setObjectName("amnt")
        self.bal = QtWidgets.QLineEdit(Atm_Withdraw_Receipt)
        self.bal.setGeometry(QtCore.QRect(260, 230, 300, 30))
        self.bal.setReadOnly(True)
        self.bal.setObjectName("bal")
        self.okay = QtWidgets.QPushButton(Atm_Withdraw_Receipt)
        self.okay.setGeometry(QtCore.QRect(260, 320, 120, 35))
        self.okay.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 0, 30);\n"
"color: white;\n"
"}")
        self.okay.setObjectName("okay")
        self.label_3 = QtWidgets.QLabel(Atm_Withdraw_Receipt)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.amnt.raise_()
        self.bal.raise_()
        self.okay.raise_()

        self.retranslateUi(Atm_Withdraw_Receipt)
        QtCore.QMetaObject.connectSlotsByName(Atm_Withdraw_Receipt)

    def retranslateUi(self, Atm_Withdraw_Receipt):
        _translate = QtCore.QCoreApplication.translate
        Atm_Withdraw_Receipt.setWindowTitle(_translate("Atm_Withdraw_Receipt", "WITHDRAW RECEIPT"))
        self.label.setText(_translate("Atm_Withdraw_Receipt", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Amount Withdraw:</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_Withdraw_Receipt", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Current Balance:</span></p></body></html>"))
        self.okay.setText(_translate("Atm_Withdraw_Receipt", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Withdraw_Receipt = QtWidgets.QWidget()
    ui = Ui_Atm_Withdraw_Receipt()
    ui.setupUi(Atm_Withdraw_Receipt)
    Atm_Withdraw_Receipt.show()
    sys.exit(app.exec_())

