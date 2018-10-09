from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import Atm_Login_Error_Max


# Error for exceeded maximum login attempts
class Log_Error_Max(QtWidgets.QMainWindow, Atm_Login_Error_Max.Ui_Atm_Login_Error_Max):
    def __init__(self):
        super(Log_Error_Max, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
        except Exception as e:
            print(e)

    def ok(self):
        self.close()


def main():
    form = Log_Error_Max()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()