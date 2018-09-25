# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_prompt.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_prompt(object):
    def setupUi(self, admin_prompt):
        admin_prompt.setObjectName("admin_prompt")
        admin_prompt.resize(358, 225)
        admin_prompt.setMinimumSize(QtCore.QSize(358, 225))
        admin_prompt.setMaximumSize(QtCore.QSize(358, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/images/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_prompt.setWindowIcon(icon)
        admin_prompt.setStyleSheet("QWidget#admin_prompt{\n"
"border-image: url(':/images/gradient.png');\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_prompt)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 300, 131))
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

        self.retranslateUi(admin_prompt)
        QtCore.QMetaObject.connectSlotsByName(admin_prompt)

    def retranslateUi(self, admin_prompt):
        _translate = QtCore.QCoreApplication.translate
        admin_prompt.setWindowTitle(_translate("admin_prompt", "Message"))
        self.label.setText(_translate("admin_prompt", "<html><head/><body><p><span style=\" color:#ffffff;\">Account has been created!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_prompt = QtWidgets.QWidget()
    ui = Ui_admin_prompt()
    ui.setupUi(admin_prompt)
    admin_prompt.show()
    sys.exit(app.exec_())

