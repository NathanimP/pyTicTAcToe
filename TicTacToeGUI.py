from PyQt5.QtWidgets import QPushButton as Button
from PyQt5.QtWidgets import QMainWindow as Main
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QMessageBox as msgbox
from PyQt5.QtGui import QFont
from random import choice

import sys
class MyApp(Main):

    def __init__(self):
        super(MyApp, self).__init__()
        self.setGeometry(300,200,300,300)
        self.setWindowTitle('TicTacToe Game')
        self.Play()
        self.j=0
        self.text = "X"
        self.msg = msgbox(self)
        self.comp_nums = [self.b1, self.b2, self.b3, self.b4, self.b1, self.b1, self.b1, self.b1, self.b1, ]
        self.num = choice(self.comp_nums)
    def Play(self):
        self.Buttons()
    def Buttons(self):
        self.b1 = Button(self)
        self.b1.setGeometry(0,0,100,100)
        self.b1.clicked.connect(lambda:self.TicTacToe(self.b1))
        self.b2 = Button(self)
        self.b2.setGeometry(100, 0, 100, 100)
        self.b2.clicked.connect(lambda:self.TicTacToe(self.b2))
        self.b3 = Button(self)
        self.b3.setGeometry(200, 0, 100, 100)
        self.b3.clicked.connect(lambda:self.TicTacToe(self.b3))
        self.b4 = Button(self)
        self.b4.setGeometry(0, 100, 100, 100)
        self.b4.clicked.connect(lambda:self.TicTacToe(self.b4))
        self.b5 = Button(self)
        self.b5.setGeometry(100, 100, 100, 100)
        self.b5.clicked.connect(lambda:self.TicTacToe(self.b5))
        self.b6 = Button(self)
        self.b6.setGeometry(200,100, 100, 100)
        self.b6.clicked.connect(lambda:self.TicTacToe(self.b6))
        self.b7 = Button(self)
        self.b7.setGeometry(0, 200, 100, 100)
        self.b7.clicked.connect(lambda:self.TicTacToe(self.b7))
        self.b8 = Button(self)
        self.b8.setGeometry(100, 200, 100, 100)
        self.b8.clicked.connect(lambda:self.TicTacToe(self.b8))
        self.b9 = Button(self)
        self.b9.setGeometry(200, 200, 100, 100)
        self.b9.clicked.connect(lambda:self.TicTacToe(self.b9))
    def TicTacToe(self,btn):
        if btn.text() != "O" and btn.text()!='X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)

        elif btn.text() != "O" and btn.text() != 'X':
            btn.setText(self.text)
        else:
            self.msg.setText("Already Clicked")
            self.j-=1
            self.msg.showNormal()
            if self.text == "X":
                self.text = "O"
            else:
                self.text = "X"
        if self.text == "X":
            self.text = "O"
        else:
            self.text = "X"
        self.j+=1
        font = QFont("Goudy Stout")
        btn.setFont(font)
        self.CheckWinner()
    def CheckWinner(self):
        if self.b1.text()=="X" and self.b2.text()=="X" and self.b3.text()=="X"\
            or  self.b1.text()=="X" and self.b2.text()=="X" and self.b3.text()=="X"\
            or  self.b1.text()=="X" and self.b4.text()=="X" and self.b7.text()=="X"\
            or  self.b1.text()=="X" and self.b5.text()=="X" and self.b9.text()=="X"\
            or  self.b2.text()=="X" and self.b5.text()=="X" and self.b8.text()=="X"\
            or  self.b3.text()=="X" and self.b6.text()=="X" and self.b9.text()=="X"\
            or  self.b3.text()=="X" and self.b5.text()=="X" and self.b7.text()=="X"\
            or  self.b7.text()=="X" and self.b8.text()=="X" and self.b9.text()=="X"\
            or  self.b4.text()=="X" and self.b5.text()=="X" and self.b6.text()=="X":
            self.DisableButtons()
            self.msg.setText("X wins\nDo you Want Play Again?")
            self.msg.showNormal()
        elif self.b1.text()=="O" and self.b2.text()=="O" and self.b3.text()=="O"\
            or  self.b1.text()=="O" and self.b2.text()=="O" and self.b3.text()=="O"\
            or  self.b1.text()=="O" and self.b4.text()=="O" and self.b7.text()=="O"\
            or  self.b1.text()=="O" and self.b5.text()=="O" and self.b9.text()=="O"\
            or  self.b2.text()=="O" and self.b5.text()=="O" and self.b8.text()=="O"\
            or  self.b3.text()=="O" and self.b6.text()=="O" and self.b9.text()=="O"\
            or  self.b3.text()=="O" and self.b5.text()=="O" and self.b7.text()=="O"\
            or  self.b7.text()=="O" and self.b8.text()=="O" and self.b9.text()=="O"\
            or  self.b4.text()=="O" and self.b5.text()=="O" and self.b6.text()=="O":
            self.DisableButtons()
            self.msg.setText("O wins\nDo you Want Play Again?")
            self.msg.showNormal()
        else:
            if self.j==9:
                self.DisableButtons()
                self.msg.setText("It is tie :(")
                self.msg.showNormal()
    def DisableButtons(self):
        self.b1.setDisabled(True)
        self.b2.setDisabled(True)
        self.b3.setDisabled(True)
        self.b4.setDisabled(True)
        self.b5.setDisabled(True)
        self.b6.setDisabled(True)
        self.b7.setDisabled(True)
        self.b8.setDisabled(True)
        self.b9.setDisabled(True)
    def RestartTheGame(self):
        ...
if __name__ == '__main__':
    app = App(sys.argv)
    win=MyApp()
    win.show()
    sys.exit(app.exec_())
