from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import atm_transactions, atm_changepin_success, atm_changepin_error, atm_changepin_reenter, atm_changepin_blank

sys.path.insert(0, '../../DAL')
from data_handler import DataHandler

sys.path.insert(0, '../../UI')
import Atm_ChangePin

dh = DataHandler('../../../Database/Files.db')


# Change PIN Page
# Change current PIN from client account
# Conditions to Avoid Error Prompt: All Fields Must be Filled, new PIN = re-entered PIN, new PIN != old PIN
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
        self.dialog = atm_transactions.Transactions()
        self.dialog.show()
        self.close()

    def success(self):
        self.dialog1 = atm_changepin_success.ChangePin_Success()
        self.dialog1.show()
        self.close()

    def changepin_error(self):
        self.dialog2 = atm_changepin_error.ChangePin_Error()
        self.dialog2.show()
        self.close()

    def changepin_reenter(self):
        self.dialog3 = atm_changepin_reenter.ChangePin_Reenter()
        self.dialog3.show()
        self.close()

    def changepin_blank(self):
        self.dialog4 = atm_changepin_blank.ChangePin_Blank()
        self.dialog4.show()
        self.close()


def main():
    form = ChangePin()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()