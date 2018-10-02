# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Withdraw_Error_Insuff.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Withdraw_Error_Insuff(object):
    def setupUi(self, Atm_Withdraw_Error_Insuff):
        Atm_Withdraw_Error_Insuff.setObjectName("Atm_Withdraw_Error_Insuff")
        Atm_Withdraw_Error_Insuff.resize(650, 450)
        Atm_Withdraw_Error_Insuff.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Withdraw_Error_Insuff.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Withdraw_Error_Insuff.setWindowIcon(icon)
        Atm_Withdraw_Error_Insuff.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_Withdraw_Error_Insuff)
        self.label.setGeometry(QtCore.QRect(230, 130, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_Withdraw_Error_Insuff)
        self.label_2.setGeometry(QtCore.QRect(280, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.no = QtWidgets.QPushButton(Atm_Withdraw_Error_Insuff)
        self.no.setGeometry(QtCore.QRect(350, 300, 120, 35))
        self.no.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.no.setObjectName("no")
        self.yes = QtWidgets.QPushButton(Atm_Withdraw_Error_Insuff)
        self.yes.setGeometry(QtCore.QRect(160, 300, 120, 35))
        self.yes.setObjectName("yes")
        self.label_3 = QtWidgets.QLabel(Atm_Withdraw_Error_Insuff)
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

        self.retranslateUi(Atm_Withdraw_Error_Insuff)
        QtCore.QMetaObject.connectSlotsByName(Atm_Withdraw_Error_Insuff)

    def retranslateUi(self, Atm_Withdraw_Error_Insuff):
        _translate = QtCore.QCoreApplication.translate
        Atm_Withdraw_Error_Insuff.setWindowTitle(_translate("Atm_Withdraw_Error_Insuff", "WITHDRAW ERROR"))
        self.label.setText(_translate("Atm_Withdraw_Error_Insuff", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Insufficient Balance!</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_Withdraw_Error_Insuff", "<html><head/><body><p><span style=\" color:#ffffff;\">Try again?</span></p></body></html>"))
        self.no.setText(_translate("Atm_Withdraw_Error_Insuff", "NO"))
        self.yes.setText(_translate("Atm_Withdraw_Error_Insuff", "YES"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Withdraw_Error_Insuff = QtWidgets.QWidget()
    ui = Ui_Atm_Withdraw_Error_Insuff()
    ui.setupUi(Atm_Withdraw_Error_Insuff)
    Atm_Withdraw_Error_Insuff.show()
    sys.exit(app.exec_())

