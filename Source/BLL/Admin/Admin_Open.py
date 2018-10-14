from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_HP, Admin_Prompt, Admin_Error3, Admin_Error4, Admin_Error5

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import admin_open

dh = DataHandler('../../../Database/Files.db')

# Open Account Page
# Add Client Account
# Conditions to Avoid Error Prompt: All Fields Must be Filled, Unique Card/Account Number, and Initial Balance >= 1000.
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
        self.dialog = Admin_HP.Homepage()
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

            elif int(bal) < 1000:
                self.error3()

            else:
                dh.add_acc(cn, an, pin, fn, mn, ln, age, contact, email, address, bal)
                self.close()
                self.success()
        except Exception as e:
            print(e)


    def success(self):
        self.dialog = Admin_HP.Homepage()
        self.dialog.show()
        self.dialog1 = Admin_Prompt.Prompt()
        self.dialog1.show()

    def error(self):
        self.dialog2 = Admin_Error3.Error3()
        self.dialog2.show()

    def error2(self):
        self.dialog3 = Admin_Error4.Error4()
        self.dialog3.show()

    def error3(self):
        self.dialog4 = Admin_Error5.Error5()
        self.dialog4.show()


def main():
    form = OpenA()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()