from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_error5


#Error for Insufficient Initial Balance
class Error5(QtWidgets.QMainWindow, admin_error5.Ui_admin_error5):
    def __init__(self):
        super(Error5, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Error5()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()