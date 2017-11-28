from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from threading import Thread
from chessui import Ui_Form
import chessai_random
import chessai_minimax
import sys
from time import sleep
blackPlayer = 1
redPlayer = -1
timeout = [21,61,121,601]
mode = ['HvsH','HvsC']
class chessGame():
    def __init__(self):
        #setupUi
        self.ui = Ui_Form()
        self.ui.setupUi(self.ui)
        self.ui.board.player = 0
        self.ui.startButton.clicked.connect(self.gameOn)
        self.ui.pauseButton.clicked.connect(self.pauseOn)
        self.ui.endButton.clicked.connect(self.endOn)


    def gameOn(self):
        msg = "游戏开始！黑方先行"
        self.ui.listWidget.addItem(" ")
        self.ui.listWidget.addItem(msg)
        self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
        self.ui.startButton.setText("重新开始")
        self.timeRefresher = QtCore.QTimer()
        self.ui.board.end = False
        self.ui.board.pause = False
        self.ui.board.timeout = timeout[self.ui.timeBox.currentIndex()]*1000
        self.ui.board.Maxdepth = self.ui.timeBox.currentIndex()+2
        self.ui.board.mode = mode[self.ui.playmodeBox.currentIndex()]
        self.ui.board.placeChess()
        self.ui.board.player = blackPlayer
        self.ui.board.timer.timeout.connect(self.RanMoveOn)#计时器
        self.timeRefresher.timeout.connect(self.updatetimeCount)
        self.ui.board.timer.start(self.ui.board.timeout)
        self.timeRefresher.start(1000)
        
    def RanMoveOn(self):
        if not (self.ui.board.end or self.ui.board.pause): 
            if self.ui.board.player == 1:#当前玩家
                msg = "黑方"
            else:
                msg = "红方"
            msg += "超时, 随机行棋"
            self.ui.listWidget.addItem(msg)
            self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
            p = self.ui.board.player
            if p == blackPlayer:#若当前玩家仍为黑
                while self.ui.board.player == blackPlayer:
                    [point,movetoX,movetoY] = chessai_random.generateMove(self.ui.board)
                    self.ui.board.move(point,movetoX,movetoY)
            elif p == redPlayer:#若当前玩家为红色 
                while self.ui.board.player == redPlayer:
                    [point,movetoX,movetoY] = chessai_random.generateMove(self.ui.board)
                    self.ui.board.move(point,movetoX,movetoY)
                    

    def updatetimeCount(self):
        if not (self.ui.board.end or self.ui.board.pause):
            if self.ui.board.timer.remainingTime() == -1:
                self.ui.board.timer.start(self.ui.board.timeout)
            self.ui.timeCount.setProperty("intValue", self.ui.board.timer.remainingTime()//1000)
            if self.ui.board.player == 1:
                self.ui.lcurrentPlayer.setText("黑方")
            else:
                self.ui.lcurrentPlayer.setText("红方")
            self.ui.update()
        
        elif self.ui.board.end:
            if self.ui.board.player == -1:
                msg = "黑方胜出"
                self.ui.listWidget.addItem(msg)
                self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
            elif self.ui.board.player == 1:
                msg = "红方胜出"
                self.ui.listWidget.addItem(msg)
                self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
            self.ui.board.player = 0
            
        
    def pauseOn(self):

        if self.ui.board.pause:
            msg = "游戏继续"
            self.ui.board.pause = False
            self.ui.pauseButton.setText("暂停")
            self.ui.board.timer.start(self.remaining)
        else:
            msg = "游戏暂停"
            self.ui.board.pause = True
            self.ui.pauseButton.setText("继续")
            self.remaining = self.ui.board.timer.remainingTime()
            self.ui.board.timer.stop()

        self.ui.listWidget.addItem(msg)
        self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
        

    def endOn(self):
        self.ui.board.player = 0
        msg = "游戏结束"
        self.ui.listWidget.addItem(msg)
        self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
        self.ui.board.end = True

#直接调用新的ui.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chessGame()
    ex.ui.show()
    sys.exit(app.exec_())
