from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_newtransaction

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Deposit_Receipt

dh = DataHandler('../../../Database/Files.db')


# Deposit Receipt window
# Display amount deposited and updated balance
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
        self.dialog = atm_newtransaction.NewTransaction()
        self.dialog.show()
        self.close()


def main():
    form = Deposit_Receipt()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()