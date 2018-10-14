from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_newtransaction

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Withdraw_Receipt

dh = DataHandler('../../../Database/Files.db')


# Withdraw Receipt window
# Display amount withdrawn and updated balance
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
        self.dialog = atm_newtransaction.NewTransaction()
        self.dialog.show()
        self.close()


def main():
    form = Withdraw_Receipt()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()