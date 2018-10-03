from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../UI')
import admin_log, admin_close, admin_open, admin_hp, admin_view, admin_viewout, SPLASH_screen
import admin_error, admin_error2, admin_error3, admin_error4
import admin_prompt, admin_prompt2

dh = DataHandler('../../Database/Files.db')

class Splash(SPLASH_screen.cssden):
    def __init__(self):
        super(Splash, self).__init__()
        self.close()
        self.dialog = Login()
        self.dialog.show()


class Login(QtWidgets.QMainWindow, admin_log.Ui_admin_log):
    def __init__(self):
        super(Login, self).__init__()
        try:
            self.setupUi(self)
            self.sys_log.clicked.connect(self.auth)
            self.sys_username.returnPressed.connect(self.auth)
            self.sys_pass.returnPressed.connect(self.auth)
        except Exception as e:
            print(e)

    def auth(self):
        user = self.sys_username.text()
        password = self.sys_pass.text()
        try:
            if dh.admin_log(user, password):
                self.log()
            else:
                self.error()
        except Exception as e:
            print(e)

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
        try:
            self.setupUi(self)
            self.sys_logout.clicked.connect(self.out)
            self.sys_open.clicked.connect(self.op)
            self.sys_close.clicked.connect(self.cl)
            self.sys_info.clicked.connect(self.vi)
        except Exception as e:
            print(e)

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
        try:
            self.setupUi(self)
            self.sys_cancel.clicked.connect(self.cancel)
            self.sys_create.clicked.connect(self.createaccount)
        except Exception as e:
            print(e)

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

        try:
            if fn.isspace() or fn == '' or mn.isspace() or mn == '' or ln.isspace() or ln == '' or age.isspace() \
                    or age == '' or contact.isspace() or contact == '' or email.isspace() or email == '' \
                    or address.isspace() or address == '' or cn.isspace() or cn == '' or an.isspace() or an == '' \
                    or pin.isspace() or pin == '' or bal.isspace() or bal == '':

                self.error()

            elif dh.check_reps(an, cn):
                self.error2()

            else:
                dh.add_acc(cn, an, pin, fn, mn, ln, age, contact, email, address, bal)
                self.close()
                self.success()
        except Exception as e:
            print(e)


    def success(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.dialog1 = Prompt()
        self.dialog1.show()

    def error(self):
        self.dialog2 = Error3()
        self.dialog2.show()

    def error2(self):
        self.dialog3 = Error4()
        self.dialog3.show()

class CloseA(QtWidgets.QMainWindow, admin_close.Ui_admin_close):
    def __init__(self):
        super(CloseA, self).__init__()
        try:
            self.setupUi(self)
            self.sys_cancel.clicked.connect(self.cancel)
            self.sys_delete.clicked.connect(self.deleteaccount)
            self.sys_an.returnPressed.connect(self.deleteaccount)
        except Exception as e:
            print(e)

    def cancel(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

    def deleteaccount(self):
        anum = self.sys_an.text()
        try:
            if dh.find_acc(anum):
                dh.delete_acc(anum)
                self.close()
                self.success()
            else:
                self.error()
        except Exception as e:
            print(e)

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
        try:
            self.setupUi(self)
            self.sys_cancel.clicked.connect(self.cancel)
            self.sys_confirm.clicked.connect(self.view_find)
            self.sys_an.returnPressed.connect(self.view_find)
        except Exception as e:
            print(e)

    def cancel(self):
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.close()

    def view_find(self):
        anum = self.sys_an.text()
        try:
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
        except Exception as e:
            print(e)

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
        try:
            self.setupUi(self)
            self.sys_back.clicked.connect(self.homepage)
            self.showdetails()
        except Exception as e:
            print(e)

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
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

class Error2(QtWidgets.QMainWindow, admin_error2.Ui_admin_error2):
    def __init__(self):
        super(Error2, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

class Error3(QtWidgets.QMainWindow, admin_error3.Ui_admin_error3):
    def __init__(self):
        super(Error3, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

class Error4(QtWidgets.QMainWindow, admin_error4.Ui_admin_error4):
    def __init__(self):
        super(Error4, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

class Prompt(QtWidgets.QMainWindow, admin_prompt.Ui_admin_prompt):
    def __init__(self):
        super(Prompt, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

class Prompt2(QtWidgets.QMainWindow, admin_prompt2.Ui_admin_prompt2):
    def __init__(self):
        super(Prompt2, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)

def main():
    form = Splash()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()