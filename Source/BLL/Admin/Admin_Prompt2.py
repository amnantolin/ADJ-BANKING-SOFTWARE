from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_prompt2


# Prompt for Successfully Deleting an Account
class Prompt2(QtWidgets.QMainWindow, admin_prompt2.Ui_admin_prompt2):
    def __init__(self):
        super(Prompt2, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Prompt2()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()