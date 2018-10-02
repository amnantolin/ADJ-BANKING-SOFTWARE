# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_error3.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_error3(object):
    def setupUi(self, admin_error3):
        admin_error3.setObjectName("admin_error3")
        admin_error3.resize(358, 225)
        admin_error3.setMinimumSize(QtCore.QSize(358, 225))
        admin_error3.setMaximumSize(QtCore.QSize(358, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_error3.setWindowIcon(icon)
        admin_error3.setStyleSheet("QWidget#admin_error3{\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_error3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 300, 81))
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
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.sys_ok = QtWidgets.QPushButton(admin_error3)
        self.sys_ok.setGeometry(QtCore.QRect(120, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sys_ok.setFont(font)
        self.sys_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_ok.setObjectName("sys_ok")

        self.retranslateUi(admin_error3)
        QtCore.QMetaObject.connectSlotsByName(admin_error3)

    def retranslateUi(self, admin_error3):
        _translate = QtCore.QCoreApplication.translate
        admin_error3.setWindowTitle(_translate("admin_error3", "Warning"))
        self.label.setText(_translate("admin_error3", "<html><head/><body><p><span style=\" color:#ffffff;\">Missing Field/s Detected!</span></p></body></html>"))
        self.label_3.setText(_translate("admin_error3", "<html><head/><body><p><span style=\" color:#ffffff;\">Try again</span></p></body></html>"))
        self.sys_ok.setText(_translate("admin_error3", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_error3 = QtWidgets.QWidget()
    ui = Ui_admin_error3()
    ui.setupUi(admin_error3)
    admin_error3.show()
    sys.exit(app.exec_())

