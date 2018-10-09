from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_transactions, atm_withdraw

sys.path.insert(0, '../../UI')
import Atm_Withdraw_Error_Insuff


# Error for insufficient balance in Withdraw Transaction
class Withdraw_Insuff(QtWidgets.QMainWindow, Atm_Withdraw_Error_Insuff.Ui_Atm_Withdraw_Error_Insuff):
    def __init__(self):
        super(Withdraw_Insuff, self).__init__()
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
    form = Withdraw_Insuff()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()