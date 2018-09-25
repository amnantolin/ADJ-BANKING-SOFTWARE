from PyQt5 import QtCore, QtGui, QtWidgets
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

parent = os.path.dirname(__file__)
accounts = os.path.join(parent, '../../DAL/accounts.txt')
admin = os.path.join(parent, '../../DAL/admin.txt')

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
        add = self.sys_add.text()
        cn = self.sys_cn.text()
        an = self.sys_an.text()
        pin = self.sys_pin.text()
        bal = self.sys_bal.text()

        fields = [cn, an, pin, bal, fn, mn, ln, age, contact, email, add]

        with open(accounts, mode='a', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerow(fields)
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
        with open(accounts, 'r') as accs:
            data = list(csv.reader(accs))

        with open(accounts, 'w', newline='') as accs:
            writer = csv.writer(accs)
            for row in data:
                if row[1] != self.sys_an.text():
                    writer.writerow(row)
        self.close()
        self.success()

    def error(self):
        self.dialog = Error2()
        self.dialog.show()

    def success(self):
        self.dialog.close()
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.dialog2 = Prompt2()
        self.dialog2.show()

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
        self.cnum = []
        self.fn = []
        self.mn =[]
        self.ln = []
        self.add =[]
        self.age = []
        self.contact =[]
        self.email = []
        self.bal = []

        with open(accounts, 'r') as afile:
            reader = csv.reader(afile, delimiter=',')
            for row in reader:
                self.cnum.append(row[0])
                self.anum.append(row[1])
                self.fn.append(row[4])
                self.mn.append(row[5])
                self.ln.append(row[6])
                self.add.append(row[10])
                self.age.append(row[7])
                self.contact.append(row[8])
                self.email.append(row[9])
                self.bal.append(row[3])
                self.anum_inp = self.sys_an.text()
                for i in range(len(self.anum)):
                    if self.anum_inp == self.anum[i]:
                        Viewout.anum = self.anum[i]
                        Viewout.cnum = self.cnum[i]
                        Viewout.fn = self.fn[i]
                        Viewout.mn = self.mn[i]
                        Viewout.ln = self.ln[i]
                        Viewout.add = self.add[i]
                        Viewout.age = self.age[i]
                        Viewout.contact = self.contact[i]
                        Viewout.email = self.email[i]
                        Viewout.bal = self.bal[i]
                        self.accview()
                        break
                    else:
                        self.error()

    def accview(self):
        self.dialog2.close()
        self.dialog3 = Viewout()
        self.dialog3.show()
        self.close()

    def error(self):
        self.dialog2 = Error2()
        self.dialog2.show()

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
        self.labeli.setText(_translate("admin_viewout", self.anum))
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







