from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_transactions, atm_login

sys.path.insert(0, '../../UI')
import Atm_NewTransaction


# New Transaction prompt
# Ask client to make new transaction
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
        self.dialog = atm_transactions.Transactions()
        self.dialog.show()
        self.close()

    def ex(self):
        self.dialog1 = atm_login.Login_Atm()
        self.dialog1.show()
        self.close()


def main():
    form = NewTransaction()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()