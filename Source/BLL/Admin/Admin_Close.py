from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_HP, Admin_Error2, Admin_Prompt2

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import admin_close

dh = DataHandler('../../../Database/Files.db')


# Close Account Page
# Deletes Specific Client Account, Must Enter a Valid Account Number
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
        self.dialog = Admin_HP.Homepage()
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
        self.dialog = Admin_Error2.Error2()
        self.dialog.show()

    def success(self):
        self.dialog1 = Admin_HP.Homepage()
        self.dialog1.show()
        self.dialog2 = Admin_Prompt2.Prompt2()
        self.dialog2.show()


def main():
    form = CloseA()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()