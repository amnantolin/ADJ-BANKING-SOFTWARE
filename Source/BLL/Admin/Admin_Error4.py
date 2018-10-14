from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_error4


# Error for Card/Account Number Repetition
class Error4(QtWidgets.QMainWindow, admin_error4.Ui_admin_error4):
    def __init__(self):
        super(Error4, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Error4()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()