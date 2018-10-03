# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_Balance.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_Balance(object):
    def setupUi(self, Atm_Balance):
        Atm_Balance.setObjectName("Atm_Balance")
        Atm_Balance.resize(650, 450)
        Atm_Balance.setMinimumSize(QtCore.QSize(650, 450))
        Atm_Balance.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_Balance.setWindowIcon(icon)
        Atm_Balance.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background: white;\n"
"background-color: rgb(30, 30, 30);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 0, 30);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Atm_Balance)
        self.label.setGeometry(QtCore.QRect(240, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.okay = QtWidgets.QPushButton(Atm_Balance)
        self.okay.setGeometry(QtCore.QRect(260, 330, 131, 41))
        self.okay.setObjectName("okay")
        self.bal = QtWidgets.QLineEdit(Atm_Balance)
        self.bal.setGeometry(QtCore.QRect(180, 220, 291, 31))
        self.bal.setReadOnly(True)
        self.bal.setObjectName("bal")
        self.label_2 = QtWidgets.QLabel(Atm_Balance)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_2.setMinimumSize(QtCore.QSize(650, 450))
        self.label_2.setMaximumSize(QtCore.QSize(650, 450))
        self.label_2.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.okay.raise_()
        self.bal.raise_()

        self.retranslateUi(Atm_Balance)
        QtCore.QMetaObject.connectSlotsByName(Atm_Balance)

    def retranslateUi(self, Atm_Balance):
        _translate = QtCore.QCoreApplication.translate
        Atm_Balance.setWindowTitle(_translate("Atm_Balance", "BALANCE INQUIRY"))
        self.label.setText(_translate("Atm_Balance", "<html><head/><body><p><span style=\" color:#ffffff;\">Your current balance:</span></p></body></html>"))
        self.okay.setText(_translate("Atm_Balance", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_Balance = QtWidgets.QWidget()
    ui = Ui_Atm_Balance()
    ui.setupUi(Atm_Balance)
    Atm_Balance.show()
    sys.exit(app.exec_())

