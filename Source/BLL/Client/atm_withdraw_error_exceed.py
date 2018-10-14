from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_withdraw, atm_transactions

sys.path.insert(0, '../../UI')
import Atm_Withdraw_Error_Exceed


# Error for exceeded withdrawal limit in Withdraw Transaction
class Withdraw_Exceed(QtWidgets.QMainWindow, Atm_Withdraw_Error_Exceed.Ui_Atm_Withdraw_Error_Exceed):
    def __init__(self):
        super(Withdraw_Exceed, self).__init__()
        try:
            self.setupUi(self)
            self.yes.clicked.connect(self.again)
            self.no.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def again(self):
        self.dialog = atm_withdraw.Withdraw()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = atm_transactions.Transactions()
        self.dialog1.show()
        self.close()


def main():
    form = Withdraw_Exceed()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()