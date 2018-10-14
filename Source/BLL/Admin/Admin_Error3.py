from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_error3


# Error for Missing Field/s Detection in Open Account
class Error3(QtWidgets.QMainWindow, admin_error3.Ui_admin_error3):
    def __init__(self):
        super(Error3, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Error3()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()