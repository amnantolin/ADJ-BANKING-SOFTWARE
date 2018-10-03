# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_log.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_log(object):
    def setupUi(self, admin_log):
        admin_log.setObjectName("admin_log")
        admin_log.resize(650, 450)
        admin_log.setMinimumSize(QtCore.QSize(650, 450))
        admin_log.setMaximumSize(QtCore.QSize(650, 450))
        admin_log.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_log.setWindowIcon(icon)
        admin_log.setStyleSheet("QWidget#centralwidget{\n"
"border-image: url(:/images/adlog.png);\n"
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
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(admin_log)
        self.centralwidget.setObjectName("centralwidget")
        self.sys_log = QtWidgets.QPushButton(self.centralwidget)
        self.sys_log.setGeometry(QtCore.QRect(240, 350, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sys_log.setFont(font)
        self.sys_log.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_log.setStyleSheet("")
        self.sys_log.setObjectName("sys_log")
        self.sys_username = QtWidgets.QLineEdit(self.centralwidget)
        self.sys_username.setGeometry(QtCore.QRect(230, 210, 321, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sys_username.setFont(font)
        self.sys_username.setStyleSheet("")
        self.sys_username.setText("")
        self.sys_username.setMaxLength(15)
        self.sys_username.setFrame(True)
        self.sys_username.setCursorPosition(15)
        self.sys_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sys_username.setReadOnly(False)
        self.sys_username.setPlaceholderText("")
        self.sys_username.setObjectName("sys_username")
        self.sys_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.sys_pass.setGeometry(QtCore.QRect(230, 270, 321, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sys_pass.setFont(font)
        self.sys_pass.setStyleSheet("")
        self.sys_pass.setInputMask("")
        self.sys_pass.setMaxLength(20)
        self.sys_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sys_pass.setObjectName("sys_pass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 190, 129, 76))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 129, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 111, 151))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        admin_log.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_log)
        QtCore.QMetaObject.connectSlotsByName(admin_log)

    def retranslateUi(self, admin_log):
        _translate = QtCore.QCoreApplication.translate
        admin_log.setWindowTitle(_translate("admin_log", "Admin Login"))
        self.sys_log.setText(_translate("admin_log", "LOG-IN"))
        self.sys_username.setInputMask(_translate("admin_log", "NNNNNNNNNNNNNNN"))
        self.label.setText(_translate("admin_log", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">USERNAME:</span></p></body></html>"))
        self.label_2.setText(_translate("admin_log", "<html><head/><body><p><span style=\" color:#ffffff;\">PASSWORD:</span></p></body></html>"))
        self.label_3.setText(_translate("admin_log", "<html><head/><body><p><img src=\":/images/logo.png\"/></p></body></html>"))
        self.label_4.setText(_translate("admin_log", "<html><head/><body><p><span style=\" font-size:26pt; text-decoration: underline; color:#b5b5b5;\">ADJ BANKING SOFTWARE</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_log = QtWidgets.QMainWindow()
    ui = Ui_admin_log()
    ui.setupUi(admin_log)
    admin_log.show()
    sys.exit(app.exec_())

