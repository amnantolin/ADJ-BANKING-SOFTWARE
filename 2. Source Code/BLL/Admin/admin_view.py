# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_view.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_view(object):
    def setupUi(self, admin_view):
        admin_view.setObjectName("admin_view")
        admin_view.resize(650, 450)
        admin_view.setMinimumSize(QtCore.QSize(650, 450))
        admin_view.setMaximumSize(QtCore.QSize(650, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_view.setWindowIcon(icon)
        admin_view.setStyleSheet("QWidget#admin_view{\n"
"    border-image: url(:/images/gradient.png);\n"
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
        self.label = QtWidgets.QLabel(admin_view)
        self.label.setGeometry(QtCore.QRect(220, 30, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(admin_view)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 310, 351, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sys_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_confirm.setFont(font)
        self.sys_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_confirm.setObjectName("sys_confirm")
        self.horizontalLayout.addWidget(self.sys_confirm)
        self.sys_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_cancel.setFont(font)
        self.sys_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sys_cancel.setObjectName("sys_cancel")
        self.horizontalLayout.addWidget(self.sys_cancel)
        self.label_4 = QtWidgets.QLabel(admin_view)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 163, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sys_an = QtWidgets.QLineEdit(admin_view)
        self.sys_an.setGeometry(QtCore.QRect(240, 180, 361, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sys_an.setFont(font)
        self.sys_an.setText("")
        self.sys_an.setMaxLength(12)
        self.sys_an.setObjectName("sys_an")

        self.retranslateUi(admin_view)
        QtCore.QMetaObject.connectSlotsByName(admin_view)

    def retranslateUi(self, admin_view):
        _translate = QtCore.QCoreApplication.translate
        admin_view.setWindowTitle(_translate("admin_view", "View Account"))
        self.label.setText(_translate("admin_view", "<html><head/><body><p><span style=\" color:#ffffff;\">VIEW ACCOUNT</span></p></body></html>"))
        self.sys_confirm.setText(_translate("admin_view", "CONFIRM"))
        self.sys_cancel.setText(_translate("admin_view", "CANCEL"))
        self.label_4.setText(_translate("admin_view", "<html><head/><body><p><span style=\" color:#ffffff;\">ACCOUNT NUMBER:</span></p></body></html>"))
        self.sys_an.setInputMask(_translate("admin_view", "999999999999"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_view = QtWidgets.QWidget()
    ui = Ui_admin_view()
    ui.setupUi(admin_view)
    admin_view.show()
    sys.exit(app.exec_())

