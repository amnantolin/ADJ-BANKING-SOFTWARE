from PyQt5 import QtCore, QtGui, QtWidgets
import Atm_Login
import Atm_Transactions
import Atm_Login_Error
import Atm_Login_Error_Max
import Atm_Deposit
import Atm_Deposit_Receipt
import Atm_NewTransaction
import Atm_Withdraw
import Atm_Withdraw_Receipt
import Atm_Withdraw_Error_Insuff
import Atm_Withdraw_Error_Exceed
import Atm_Balance
import Atm_ChangePin
import Atm_ChangePin_Success
import Atm_ChangePin_Error
import Atm_ChangePin_Reenter
import sys
import csv
import os

parent = os.path.dirname(__file__)
accounts = os.path.join(parent, 'accounts.txt')


class Login(QtWidgets.QMainWindow, Atm_Login.Ui_Atm_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.log.clicked.connect(self.auth)

    def auth(self):
        self.card_client = []
        self.pin_client = []
        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.card_client.append(row[0])
                self.pin_client.append(row[2])
                self.card_input = self.card.text()
                self.pin_input = self.pin.text()
                for i in range(len(self.card_client)):
                    if self.card_input == self.card_client[i]:
                        if self.pin_input == self.pin_client[i]:
                            Deposit.card_client = self.card_client[i]
                            Deposit_Receipt.card_client = self.card_client[i]
                            Withdraw.card_client = self.card_client[i]
                            Withdraw_Receipt.card_client = self.card_client[i]
                            Balance.card_client = self.card_client[i]
                            ChangePin.card_client = self.card_client[i]
                            self.login()
                            break
                        else:
                            self.log_error()
                            break
                    else:
                        self.log_error()

    def login(self):
        self.dialog1.close()
        self.dialog = Transactions()
        self.dialog.show()
        self.close()

    def log_error(self):
        self.dialog1 = Log_Error()
        self.dialog1.show()
        self.close()


class Transactions(QtWidgets.QMainWindow, Atm_Transactions.Ui_Atm_Transactions):
    def __init__(self):
        super(Transactions, self).__init__()
        self.setupUi(self)
        self.deposit.clicked.connect(self.dep)
        self.withdraw.clicked.connect(self.wit)
        self.balance.clicked.connect(self.bal)
        self.changepin.clicked.connect(self.change)
        self.logout.clicked.connect(self.out)

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
        self.setupUi(self)
        self.confirm.clicked.connect(self.deposit)
        self.cancel.clicked.connect(self.back)

    def deposit(self):
        self.card_client1 = []
        self.balance_client = []

        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.balance_client.append(row[3])
                self.card_client1.append(row[0])
                for i in range(len(self.card_client1)):
                    if self.card_client == self.card_client1[i]:
                        amount = int(self.amount.text()) + int(self.balance_client[i])
                        Deposit_Receipt.amount = self.amount.text()

                        with open(accounts, 'r') as accs:
                            data = list(csv.reader(accs))

                        with open(accounts, 'w', newline='') as accs:
                            writer = csv.writer(accs)
                            for row1 in data:
                                if row1[0] != self.card_client:
                                    writer.writerow(row1)
                                else:
                                    row1[3] = amount
                                    writer.writerow(row1)
                        self.success()
                        break

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
        self.setupUi(self)
        self.okay.clicked.connect(self.ok)
        self.showreceipt()

    def showreceipt(self):
        self.card_client1 = []
        self.balance_client = []

        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.balance_client.append(row[3])
                self.card_client1.append(row[0])
                for i in range(len(self.card_client1)):
                    if self.card_client == self.card_client1[i]:
                        _translate = QtCore.QCoreApplication.translate
                        self.amnt.setText(_translate("Atm_Deposit_Receipt", self.amount))
                        self.bal.setText(_translate("Atm_Deposit_Receipt", self.balance_client[i]))
                        break

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class NewTransaction(QtWidgets.QMainWindow, Atm_NewTransaction.Ui_Atm_NewTransaction):
    def __init__(self):
        super(NewTransaction, self).__init__()
        self.setupUi(self)
        self.newtrans.clicked.connect(self.new)
        self.exit.clicked.connect(self.ex)

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
        self.setupUi(self)
        self.confirm.clicked.connect(self.withdraw)
        self.cancel.clicked.connect(self.back)

    def withdraw(self):
        self.card_client1 = []
        self.balance_client = []

        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.balance_client.append(row[3])
                self.card_client1.append(row[0])
                for i in range(len(self.card_client1)):
                    if self.card_client == self.card_client1[i]:
                        if int(self.amount.text()) <= 10000:
                            if int(self.amount.text()) <= int(self.balance_client[i]):
                                amount = int(self.balance_client[i]) - int(self.amount.text())
                                Withdraw_Receipt.amount = self.amount.text()

                                with open(accounts, 'r') as accs:
                                    data = list(csv.reader(accs))

                                with open(accounts, 'w', newline='') as accs:
                                    writer = csv.writer(accs)
                                    for row1 in data:
                                        if row1[0] != self.card_client:
                                            writer.writerow(row1)
                                        else:
                                            row1[3] = amount
                                            writer.writerow(row1)
                                self.success()
                                break

                            else:
                                self.withdraw_insuff()
                                break

                        else:
                            self.withdraw_exceed()
                            break

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
        self.setupUi(self)
        self.okay.clicked.connect(self.ok)
        self.showreceipt()

    def showreceipt(self):
        self.card_client1 = []
        self.balance_client = []

        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.balance_client.append(row[3])
                self.card_client1.append(row[0])
                for i in range(len(self.card_client1)):
                    if self.card_client == self.card_client1[i]:
                        _translate = QtCore.QCoreApplication.translate
                        self.amnt.setText(_translate("Atm_Deposit_Receipt", self.amount))
                        self.bal.setText(_translate("Atm_Deposit_Receipt", self.balance_client[i]))
                        break

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class Balance(QtWidgets.QMainWindow, Atm_Balance.Ui_Atm_Balance):
    def __init__(self):
        super(Balance, self).__init__()
        self.setupUi(self)
        self.okay.clicked.connect(self.ok)
        self.showbalance()

    def showbalance(self):
        self.balance_client = []
        self.card_client1 = []

        with open(accounts, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.balance_client.append(row[3])
                self.card_client1.append(row[0])
                for i in range(len(self.card_client1)):
                    if self.card_client == self.card_client1[i]:
                        self.balance = self.balance_client[i]
                        _translate = QtCore.QCoreApplication.translate
                        self.bal.setText(_translate("Atm_Balance", self.balance))
                        break


    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class ChangePin(QtWidgets.QMainWindow, Atm_ChangePin.Ui_Atm_ChangePin):
    def __init__(self):
        super(ChangePin, self).__init__()
        self.setupUi(self)
        self.confirm.clicked.connect(self.change)
        self.cancel.clicked.connect(self.back)

    def change(self):
        pin = self.pin.text()
        self.pin_client = []
        self.card_client1 = []
        repin = self.repin.text()
        if pin == repin:
            with open(accounts, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    self.pin_client.append(row[2])
                    self.card_client1.append(row[0])
                    for i in range(len(self.card_client1)):
                        if self.card_client == self.card_client1[i]:
                            if pin == self.pin_client[i]:
                                self.changepin_error()
                                break
                            else:
                                with open(accounts, 'r') as accs:
                                    data = list(csv.reader(accs))

                                with open(accounts, 'w', newline='') as accs:
                                    writer = csv.writer(accs)
                                    for row1 in data:
                                        if row1[0] != self.card_client:
                                            writer.writerow(row1)
                                        else:
                                            row1[2] = pin
                                            writer.writerow(row1)
                                self.success()
                                break
        else:
            self.changepin_reenter()

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


class Log_Error(QtWidgets.QMainWindow, Atm_Login_Error.Ui_Atm_Login_Error):
    def __init__(self):
        super(Log_Error, self).__init__()
        self.setupUi(self)
        self.yes.clicked.connect(self.again)
        self.no.clicked.connect(self.cancel)

    def again(self):
        self.dialog = Login()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.close()


class Withdraw_Insuff(QtWidgets.QMainWindow, Atm_Withdraw_Error_Insuff.Ui_Atm_Withdraw_Error_Insuff):
    def __init__(self):
        super(Withdraw_Insuff, self).__init__()
        self.setupUi(self)
        self.yes.clicked.connect(self.again)
        self.no.clicked.connect(self.cancel)

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
        self.setupUi(self)
        self.yes.clicked.connect(self.again)
        self.no.clicked.connect(self.cancel)

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
        self.setupUi(self)
        self.okay.clicked.connect(self.ok)

    def ok(self):
        self.dialog = NewTransaction()
        self.dialog.show()
        self.close()


class ChangePin_Error(QtWidgets.QMainWindow, Atm_ChangePin_Error.Ui_Atm_ChangePin_Error):
    def __init__(self):
        super(ChangePin_Error, self).__init__()
        self.setupUi(self)
        self.yes.clicked.connect(self.again)
        self.no.clicked.connect(self.cancel)

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
        self.setupUi(self)
        self.yes.clicked.connect(self.again)
        self.no.clicked.connect(self.cancel)

    def again(self):
        self.dialog = ChangePin()
        self.dialog.show()
        self.close()

    def cancel(self):
        self.dialog1 = Transactions()
        self.dialog1.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
