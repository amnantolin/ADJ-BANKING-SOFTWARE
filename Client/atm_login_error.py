from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import Atm_Login_Error


# Error for Wrong Account number and/or PIN
class Log_Error(QtWidgets.QMainWindow, Atm_Login_Error.Ui_Atm_Login_Error):
    def __init__(self):
        super(Log_Error, self).__init__()
        try:
            self.setupUi(self)
            self.ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Log_Error()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()
