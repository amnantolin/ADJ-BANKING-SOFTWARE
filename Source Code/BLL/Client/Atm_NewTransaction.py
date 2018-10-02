# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_NewTransaction.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_NewTransaction(object):
    def setupUi(self, Atm_NewTransaction):
        Atm_NewTransaction.setObjectName("Atm_NewTransaction")
        Atm_NewTransaction.resize(650, 450)
        Atm_NewTransaction.setMinimumSize(QtCore.QSize(650, 450))
        Atm_NewTransaction.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_NewTransaction.setWindowIcon(icon)
        Atm_NewTransaction.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(Atm_NewTransaction)
        self.label.setGeometry(QtCore.QRect(160, 150, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.newtrans = QtWidgets.QPushButton(Atm_NewTransaction)
        self.newtrans.setGeometry(QtCore.QRect(150, 290, 110, 35))
        self.newtrans.setStyleSheet("\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 30, 0);\n"
"color: white;\n"
"}")
        self.newtrans.setObjectName("newtrans")
        self.exit = QtWidgets.QPushButton(Atm_NewTransaction)
        self.exit.setGeometry(QtCore.QRect(380, 290, 110, 35))
        self.exit.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.exit.setObjectName("exit")
        self.label_2 = QtWidgets.QLabel(Atm_NewTransaction)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_2.setMinimumSize(QtCore.QSize(650, 450))
        self.label_2.setMaximumSize(QtCore.QSize(650, 45))
        self.label_2.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.newtrans.raise_()
        self.exit.raise_()

        self.retranslateUi(Atm_NewTransaction)
        QtCore.QMetaObject.connectSlotsByName(Atm_NewTransaction)

    def retranslateUi(self, Atm_NewTransaction):
        _translate = QtCore.QCoreApplication.translate
        Atm_NewTransaction.setWindowTitle(_translate("Atm_NewTransaction", "NEW TRANSACTION"))
        self.label.setText(_translate("Atm_NewTransaction", "<html><head/><body><p><span style=\" color:#ffffff;\">Do you wish to make another transaction?</span></p></body></html>"))
        self.newtrans.setText(_translate("Atm_NewTransaction", "YES"))
        self.exit.setText(_translate("Atm_NewTransaction", "NO"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_NewTransaction = QtWidgets.QWidget()
    ui = Ui_Atm_NewTransaction()
    ui.setupUi(Atm_NewTransaction)
    Atm_NewTransaction.show()
    sys.exit(app.exec_())

