from PyQt5 import QtCore, QtGui, QtWidgets
import admin_close
import admin_error
import admin_error2
import admin_hp
import admin_log
import admin_view
import sys
import csv
import os

parent = os.path.dirname(__file__)
accounts = os.path.join(parent, 'accounts.txt')
admin = os.path.join(parent, 'admin.txt')

class Login(QtWidgets.QMainWindow, admin_log.Ui_admin_log):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.sys_log.clicked.connect(self.auth)

    def auth(self):
        self.user_admin = []
        self.pass_admin = []
        with open(admin, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.user_admin.append(row[0])
                self.pass_admin.append(row[1])
                self.userinp = self.sys_username.text()
                self.passinp = self.sys_pass.text()
                for i in range(len(self.user_admin)):
                    if self.userinp == self.user_admin[i]:
                        if self.passinp == self.pass_admin[i]:
                            self.log()
                            break
                        else:
                            self.error()
                            break
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
        self.anum = []
        with open(accounts, 'r') as afile:
            reader = csv.reader(afile, delimiter=',')
            for row in reader:
                self.anum.append(row[1])
                self.anum_inp = self.sys_an.text()
                for i in range(len(self.anum)):
                    if self.anum_inp == self.anum[i]:
                        self.accdelete()
                        break
                    else:
                        self.error()

    def accdelete(self):
        # insert codes for account deletion
        pass

    def error(self):
        self.dialog = Error2()
        self.dialog.show()

class View(QtWidgets.QMainWindow, admin_view.Ui_admin_view):
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.sys_cancel.clicked.connect(self.cancel)
        self.sys_confirm.clicked.connect(self.viewaccount)

    def cancel(self):
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.close()

    def viewaccount(self):
        self.anum = []

        with open(accounts, 'r') as afile:
            reader = csv.reader(afile, delimiter=',')
            for row in reader:
                self.anum.append(row[1])
                self.anum_inp = self.sys_an.text()
                for i in range(len(self.anum)):
                    if self.anum_inp == self.anum[i]:
                        self.accview()
                        break
                    else:
                        self.error()

    def accview(self):
        # insert codes for view account info
        pass

    def error(self):
        self.dialog2 = Error2()
        self.dialog2.show()

class Error(QtWidgets.QMainWindow, admin_error.Ui_admin_error):
    def __init__(self):
        super(Error, self).__init__()
        self.setupUi(self)

class Error2(QtWidgets.QMainWindow, admin_error2.Ui_admin_error2):
    def __init__(self):
        super(Error2, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()







