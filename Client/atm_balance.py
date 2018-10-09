from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_newtransaction

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_Balance

dh = DataHandler('../../../Database/Files.db')


# Balance Page
# Display current balance
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
        self.bal.setText(_translate("Atm_Balance", bal))

    def ok(self):
        self.dialog = atm_newtransaction.NewTransaction()
        self.dialog.show()
        self.close()


def main():
    form = Balance()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()