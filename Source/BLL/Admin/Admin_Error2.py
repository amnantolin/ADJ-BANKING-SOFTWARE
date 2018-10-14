from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_error2


# Error for Wrong Account Number
class Error2(QtWidgets.QMainWindow, admin_error2.Ui_admin_error2):
    def __init__(self):
        super(Error2, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Error2()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()