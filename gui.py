import sys
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from calc import calcSolution


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(100, 100, 265, 230)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('calculator.png'))
        self.setWindowTitle('Calculator')

        menubar = self.menuBar()
        exit_ = menubar.addMenu('&Exit')
        help_ = menubar.addMenu('&Help')

        self.calcLine = QLineEdit(self)
        self.calcLine.setReadOnly(True)
        self.calcLine.setGeometry(25, 35, 215, 30)

        button1 = QPushButton('1', self)
        button1.clicked.connect(partial(self.printToBar, 1))
        button1.setGeometry(25, 75, 50, 30)

        button2 = QPushButton('2', self)
        button2.clicked.connect(partial(self.printToBar, 2))
        button2.setGeometry(80, 75, 50, 30)

        button3 = QPushButton('3', self)
        button3.clicked.connect(partial(self.printToBar, 3))
        button3.setGeometry(135, 75, 50, 30)

        buttonPlus = QPushButton('+', self)
        buttonPlus.clicked.connect(partial(self.printToBar, ' + '))
        buttonPlus.setGeometry(190, 75, 50, 30)

        button4 = QPushButton('4', self)
        button4.clicked.connect(partial(self.printToBar, 4))
        button4.setGeometry(25, 110, 50, 30)

        button5 = QPushButton('5', self)
        button5.clicked.connect(partial(self.printToBar, 5))
        button5.setGeometry(80, 110, 50, 30)

        button6 = QPushButton('6', self)
        button6.clicked.connect(partial(self.printToBar, 6))
        button6.setGeometry(135, 110, 50, 30)

        buttonMinus = QPushButton('-', self)
        buttonMinus.clicked.connect(partial(self.printToBar, ' - '))
        buttonMinus.setGeometry(190, 110, 50, 30)

        button7 = QPushButton('7', self)
        button7.clicked.connect(partial(self.printToBar, 7))
        button7.setGeometry(25, 145, 50, 30)

        button8 = QPushButton('8', self)
        button8.clicked.connect(partial(self.printToBar, 8))
        button8.setGeometry(80, 145, 50, 30)

        button9 = QPushButton('9', self)
        button9.clicked.connect(partial(self.printToBar, 9))
        button9.setGeometry(135, 145, 50, 30)

        buttonMulti = QPushButton('x', self)
        buttonMulti.clicked.connect(partial(self.printToBar, ' x '))
        buttonMulti.setGeometry(190, 145, 50, 30)

        buttonReset = QPushButton('AC', self)
        buttonReset.clicked.connect(self.resetCalcLine)
        buttonReset.setGeometry(25, 180, 50, 30)

        button0 = QPushButton('0', self)
        button0.clicked.connect(partial(self.printToBar, 0))
        button0.setGeometry(80, 180, 50, 30)

        buttonEqual = QPushButton('=', self)
        buttonEqual.clicked.connect(self.solve)
        buttonEqual.setGeometry(135, 180, 50, 30)

        buttonDiv = QPushButton('/', self)
        buttonDiv.clicked.connect(partial(self.printToBar, ' / '))
        buttonDiv.setGeometry(190, 180, 50, 30)

    def printToBar(self, inp):
        self.calcLine.setText(str(self.calcLine.text()) + str(inp))

    def resetCalcLine(self):
        self.calcLine.clear()

    def solve(self):
        self.calcLine.setText(calcSolution(str(self.calcLine.text())))

