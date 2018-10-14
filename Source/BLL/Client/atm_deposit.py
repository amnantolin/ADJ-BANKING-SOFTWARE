from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_transactions, atm_deposit_receipt

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Deposit

dh = DataHandler('../../../Database/Files.db')


# Deposit Page
# Deposit amount to client account
class Deposit(QtWidgets.QMainWindow, Atm_Deposit.Ui_Atm_Deposit):
    def __init__(self):
        super(Deposit, self).__init__()
        try:
            self.setupUi(self)
            self.confirm.clicked.connect(self.deposit)
            self.cancel.clicked.connect(self.back)
            self.amount.returnPressed.connect(self.deposit)
        except Exception as e:
            print(e)

    def deposit(self):
        try:
            bal = int(dh.get_bal(self.anum)[0])
            dep = self.amount.text()

            if dep.isspace() or dep == '':
                dep = 0
            else:
                dep = int(self.amount.text())

            newbal = int(bal + dep)
            atm_deposit_receipt.Deposit_Receipt.dep = str(dep)
            dh.update_bal(newbal, self.anum)
            self.success()
        except Exception as e:
            print(e)

    def success(self):
        self.dialog = atm_deposit_receipt.Deposit_Receipt()
        self.dialog.show()
        self.close()

    def back(self):
        self.dialog1 = atm_transactions.Transactions()
        self.dialog1.show()
        self.close()


def main():
    form = Deposit()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()