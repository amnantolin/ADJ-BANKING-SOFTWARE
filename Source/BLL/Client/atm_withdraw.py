from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_withdraw_receipt, atm_transactions, atm_withdraw_error_insuff, atm_withdraw_error_exceed

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Withdraw

dh = DataHandler('../../../Database/Files.db')


# Withdraw Page
# Withdraw amount from client account
# Conditions to Avoid Error Prompt: Maximum withdrawal limit = 10000, and withdraw amount <= balance.
class Withdraw(QtWidgets.QMainWindow, Atm_Withdraw.Ui_Atm_Withdraw):
    def __init__(self):
        super(Withdraw, self).__init__()
        try:
            self.setupUi(self)
            self.confirm.clicked.connect(self.withdraw)
            self.cancel.clicked.connect(self.back)
            self.amount.returnPressed.connect(self.withdraw)
        except Exception as e:
            print(e)

    def withdraw(self):
        try:
            bal = int(dh.get_bal(self.anum)[0])
            wdraw = self.amount.text()

            if wdraw.isspace() or wdraw == '':
                wdraw = 0
            else:
                wdraw = int(self.amount.text())

            if wdraw > 10000:
                self.withdraw_exceed()
            elif wdraw > bal:
                self.withdraw_insuff()
            else:
                newbal = int(bal - wdraw)
                atm_withdraw_receipt.Withdraw_Receipt.wdraw = str(wdraw)
                dh.update_bal(newbal, self.anum)
                self.success()
        except Exception as e:
            print(e)

    def success(self):
        self.dialog = atm_withdraw_receipt.Withdraw_Receipt()
        self.dialog.show()
        self.close()

    def back(self):
        self.dialog1 = atm_transactions.Transactions()
        self.dialog1.show()
        self.close()

    def withdraw_insuff(self):
        self.dialog2 = atm_withdraw_error_insuff.Withdraw_Insuff()
        self.dialog2.show()
        self.close()

    def withdraw_exceed(self):
        self.dialog3 = atm_withdraw_error_exceed.Withdraw_Exceed()
        self.dialog3.show()
        self.close()


def main():
    form = Withdraw()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()