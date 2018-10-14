from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_transactions, atm_login_error, atm_login_error_max, atm_deposit, atm_deposit_receipt
import atm_withdraw, atm_withdraw_receipt, atm_balance, atm_changepin

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Login, SPLASH_screen

dh = DataHandler('../../../Database/Files.db')


# Initialize Splash Screen UI
class Splash(SPLASH_screen.cssden):
    def __init__(self):
        super(Splash, self).__init__()
        Login_Atm.log_count = 1
        self.close()
        self.dialog = Login_Atm()
        self.dialog.show()


# ATM Login Page
# Client Account Authentication, Prompts Error Message if Wrong Account number and/or PIN Input,
# and exceeded maximum login attempts of 3
class Login_Atm(QtWidgets.QMainWindow, Atm_Login.Ui_Atm_Login):
    def __init__(self):
        super(Login_Atm, self).__init__()
        try:
            self.setupUi(self)
            self.log.clicked.connect(self.authenticate)
            self.card.returnPressed.connect(self.authenticate)
            self.pin.returnPressed.connect(self.authenticate)
        except Exception as e:
            print(e)

    def authenticate(self):
        cnum = self.card.text()
        pnum = self.pin.text()

        try:
            if dh.client_log(cnum, pnum):
                self.log_count = 0
                atm_withdraw.Withdraw.anum = dh.view_anum(cnum)[0]
                atm_withdraw_receipt.Withdraw_Receipt.anum = dh.view_anum(cnum)[0]
                atm_deposit.Deposit.anum = dh.view_anum(cnum)[0]
                atm_deposit_receipt.Deposit_Receipt.anum = dh.view_anum(cnum)[0]
                atm_balance.Balance.anum = dh.view_anum(cnum)[0]
                atm_changepin.ChangePin.anum = dh.view_anum(cnum)[0]
                self.login()
            elif self.log_count == 3:
                self.log_error_max()
            else:
                self.log_count = int(self.log_count) + 1
                self.log_error()
        except Exception as e:
            print(e)

    def login(self):
        self.dialog = atm_transactions.Transactions()
        self.dialog.show()
        self.close()

    def log_error(self):
        self.dialog1 = atm_login_error.Log_Error()
        self.dialog1.show()

    def log_error_max(self):
        self.dialog2 = atm_login_error_max.Log_Error_Max()
        self.dialog2.show()
        self.close()


def main():
    form = Splash()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()