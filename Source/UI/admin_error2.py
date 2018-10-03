# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_error2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_error2(object):
    def setupUi(self, admin_error2):
        admin_error2.setObjectName("admin_error2")
        admin_error2.resize(358, 225)
        admin_error2.setMinimumSize(QtCore.QSize(358, 225))
        admin_error2.setMaximumSize(QtCore.QSize(358, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_error2.setWindowIcon(icon)
        admin_error2.setStyleSheet("QWidget#admin_error2{\n"
"border-image: url(:images/aderr.png);\n"
"}\n"
"\n"
"QPushButton{\n"
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
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_error2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 321, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.sys_ok = QtWidgets.QPushButton(admin_error2)
        self.sys_ok.setGeometry(QtCore.QRect(110, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sys_ok.setFont(font)
        self.sys_ok.setObjectName("sys_ok")
        self.sys_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(admin_error2)
        QtCore.QMetaObject.connectSlotsByName(admin_error2)

    def retranslateUi(self, admin_error2):
        _translate = QtCore.QCoreApplication.translate
        admin_error2.setWindowTitle(_translate("admin_error2", "Warning"))
        self.label.setText(_translate("admin_error2", "<html><head/><body><p><span style=\" color:#ffffff;\">Account Number</span></p></body></html>"))
        self.label_2.setText(_translate("admin_error2", "<html><head/><body><p><span style=\" color:#ffffff;\">Doesn\'t Exist, Try Again!</span></p></body></html>"))
        self.sys_ok.setText(_translate("admin_error2", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_error2 = QtWidgets.QWidget()
    ui = Ui_admin_error2()
    ui.setupUi(admin_error2)
    admin_error2.show()
    sys.exit(app.exec_())

