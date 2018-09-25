from PyQt5 import QtCore, QtGui, QtWidgets
import admin_view
import admin_viewout
import sys
import csv
import os

parent = os.path.dirname(__file__)
accounts = os.path.join(parent, 'accounts.txt')

class View(QtWidgets.QMainWindow, admin_view.Ui_admin_view):
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.sys_cancel.clicked.connect(self.cancel)
        self.sys_confirm.clicked.connect(self.viewaccount)

    def cancel(self):
        self.dialog1 = Homepage()
        self.dialog1.show()
        self.close()

    def viewaccount(self):
        self.anum = []
        self.cnum = []
        self.fn = []
        self.mn =[]
        self.ln = []
        self.add =[]
        self.age = []
        self.contact =[]
        self.email = []
        self.bal = []

        with open(accounts, 'r') as afile:
            reader = csv.reader(afile, delimiter=',')
            for row in reader:
                self.cnum.append(row[0])
                self.anum.append(row[1])
                self.fn.append(row[4])
                self.mn.append(row[5])
                self.ln.append(row[6])
                self.add.append(row[10])
                self.age.append(row[7])
                self.contact.append(row[8])
                self.email.append(row[9])
                self.bal.append(row[3])
                self.anum_inp = self.sys_an.text()
                for i in range(len(self.anum)):
                    if self.anum_inp == self.anum[i]:
                        Viewout.anum = self.anum[i]
                        Viewout.cnum = self.cnum[i]
                        Viewout.fn = self.fn[i]
                        Viewout.mn = self.mn[i]
                        Viewout.ln = self.ln[i]
                        Viewout.add = self.add[i]
                        Viewout.age = self.age[i]
                        Viewout.contact = self.contact[i]
                        Viewout.email = self.email[i]
                        Viewout.bal = self.bal[i]
                        self.accview()
                        break
                    else:
                        self.error()

    def accview(self):
        self.dialog2.close()
        self.dialog3 = Viewout()
        self.dialog3.show()
        self.close()

    def error(self):
        self.dialog2 = Error2()
        self.dialog2.show()

class Viewout(QtWidgets.QMainWindow, admin_viewout.Ui_admin_viewout):
    def __init__(self):
        super(Viewout, self).__init__()
        self.setupUi(self)
        self.sys_back.clicked.connect(self.homepage)
        self.showdetails()

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
        self.labeli.setText(_translate("admin_viewout", self.anum))
        self.labelj.setText(_translate("admin_viewout", self.bal))

    def homepage(self):
        self.dialog = Homepage()
        self.dialog.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()