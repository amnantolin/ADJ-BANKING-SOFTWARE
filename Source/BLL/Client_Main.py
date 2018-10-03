from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../UI')
import Atm_Login, Atm_Transactions, Atm_Deposit, Atm_Deposit_Receipt, Atm_Withdraw, Atm_Withdraw_Receipt, Atm_Balance, Atm_ChangePin
import Atm_Login_Error, Atm_Login_Error_Max, Atm_NewTransaction, Atm_Withdraw_Error_Insuff, Atm_Withdraw_Error_Exceed, Atm_ChangePin_Success, SPLASH_screen
import Atm_ChangePin_Error, Atm_ChangePin_Reenter, Atm_ChangePin_Blank

dh = DataHandler('../../Database/Files.db')

class Splash(SPLASH_screen.cssden):
    def __init__(self):
        super(Splash, self).__init__()
        Login.log_count = 1
        self.close()
        self.dialog = Login()
        self.dialog.show()

class Login(QtWidgets.QMainWindow, Atm_Login.Ui_Atm_Login):
    def __init__(self):
        super(Login, self).__init__()
        try:
            self.setupUi(self)
            self.log.clicked.connect(self.auth)
            self.card.returnPressed.connect(self.auth)
            self.pin.returnPressed.connect(self.auth)
        except Exception as e:
            print(e)

    def auth(self):
        cnum = self.card.text()
        pnum = self.pin.text()

        try:
            if dh.client_log(cnum, pnum):
                self.log_count = 0
                Withdraw.anum = dh.view_anum(cnum)[0]
                Withdraw_Receipt.anum = dh.view_anum(cnum)[0]
                Deposit.anum = dh.view_anum(cnum)[0]
                Deposit_Receipt.anum = dh.view_anum(cnum)[0]
                Balance.anum = dh.view_anum(cnum)[0]
                ChangePin.anum = dh.view_anum(cnum)[0]
                self.login()
            elif self.log_count == 3:
                self.log_error_max()
            else:
                self.log_count = int(self.log_count) + 1
                self.log_error()
        except Exception as e:
            print(e)

    def login(self):
        self.dialog = Transactions()
        self.dialog.show()
        self.close()

    def log_error(self):
        self.dialog1 = Log_Error()
        self.dialog1.show()

    def log_error_max(self):
        self.dialog2 = Log_Error_Max()
        self.dialog2.show()
        self.close()


