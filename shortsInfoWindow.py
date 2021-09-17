import sys
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ShortsInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()
        
    def initMe(self):
        self.setGeometry(300, 300, 200, 100)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('Icons/ctrl.png'))
        self.setWindowTitle('Shortcuts')
        font = QFont('Arial', 12)

        textBox = QLabel('Shortcuts:  Buttons 1-9: 1-9\nOperators:  +, -, x, /\nAC:  Ctrl+BackSpace\n'
                         'Equal(=):  Enter\nExit:  Ctrl+E', self)
        textBox.setGeometry(0, 0, 200, 100)
        textBox.setFont(font)

        self.show()
