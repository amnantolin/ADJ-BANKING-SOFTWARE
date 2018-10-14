from Admin_Log import main
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    sys.exit(app.exec_())
