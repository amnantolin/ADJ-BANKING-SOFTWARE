from PyQt5 import QtCore, QtGui, QtWidgets
from data_handler import DataHandler
import admin_close
import admin_open
import admin_error
import admin_error2
import admin_hp
import admin_log
import admin_prompt
import admin_prompt2
import admin_view
import admin_viewout
import sys
import csv
import os

dh = DataHandler('../../DAL/Files.db')

class Login(QtWidgets.QMainWindow, admin_log.Ui_admin_log):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.sys_log.clicked.connect(self.auth)

    def auth(self):
        user = self.sys_username.text()
        password = self.sys_pass.text()
        if dh.admin_log(user, password):
            self.log()
        else:
            self.error()

    def log(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

    def error(self):
        self.dialog = Error()
        self.dialog.show()

class Homepage(QtWidgets.QMainWindow, admin_hp.Ui_admin_hp):
    def __init__(self):
        super(Homepage, self).__init__()
        self.setupUi(self)
        self.sys_logout.clicked.connect(self.out)
        self.sys_open.clicked.connect(self.op)
        self.sys_close.clicked.connect(self.cl)
        self.sys_info.clicked.connect(self.vi)

    def out(self):
        self.dialog = Login()
        self.dialog.show()
        self.close()

    def op(self):
        self.dialog = OpenA()
        self.dialog.show()
        self.close()

    def cl(self):
        self.dialog = CloseA()
        self.dialog.show()
        self.close()

    def vi(self):
        self.dialog = View()
        self.dialog.show()
        self.close()

class OpenA(QtWidgets.QMainWindow, admin_open.Ui_admin_open):
    def __init__(self):
        super(OpenA, self).__init__()
        self.setupUi(self)
        self.sys_cancel.clicked.connect(self.cancel)
        self.sys_create.clicked.connect(self.createaccount)

    def cancel(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

    def createaccount(self):
        fn = self.sys_fn.text()
        mn = self.sys_mn.text()
        ln = self.sys_ln.text()
        age = self.sys_age.text()
        contact = self.sys_contact.text()
        email = self.sys_email.text()
        address = self.sys_add.text()
        cn = self.sys_cn.text()
        an = self.sys_an.text()
        pin = self.sys_pin.text()
        bal = self.sys_bal.text()

        dh.add_acc(cn, an, pin, fn, mn, ln, age, contact, email, address, bal)

        self.close()
        self.success()

    def success(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.dialog1 = Prompt()
        self.dialog1.show()

class CloseA(QtWidgets.QMainWindow, admin_close.Ui_admin_close):
    def __init__(self):
        super(CloseA, self).__init__()
        self.setupUi(self)
        self.sys_cancel.clicked.connect(self.cancel)
        self.sys_delete.clicked.connect(self.deleteaccount)

    def cancel(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

    def deleteaccount(self):
        anum = self.sys_an.text()
        if dh.find_acc(anum):
            dh.delete_acc(anum)
            self.close()
            self.success()
        else:
            self.error()

    def error(self):
        self.dialog = Error2()
        self.dialog.show()

    def success(self):
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.dialog2 = Prompt2()
        self.dialog2.show()

class View(QtWidgets.QMainWindow, admin_view.Ui_admin_view):
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.sys_cancel.clicked.connect(self.cancel)
        self.sys_confirm.clicked.connect(self.view_find)

    def cancel(self):
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.close()

    def view_find(self):
        anum = self.sys_an.text()
        if dh.find_acc(anum):
            Viewout.acc = str(dh.view_info(anum)[0])
            Viewout.fn = dh.view_info(anum)[1]
            Viewout.mn = dh.view_info(anum)[2]
            Viewout.ln = dh.view_info(anum)[3]
            Viewout.age = dh.view_info(anum)[4]
            Viewout.contact = dh.view_info(anum)[5]
            Viewout.email = dh.view_info(anum)[6]
            Viewout.add = dh.view_info(anum)[7]
            Viewout.bal = str(dh.view_info(anum)[8])
            Viewout.cnum = str(dh.view_info1(anum)[0])
            self.accview()
        else:
            self.error()

    def error(self):
        self.dialog2 = Error2()
        self.dialog2.show()

    def accview(self):
        self.dialog3 = Viewout()
        self.dialog3.show()
        self.close()


class Viewout(QtWidgets.QMainWindow, admin_viewout.Ui_admin_viewout):
    def __init__(self):
        super(Viewout, self).__init__()
        self.setupUi(self)
        self.sys_back.clicked.connect(self.homepage)
        self.showdetails()

    def showdetails(self):
        _translate = QtCore.QCoreApplication.translate
        self.labela.setText(_translate("admin_viewout", self.fn))
        self.labelb.setText(_translate("admin_viewout", self.mn))
        self.labelc.setText(_translate("admin_viewout", self.ln))
        self.labeld.setText(_translate("admin_viewout", self.add))
        self.labele.setText(_translate("admin_viewout", self.age))
        self.labelf.setText(_translate("admin_viewout", self.contact))
        self.labelg.setText(_translate("admin_viewout", self.email))
        self.labelh.setText(_translate("admin_viewout", self.cnum))
        self.labeli.setText(_translate("admin_viewout", self.acc))
        self.labelj.setText(_translate("admin_viewout", self.bal))

    def homepage(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

class Error(QtWidgets.QMainWindow, admin_error.Ui_admin_error):
    def __init__(self):
        super(Error, self).__init__()
        self.setupUi(self)

class Error2(QtWidgets.QMainWindow, admin_error2.Ui_admin_error2):
    def __init__(self):
        super(Error2, self).__init__()
        self.setupUi(self)

class Prompt(QtWidgets.QMainWindow, admin_prompt.Ui_admin_prompt):
    def __init__(self):
        super(Prompt, self).__init__()
        self.setupUi(self)

class Prompt2(QtWidgets.QMainWindow, admin_prompt2.Ui_admin_prompt2):
    def __init__(self):
        super(Prompt2, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()







