from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_login, atm_deposit, atm_balance, atm_withdraw, atm_changepin

sys.path.insert(0, '../../UI')
import Atm_Transactions


# ATM Transaction Page/Main Menu
# Choose to open either Deposit Page, Withdraw Page, Balance Page, or Change PIN Page
class Transactions(QtWidgets.QMainWindow, Atm_Transactions.Ui_Atm_Transactions):
    def __init__(self):
        super(Transactions, self).__init__()
        try:
            self.setupUi(self)
            self.deposit.clicked.connect(self.Deposit)
            self.withdraw.clicked.connect(self.Withdraw)
            self.balance.clicked.connect(self.Balance)
            self.changepin.clicked.connect(self.ChangePin)
            self.logout.clicked.connect(self.Logout)
        except Exception as e:
            print(e)

    def Deposit(self):
        self.dialog = atm_deposit.Deposit()
        self.dialog.show()
        self.close()

    def Withdraw(self):
        self.dialog1 = atm_withdraw.Withdraw()
        self.dialog1.show()
        self.close()

    def Balance(self):
        self.dialog2 = atm_balance.Balance()
        self.dialog2.show()
        self.close()

    def ChangePin(self):
        self.dialog3 = atm_changepin.ChangePin()
        self.dialog3.show()
        self.close()

    def Logout(self):
        self.dialog4 = atm_login.Login_Atm()
        self.dialog4.show()
        self.close()


def main():
    form = Transactions()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()