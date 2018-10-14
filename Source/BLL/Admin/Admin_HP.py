from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_Log, Admin_Open, Admin_Close, Admin_View

sys.path.insert(0, '../../UI')
import admin_hp


# Admin Homepage/Main Menu
# Choose to open either Open Account Page, Close Account Page, or View Info Page
class Homepage(QtWidgets.QMainWindow, admin_hp.Ui_admin_hp):
    def __init__(self):
        super(Homepage, self).__init__()
        try:
            self.setupUi(self)
            self.sys_logout.clicked.connect(self.Logout)
            self.sys_open.clicked.connect(self.OpenAcc)
            self.sys_close.clicked.connect(self.CloseAcc)
            self.sys_info.clicked.connect(self.ViewAcc)
        except Exception as e:
            print(e)

    def Logout(self):
        self.dialog = Admin_Log.Login_Admin()
        self.dialog.show()
        self.close()

    def OpenAcc(self):
        self.dialog = Admin_Open.OpenA()
        self.dialog.show()
        self.close()

    def CloseAcc(self):
        self.dialog = Admin_Close.CloseA()
        self.dialog.show()
        self.close()

    def ViewAcc(self):
        self.dialog = Admin_View.View()
        self.dialog.show()
        self.close()


def main():
    form = Homepage()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()