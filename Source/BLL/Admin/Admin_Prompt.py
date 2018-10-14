from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, '../../UI')
import admin_prompt


# Prompt for Successfully Opening an Account
class Prompt(QtWidgets.QMainWindow, admin_prompt.Ui_admin_prompt):
    def __init__(self):
        super(Prompt, self).__init__()
        try:
            self.setupUi(self)
            self.sys_ok.clicked.connect(self.close)
        except Exception as e:
            print(e)


def main():
    form = Prompt()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()