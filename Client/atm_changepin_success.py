from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_newtransaction

sys.path.insert(0, '../../UI')
import Atm_ChangePin_Success


# Prompt for Successfully changing PIN
class ChangePin_Success(QtWidgets.QMainWindow, Atm_ChangePin_Success.Ui_Atm_ChangePin_Success):
    def __init__(self):
        super(ChangePin_Success, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
        except Exception as e:
            print(e)

    def ok(self):
        self.dialog = atm_newtransaction.NewTransaction()
        self.dialog.show()
        self.close()


def main():
    form = ChangePin_Success()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()