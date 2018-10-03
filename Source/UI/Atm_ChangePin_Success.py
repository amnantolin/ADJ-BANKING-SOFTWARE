# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_ChangePin_Success.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_ChangePin_Success(object):
    def setupUi(self, Atm_ChangePin_Success):
        Atm_ChangePin_Success.setObjectName("Atm_ChangePin_Success")
        Atm_ChangePin_Success.resize(650, 450)
        Atm_ChangePin_Success.setMinimumSize(QtCore.QSize(650, 450))
        Atm_ChangePin_Success.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_ChangePin_Success.setWindowIcon(icon)
        Atm_ChangePin_Success.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background: transparent;\n"
"background-color:  rgb(30, 30, 30);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 0, 50);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Atm_ChangePin_Success)
        self.label.setGeometry(QtCore.QRect(140, 150, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.okay = QtWidgets.QPushButton(Atm_ChangePin_Success)
        self.okay.setGeometry(QtCore.QRect(260, 300, 120, 40))
        self.okay.setObjectName("okay")
        self.label_2 = QtWidgets.QLabel(Atm_ChangePin_Success)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_2.setMinimumSize(QtCore.QSize(650, 450))
        self.label_2.setMaximumSize(QtCore.QSize(650, 450))
        self.label_2.setStyleSheet("border-image: url(:/images/clientbg1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.okay.raise_()

        self.retranslateUi(Atm_ChangePin_Success)
        QtCore.QMetaObject.connectSlotsByName(Atm_ChangePin_Success)

    def retranslateUi(self, Atm_ChangePin_Success):
        _translate = QtCore.QCoreApplication.translate
        Atm_ChangePin_Success.setWindowTitle(_translate("Atm_ChangePin_Success", "CHANGE PIN SUCCESSFUL"))
        self.label.setText(_translate("Atm_ChangePin_Success", "<html><head/><body><p><span style=\" color:#ffffff;\">Current PIN has been changed successfully!</span></p></body></html>"))
        self.okay.setText(_translate("Atm_ChangePin_Success", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_ChangePin_Success = QtWidgets.QWidget()
    ui = Ui_Atm_ChangePin_Success()
    ui.setupUi(Atm_ChangePin_Success)
    Atm_ChangePin_Success.show()
    sys.exit(app.exec_())

