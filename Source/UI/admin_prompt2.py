# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_prompt2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_prompt2(object):
    def setupUi(self, admin_prompt2):
        admin_prompt2.setObjectName("admin_prompt2")
        admin_prompt2.resize(358, 225)
        admin_prompt2.setMinimumSize(QtCore.QSize(358, 225))
        admin_prompt2.setMaximumSize(QtCore.QSize(358, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_prompt2.setWindowIcon(icon)
        admin_prompt2.setStyleSheet("QWidget#admin_prompt2{\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_prompt2)
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
        self.sys_ok = QtWidgets.QPushButton(admin_prompt2)
        self.sys_ok.setGeometry(QtCore.QRect(110, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sys_ok.setFont(font)
        self.sys_ok.setObjectName("sys_ok")
        self.sys_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(admin_prompt2)
        QtCore.QMetaObject.connectSlotsByName(admin_prompt2)

    def retranslateUi(self, admin_prompt2):
        _translate = QtCore.QCoreApplication.translate
        admin_prompt2.setWindowTitle(_translate("admin_prompt2", "Message"))
        self.label.setText(_translate("admin_prompt2", "<html><head/><body><p><span style=\" color:#ffffff;\">Account has been deleted!</span></p></body></html>"))
        self.sys_ok.setText(_translate("admin_prompt2", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_prompt2 = QtWidgets.QWidget()
    ui = Ui_admin_prompt2()
    ui.setupUi(admin_prompt2)
    admin_prompt2.show()
    sys.exit(app.exec_())

