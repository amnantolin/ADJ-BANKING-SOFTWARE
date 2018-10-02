# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atm_ChangePin_Blank.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res1

class Ui_Atm_ChangePin_Blank(object):
    def setupUi(self, Atm_ChangePin_Blank):
        Atm_ChangePin_Blank.setObjectName("Atm_ChangePin_Blank")
        Atm_ChangePin_Blank.resize(650, 450)
        Atm_ChangePin_Blank.setMinimumSize(QtCore.QSize(650, 450))
        Atm_ChangePin_Blank.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Atm_ChangePin_Blank.setWindowIcon(icon)
        Atm_ChangePin_Blank.setStyleSheet("QPushButton{\n"
"background: transparent;\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}\n"
"\n"
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
        self.label = QtWidgets.QLabel(Atm_ChangePin_Blank)
        self.label.setGeometry(QtCore.QRect(220, 130, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Atm_ChangePin_Blank)
        self.label_2.setGeometry(QtCore.QRect(280, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yes = QtWidgets.QPushButton(Atm_ChangePin_Blank)
        self.yes.setGeometry(QtCore.QRect(160, 320, 100, 30))
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QPushButton(Atm_ChangePin_Blank)
        self.no.setGeometry(QtCore.QRect(360, 320, 100, 30))
        self.no.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(80, 0, 0);\n"
"color: white;\n"
"}")
        self.no.setObjectName("no")
        self.label_3 = QtWidgets.QLabel(Atm_ChangePin_Blank)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.label_3.setMinimumSize(QtCore.QSize(650, 450))
        self.label_3.setMaximumSize(QtCore.QSize(650, 450))
        self.label_3.setStyleSheet("border-image: url(:/images/clientbgErr.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.yes.raise_()
        self.no.raise_()

        self.retranslateUi(Atm_ChangePin_Blank)
        QtCore.QMetaObject.connectSlotsByName(Atm_ChangePin_Blank)

    def retranslateUi(self, Atm_ChangePin_Blank):
        _translate = QtCore.QCoreApplication.translate
        Atm_ChangePin_Blank.setWindowTitle(_translate("Atm_ChangePin_Blank", "CHANGE PIN ERROR"))
        self.label.setText(_translate("Atm_ChangePin_Blank", "<html><head/><body><p><span style=\" color:#ffffff;\">Missing field detected!</span></p></body></html>"))
        self.label_2.setText(_translate("Atm_ChangePin_Blank", "<html><head/><body><p><span style=\" color:#ffffff;\">Try again?</span></p></body></html>"))
        self.yes.setText(_translate("Atm_ChangePin_Blank", "YES"))
        self.no.setText(_translate("Atm_ChangePin_Blank", "NO"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atm_ChangePin_Blank = QtWidgets.QWidget()
    ui = Ui_Atm_ChangePin_Blank()
    ui.setupUi(Atm_ChangePin_Blank)
    Atm_ChangePin_Blank.show()
    sys.exit(app.exec_())

