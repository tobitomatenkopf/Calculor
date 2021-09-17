import sys

from PyQt5.QtWidgets import *#

from mainWindow import mainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainWindow()
    w.show()
    sys.exit(app.exec_())
