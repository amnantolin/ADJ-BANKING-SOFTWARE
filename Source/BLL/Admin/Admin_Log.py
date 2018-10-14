from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_HP, Admin_Error

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import admin_log, SPLASH_screen

dh = DataHandler('../../../Database/Files.db')

# Initialize Splash Screen UI
class Splash(SPLASH_screen.cssden):
    def __init__(self):
        super(Splash, self).__init__()
        self.close()
        self.dialog = Login_Admin()
        self.dialog.show()


# Admin Login Page
# Admin Account Authentication, Prompts Error Message if Wrong Username and/or Password Input
class Login_Admin(QtWidgets.QMainWindow, admin_log.Ui_admin_log):
    def __init__(self):
        super(Login_Admin, self).__init__()
        try:
            self.setupUi(self)
            self.sys_log.clicked.connect(self.authenticate)
            self.sys_username.returnPressed.connect(self.authenticate)
            self.sys_pass.returnPressed.connect(self.authenticate)
        except Exception as e:
            print(e)

    def authenticate(self):
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
        self.dialog = Admin_HP.Homepage()
        self.dialog.show()
        self.close()

    def error(self):
        self.dialog = Admin_Error.Error()
        self.dialog.show()


def main():
    form = Splash()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()