class Transactions(QtWidgets.QMainWindow, Atm_Transactions.Ui_Atm_Transactions):
    def __init__(self):
        super(Transactions, self).__init__()
        try:
            self.setupUi(self)
            self.deposit.clicked.connect(self.dep)
            self.withdraw.clicked.connect(self.wit)
            self.balance.clicked.connect(self.bal)
            self.changepin.clicked.connect(self.change)
            self.logout.clicked.connect(self.out)
        except Exception as e:
            print(e)

    def dep(self):
        self.dialog = Deposit()
        self.dialog.show()
        self.close()

    def wit(self):
        self.dialog1 = Withdraw()
        self.dialog1.show()
        self.close()

    def bal(self):
        self.dialog2 = Balance()
        self.dialog2.show()
        self.close()

    def change(self):
        self.dialog3 = ChangePin()
        self.dialog3.show()
        self.close()

    def out(self):
        self.dialog4 = Login()
        self.dialog4.show()
        self.close()


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
            Deposit_Receipt.dep = str(dep)
            Deposit_Receipt.bal = str(newbal)
            dh.update_bal(newbal, self.anum)
            self.success()
        except Exception as e:
            print(e)

    def success(self):
        self.dialog = Deposit_Receipt()
        self.dialog.show()
        self.close()

    def back(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


class Deposit_Receipt(QtWidgets.QMainWindow, Atm_Deposit_Receipt.Ui_Atm_Deposit_Receipt):
    def __init__(self):
        super(Deposit_Receipt, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
            self.showreceipt()
        except Exception as e:
            print(e)

    def showreceipt(self):
        try:
            bal = str(dh.get_bal(self.anum)[0])
        except Exception as e:
            print(e)
        _translate = QtCore.QCoreApplication.translate
        self.amnt.setText(_translate("Atm_Deposit_Receipt", self.dep))
        self.bal.setText(_translate("Atm_Deposit_Receipt", bal))

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class NewTransaction(QtWidgets.QMainWindow, Atm_NewTransaction.Ui_Atm_NewTransaction):
    def __init__(self):
        super(NewTransaction, self).__init__()
        try:
            self.setupUi(self)
            self.newtrans.clicked.connect(self.new)
            self.exit.clicked.connect(self.ex)
        except Exception as e:
            print(e)

    def new(self):
        self.dialog = Transactions()
        self.dialog.show()
        self.close()

    def ex(self):
        self.dialog1 = Login()
        self.dialog1.show()
        self.close()


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
                Withdraw_Receipt.wdraw = str(wdraw)
                Withdraw_Receipt.bal = str(newbal)
                dh.update_bal(newbal, self.anum)
                self.success()
        except Exception as e:
            print(e)

    def success(self):
        self.dialog = Withdraw_Receipt()
        self.dialog.show()
        self.close()

    def back(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()

    def withdraw_insuff(self):
        self.dialog2 = Withdraw_Insuff()
        self.dialog2.show()
        self.close()

    def withdraw_exceed(self):
        self.dialog3 = Withdraw_Exceed()
        self.dialog3.show()
        self.close()


class Withdraw_Receipt(QtWidgets.QMainWindow, Atm_Withdraw_Receipt.Ui_Atm_Withdraw_Receipt):
    def __init__(self):
        super(Withdraw_Receipt, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
            self.showreceipt()
        except Exception as e:
            print(e)

    def showreceipt(self):
        try:
            bal = str(dh.get_bal(self.anum)[0])
        except Exception as e:
            print(e)
        _translate = QtCore.QCoreApplication.translate
        self.amnt.setText(_translate("Atm_Withdraw_Receipt", self.wdraw))
        self.bal.setText(_translate("Atm_Withdraw_Receipt", bal))

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class Balance(QtWidgets.QMainWindow, Atm_Balance.Ui_Atm_Balance):
    def __init__(self):
        super(Balance, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
            self.showbalance()
        except Exception as e:
            print(e)

    def showbalance(self):
        try:
            bal = str(dh.get_bal(self.anum)[0])
        except Exception as e:
            print(e)
        _translate = QtCore.QCoreApplication.translate
        self.bal.setText(_translate("Atm_Withdraw_Receipt", bal))

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class ChangePin(QtWidgets.QMainWindow, Atm_ChangePin.Ui_Atm_ChangePin):
    def __init__(self):
        super(ChangePin, self).__init__()
        try:
            self.setupUi(self)
            self.confirm.clicked.connect(self.change)
            self.cancel.clicked.connect(self.back)
            self.pin.returnPressed.connect(self.change)
            self.repin.returnPressed.connect(self.change)
        except Exception as e:
            print(e)

    def change(self):
        try:
            oldpin = str(dh.get_pin(self.anum)[0])
        except Exception as e:
            print(e)
        pin = self.pin.text()
        repin = self.repin.text()

        try:
            if pin.isspace() or pin == '' or repin.isspace() or repin == '':
                self.changepin_blank()
            elif pin != repin:
                self.changepin_reenter()
            elif pin == oldpin:
                self.changepin_error()
            else:
                newpin = int(pin)
                dh.update_pin(newpin, self.anum)
                self.success()
        except Exception as e:
            print(e)

    def back(self):
        self.dialog = Transactions()
        self.dialog.show()
        self.close()

    def success(self):
        self.dialog1 = ChangePin_Success()
        self.dialog1.show()
        self.close()

    def changepin_error(self):
        self.dialog2 = ChangePin_Error()
        self.dialog2.show()
        self.close()

    def changepin_reenter(self):
        self.dialog3 = ChangePin_Reenter()
        self.dialog3.show()
        self.close()

    def changepin_blank(self):
        self.dialog4 = ChangePin_Blank()
        self.dialog4.show()
        self.close()


class Log_Error(QtWidgets.QMainWindow, Atm_Login_Error.Ui_Atm_Login_Error):
    def __init__(self):
        super(Log_Error, self).__init__()
        try:
            self.setupUi(self)
            self.ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


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
        self.dialog = Withdraw()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


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
        self.dialog = Withdraw()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


class ChangePin_Success(QtWidgets.QMainWindow, Atm_ChangePin_Success.Ui_Atm_ChangePin_Success):
    def __init__(self):
        super(ChangePin_Success, self).__init__()
        try:
            self.setupUi(self)
            self.okay.clicked.connect(self.ok)
        except Exception as e:
            print(e)

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class ChangePin_Error(QtWidgets.QMainWindow, Atm_ChangePin_Error.Ui_Atm_ChangePin_Error):
    def __init__(self):
        super(ChangePin_Error, self).__init__()
        try:
            self.setupUi(self)
            self.yes.clicked.connect(self.again)
            self.no.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def again(self):
        self.dialog = ChangePin()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


class ChangePin_Reenter(QtWidgets.QMainWindow, Atm_ChangePin_Reenter.Ui_Atm_ChangePin_Reenter):
    def __init__(self):
        super(ChangePin_Reenter, self).__init__()
        try:
            self.setupUi(self)
            self.yes.clicked.connect(self.again)
            self.no.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def again(self):
        self.dialog = ChangePin()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


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
        self.dialog = ChangePin()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()

def main():
    form = Splash()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()