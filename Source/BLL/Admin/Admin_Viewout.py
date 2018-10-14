from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Admin_HP

sys.path.insert(0, '../../UI')
import admin_viewout


# Output Page For Client Information
# Shows Details About the Specific Client
class Viewout(QtWidgets.QMainWindow, admin_viewout.Ui_admin_viewout):
    def __init__(self):
        super(Viewout, self).__init__()
        try:
            self.setupUi(self)
            self.sys_back.clicked.connect(self.homepage)
            self.showdetails()
        except Exception as e:
            print(e)

    def showdetails(self):
        _translate = QtCore.QCoreApplication.translate
        self.labela.setText(_translate("admin_viewout", self.fn))
        self.labelb.setText(_translate("admin_viewout", self.mn))
        self.labelc.setText(_translate("admin_viewout", self.ln))
        self.labeld.setText(_translate("admin_viewout", self.add))
        self.labele.setText(_translate("admin_viewout", self.age))
        self.labelf.setText(_translate("admin_viewout", self.contact))
        self.labelg.setText(_translate("admin_viewout", self.email))
        self.labelh.setText(_translate("admin_viewout", self.cnum))
        self.labeli.setText(_translate("admin_viewout", self.acc))
        self.labelj.setText(_translate("admin_viewout", self.bal))

    def homepage(self):
        self.dialog = Admin_HP.Homepage()
        self.dialog.show()
        self.close()


def main():
    form = Viewout()
    app = QtWidgets.QApplication(sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()