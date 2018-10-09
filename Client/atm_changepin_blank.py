from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_changepin, atm_transactions

sys.path.insert(0, '../../UI')
import Atm_ChangePin_Blank


# Error for Missing Field/s Detection in Change PIN
class ChangePin_Blank(QtWidgets.QMainWindow, Atm_ChangePin_Blank.Ui_Atm_ChangePin_Blank):
    def __init__(self):
        super(ChangePin_Blank, self).__init__()
        try:
            self.setupUi(self)
            self.yes.clicked.connect(self.again)
            self.no.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def again(self):
        self.dialog = atm_changepin.ChangePin()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = atm_transactions.Transactions()
        self.dialog1.show()
        self.close()


def main():
    form = ChangePin_Blank()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()