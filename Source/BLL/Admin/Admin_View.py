from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_HP, Admin_Viewout, Admin_Error2

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import admin_view

dh = DataHandler('../../../Database/Files.db')


# View Client Info Page
# Checks for Valid Client Account Number to Proceed
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
        self.dialog1 = Admin_HP.Homepage()
        self.dialog1.show()
        self.close()

    def view_find(self):
        anum = self.sys_an.text()
        try:
            if dh.find_acc(anum):
                Admin_Viewout.Viewout.acc = str(dh.view_info(anum)[0])
                Admin_Viewout.Viewout.fn = dh.view_info(anum)[1]
                Admin_Viewout.Viewout.mn = dh.view_info(anum)[2]
                Admin_Viewout.Viewout.ln = dh.view_info(anum)[3]
                Admin_Viewout.Viewout.age = dh.view_info(anum)[4]
                Admin_Viewout.Viewout.contact = dh.view_info(anum)[5]
                Admin_Viewout.Viewout.email = dh.view_info(anum)[6]
                Admin_Viewout.Viewout.add = dh.view_info(anum)[7]
                Admin_Viewout.Viewout.bal = str(dh.view_info(anum)[8])
                Admin_Viewout.Viewout.cnum = str(dh.view_info1(anum)[0])
                self.accview()
            else:
                self.error()
        except Exception as e:
            print(e)

    def error(self):
        self.dialog2 = Admin_Error2.Error2()
        self.dialog2.show()

    def accview(self):
        self.dialog3 = Admin_Viewout.Viewout()
        self.dialog3.show()
        self.close()


def main():
    form = View()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()