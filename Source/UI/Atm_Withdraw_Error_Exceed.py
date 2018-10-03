# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Withdraw_Error_Exceed.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Withdraw_Error_Exceed(object):
    def setupUi(self, Atm_Withdraw_Error_Exceed):
        Atm_Withdraw_Error_Exceed.setObjectName("Atm_Withdraw_Error_Exceed")
        Atm_Withdraw_Error_Exceed.resize(650, 450)
        Atm_Withdraw_Error_Exceed.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Withdraw_Error_Exceed.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Withdraw_Error_Exceed.setWindowIcon(icon)
        Atm_Withdraw_Error_Exceed.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_Withdraw_Error_Exceed)
        self.label.setGeometry(QtCore.QRect(100, 150, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Withdraw_Error_Exceed)
        self.label_2.setGeometry(QtCore.QRect(280, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.no = QtWidgets.QPushButton(Atm_Withdraw_Error_Exceed)
        self.no.setGeometry(QtCore.QRect(360, 310, 120, 35))
        self.no.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.no.setObjectName("no")
        self.yes = QtWidgets.QPushButton(Atm_Withdraw_Error_Exceed)
        self.yes.setGeometry(QtCore.QRect(150, 310, 120, 35))
        self.yes.setObjectName("yes")
        self.label_3 = QtWidgets.QLabel(Atm_Withdraw_Error_Exceed)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbgErr.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.no.raise_()
        self.yes.raise_()

        self.retranslateUi(Atm_Withdraw_Error_Exceed)
        QtCore.QMetaObject.connectSlotsByName(Atm_Withdraw_Error_Exceed)

    def retranslateUi(self, Atm_Withdraw_Error_Exceed):
        _translate = QtCore.QCoreApplication.translate
        Atm_Withdraw_Error_Exceed.setWindowTitle(_translate("Atm_Withdraw_Error_Exceed", "WITHDRAW ERROR"))
        self.label.setText(_translate("Atm_Withdraw_Error_Exceed", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">You have exceeded the withdrawal limit per transaction!</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_Withdraw_Error_Exceed", "<html><head/><body><p><span style=\" color:#ffffff;\">Try again?</span></p></body></html>"))
        self.no.setText(_translate("Atm_Withdraw_Error_Exceed", "NO"))
        self.yes.setText(_translate("Atm_Withdraw_Error_Exceed", "YES"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Withdraw_Error_Exceed = QtWidgets.QWidget()
    ui = Ui_Atm_Withdraw_Error_Exceed()
    ui.setupUi(Atm_Withdraw_Error_Exceed)
    Atm_Withdraw_Error_Exceed.show()
    sys.exit(app.exec_())

