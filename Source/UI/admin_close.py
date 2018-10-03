# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_close.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_close(object):
    def setupUi(self, admin_close):
        admin_close.setObjectName("admin_close")
        admin_close.resize(650, 450)
        admin_close.setMinimumSize(QtCore.QSize(650, 450))
        admin_close.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_close.setWindowIcon(icon)
        admin_close.setStyleSheet("QWidget#admin_close{\n"
"border-image: url(:images/ad.png);\n"
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
        self.label = QtWidgets.QLabel(admin_close)
        self.label.setGeometry(QtCore.QRect(210, 30, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(admin_close)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 310, 351, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sys_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_delete.setFont(font)
        self.sys_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_delete.setObjectName("sys_delete")
        self.horizontalLayout.addWidget(self.sys_delete)
        self.sys_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_cancel.setFont(font)
        self.sys_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_cancel.setObjectName("sys_cancel")
        self.horizontalLayout.addWidget(self.sys_cancel)
        self.label_4 = QtWidgets.QLabel(admin_close)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 163, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sys_an = QtWidgets.QLineEdit(admin_close)
        self.sys_an.setGeometry(QtCore.QRect(250, 180, 361, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sys_an.setFont(font)
        self.sys_an.setText("")
        self.sys_an.setMaxLength(12)
        self.sys_an.setObjectName("sys_an")

        self.retranslateUi(admin_close)
        QtCore.QMetaObject.connectSlotsByName(admin_close)

    def retranslateUi(self, admin_close):
        _translate = QtCore.QCoreApplication.translate
        admin_close.setWindowTitle(_translate("admin_close", "Close Account"))
        self.label.setText(_translate("admin_close", "<html><head/><body><p><span style=\" color:#ffffff;\">CLOSE ACCOUNT</span></p></body></html>"))
        self.sys_delete.setText(_translate("admin_close", "CONFIRM"))
        self.sys_cancel.setText(_translate("admin_close", "CANCEL"))
        self.label_4.setText(_translate("admin_close", "<html><head/><body><p><span style=\" color:#ffffff;\">ACCOUNT NUMBER:</span></p></body></html>"))
        self.sys_an.setInputMask(_translate("admin_close", "999999999999"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_close = QtWidgets.QWidget()
    ui = Ui_admin_close()
    ui.setupUi(admin_close)
    admin_close.show()
    sys.exit(app.exec_())

