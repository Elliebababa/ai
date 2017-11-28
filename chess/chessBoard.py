from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import chessai_minimax
from threading import Thread
chessSize = 56
chessAreaX =[0,0, 57, 115, 173, 231, 288, 346, 404, 462]
chessAreaY =[0,0, 57, 115, 172, 230, 290, 348, 405, 463, 520]
chessList = ['BA','BB','BC','BK','BN','BP','BR','RA','RB','RC','RK','RN','RP','RR']
bChess = {0:[14,16],1:[13,17],2:[32,38],3:[15],4:[12,18],5:[41,43,45,47,49],6:[11,19]}
rChess = {7:[104,106],8:[103,107],9:[82,88],10:[105],11:[102,108],12:[71,73,75,77,79],13:[101,109]}
blackPlayer = 1
redPlayer = -1

class chessBoard(QWidget):
    def __init__(self,parent):
        super(chessBoard,self).__init__(parent)
        self.mode = 'HvsC'
        self.timer = QtCore.QTimer()
        self.timeout = 10000
        self.bChess = {}
        self.rChess = {}
        self.painter = QtGui.QPainter(self)
        self.board = {(i+1)*10 + j+1 : -1 for i in range (10) for j in range(9)}
        self.focus = -1
        self.Maxdepth = 4
        self.end = False
        self.pause = False
        self.player = blackPlayer
        self.setBackground()
        self.placeChess()


    def placeChess(self):
        #摆放棋子
        self.board = {(i+1)*10 + j+1 : -1 for i in range (10) for j in range(9)}
        
        for j in bChess:
            self.bChess[j] = bChess[j].copy()
            for pos in self.bChess[j]:
                self.board[pos]=j
                
        for j in rChess:
            self.rChess[j] = rChess[j].copy()
            for pos in self.rChess[j]:
                self.board[pos] = j
        self.update()

    def setBackground(self):
        #放置棋盘
        self.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QPixmap('RES\\BOARD.bmp'))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(),brush)
        self.setPalette(palette)
        
    
    def paintEvent(self,QPaintEvent):
        self.painter.begin(self)
        pixmap = QtGui.QPixmap('RES\\BA.BMP')
        mask = QtGui.QBitmap('RES\\mask.bmp')
        for key in self.board:
            if self.board[key] != -1:
                path = 'RES\\'+chessList[self.board[key]]+'.BMP'
                pixmap.load(path)
                pixmap.setMask(mask)
                self.painter.drawPixmap(chessAreaX[key % 10],chessAreaY[key // 10],pixmap)
        if self.focus != -1:
            path = 'RES\\'+chessList[self.board[self.focus]]+'.BMP'
            pixmap.load(path)
            self.painter.drawPixmap(chessAreaX[self.focus % 10],chessAreaY[self.focus // 10],pixmap)    
        self.painter.end()
            
        
         
    
    def mousePressEvent(self,QMouseEvent):
            #没有棋子被选中的状态，判断点击的地方是否选中棋子
        if not self.pause and not self.end and (self.mode == 'HvsH' or (self.mode == 'HvsC' and self.player == blackPlayer)):
            if self.focus == -1:
                self.focus = self.chessSelected(QMouseEvent)
                self.update()

                    #有棋子选中的状态，判断点击的地方是否可以移动，并做相应的移动
            else:
                point = self.focus
                movetoX = QMouseEvent.x()
                movetoY = QMouseEvent.y()
                self.move(point,movetoX,movetoY)
                self.update()   
                self.focus = -1
        
    def move(self,point,movetoX,movetoY):
        chessType = self.board[point] % 7
        if self.board[point] // 7 == 0:
            chesscolor = blackPlayer
        else:
            chesscolor = redPlayer

        if not chesscolor == self.player:
            return False
        
        for i in range(9):
            for j in range(10):
                if chessAreaX[i+1] < movetoX and  chessAreaX[i+1]+chessSize > movetoX and chessAreaY[j+1] < movetoY and  chessAreaY[j+1]+chessSize > movetoY:
                    #找到点击区域
                    clickX = i+1
                    clickY = j+1
                    clickpos = clickX+clickY*10
                    focusX = point % 10
                    focusY = point // 10
                    moveable = False

                    
                    #没有移动
                    if clickX == focusX and clickY == focusY:
                        break
                    
                    #判断区域是否可下
                    #不能有自己的棋子
                    if chesscolor == blackPlayer:#黑方
                        if self.board[clickpos] in range(0,7):
                            break
                    if chesscolor == redPlayer:#红方
                        if self.board[clickpos] in range(7,14):
                            break

                    
                    #按规则行走
                    if chessType == 0:#士 仅能在米字格内行走米字
                        if abs(clickX - 5) <=1 and (abs(clickY - 2)<= 1 or abs(clickY - 9)<= 1) :
                            if abs(clickX - focusX)+abs(clickY - focusY) == 1:
                                moveable = True
                            if (focusX+focusY) % 2 == (chesscolor + 1)//2:
                                if abs(clickX - focusX) == 1 and abs(clickY - focusY) == 1:
                                    moveable = True
                  
                    elif chessType == 1:#象 仅能在河内走田字 田字中间不能隔着棋子
                        if (chesscolor == blackPlayer and clickY <= 5) or (chesscolor == redPlayer and clickY >= 6):
                            if abs(clickX - focusX) == 2  and abs(clickY - focusY) == 2:
                                if self.board[(clickX + focusX)/2+(clickY + focusY)/2*10] == -1:
                                    moveable = True

                    elif chessType == 2:#炮 不吃棋子可以直走 直走中间不能隔着棋子 吃棋子要隔着一只棋子
                        if (clickX == focusX):
                            count = -1
                            if clickY < focusY:
                                sPos,ePos = clickY,focusY
                            else:
                                ePos,sPos = clickY,focusY
                            for i in range(sPos,ePos+1):
                                if self.board[clickX+i*10] != -1:
                                    count+=1
                        elif (clickY == focusY):
                            count = -1
                            if clickX < focusX:
                                sPos,ePos = clickX,focusX
                            else:
                                ePos,sPos = clickX,focusX

                            for i in range(sPos,ePos+1):
                                if self.board[clickY*10+i] != -1:
                                    count+=1
                        else:
                            break
                        if (self.board[clickpos] != -1 and count == 2) or (self.board[clickpos] == -1 and count == 0):
                            moveable = True
                        else:
                            break
                            

                    elif chessType == 3:#将 仅能在米字格内行走直线
                        if abs(clickX - 5) <=1 and (abs(clickY - 2)<= 1 or abs(clickY - 9)<= 1) :
                            if abs(clickX - focusX)+abs(clickY - focusY) == 1:
                                moveable = True
                        if (chesscolor == blackPlayer and clickX == self.rChess[10][0]%10) or (chesscolor == redPlayer and clickX== self.bChess[3][0]%10):
                            count = 0
                            for i in range(self.bChess[3][0]//10+1,self.rChess[10][0]//10):
                                if not self.board[i*10+clickX] == -1:
                                    count +=1
                            if count == 0:
                                break   

                    elif chessType == 4:#马 走日字 不能绊马脚
                        if abs(clickX - focusX) > 0 and abs(clickY - focusY) > 0 and abs(clickX - focusX)+abs(clickY - focusY) == 3:
                            if abs(clickY - focusY) ==2:
                                if self.board[focusX+(clickY + focusY)/2*10] == -1:
                                    moveable = True
                            else:
                                if self.board[focusY*10+(clickX + focusX)/2] == -1:
                                    moveable = True
                        else:
                            break

                    

                    elif chessType == 5:#卒 过河前直走 过河后任意走 不能后退

                        if (chesscolor == blackPlayer and clickY <= 5) or (chesscolor == redPlayer and clickY >= 6):
                            over = False
                        else:
                            over = True

                        if not over and not (clickX == focusX):#未过河不能打横走
                            break

                        if (chesscolor == blackPlayer and clickY < focusY) or (chesscolor == redPlayer and clickY > focusY):#不能后退
                            break

                        if abs(clickX - focusX)+abs(clickY - focusY) == 1:
                                moveable = True

                    elif chessType == 6:#车 直走 中间不能隔着棋子
                        if (clickX == focusX):
                            count = 0
                            if clickY < focusY:
                                sPos,ePos = clickY,focusY
                            else:
                                ePos,sPos = clickY,focusY
                            for i in range(sPos+1,ePos):
                                if self.board[clickX+i*10] != -1:
                                    count+=1
                        elif clickY == focusY:
                            count = 0
                            if clickX < focusX:
                                sPos,ePos = clickX,focusX
                            else:
                                ePos,sPos = clickX,focusX
                            for i in range(sPos+1,ePos):
                                if self.board[clickY*10+i] != -1:
                                    count+=1
                        else:
                            break
                        if (count == 0):
                            moveable = True
                        else:
                            break
                    
                    #将帅不能照面
                    if (not chessType == 3 and self.rChess[10][0]%10 == self.bChess[3][0]%10 == focusX and not clickX==focusX):
                        count = 0
                        for i in range(self.bChess[3][0]//10+1,self.rChess[10][0]//10):
                            if not self.board[i*10+focusX] == -1:
                                count +=1
                        if count == 1:
                            break       
                                    

                    if moveable:
                        
                        if not self.board[clickpos] == -1:#对手棋子被吃掉
                            if chesscolor == redPlayer:
                                self.bChess[self.board[clickpos]].remove(clickpos)
                            else:
                                self.rChess[self.board[clickpos]].remove(clickpos)
                        if chesscolor == redPlayer:
                            c = self.board[point]
                            i = self.rChess[c].index(point)
                            self.rChess[c][i] = clickpos
                        else:
                            c = self.board[point]
                            i = self.bChess[c].index(point)
                            self.bChess[c][i] = clickpos
                        self.board[clickpos] = self.board[point]
                        self.board[point] = -1
                        self.player = -self.player #成功移动交换玩家
                        #print(self.rChess,self.bChess)
                        self.timer.start(self.timeout)
                        #print(self.player,self.timer.remainingTime())
                        self.update()

                        self.checkWinning()
                        
                        if not self.end and self.mode == 'HvsC' and self.player == redPlayer:
                            
                            chessai = chessai_minimax.chessai(self.board,self.Maxdepth)
                            #人机模式 在人成功下棋之后 电脑马上进行计算
                            #t1 = Thread(taself.ui.board.player = redPlayer
                            t1 = Thread(target = chessai.generateMove,args = (self.move,),daemon =False)
                            t1.start()

                        return True

                    break
                        
        return False
        

    def chessSelected(self,QMouseEvent):
        for i in range(9):
            for j in range(10):
                if chessAreaX[i+1] < QMouseEvent.x() and  chessAreaX[i+1]+chessSize > QMouseEvent.x() and chessAreaY[j+1] < QMouseEvent.y() and  chessAreaY[j+1]+chessSize > QMouseEvent.y():
                    focus = (i+1)+(j+1)*10
                    if self.board[focus] != -1:
                        return focus
                    else:
                        return -1
                        
        return -1


    def checkWinning(self):
        if not len(self.rChess[10]):
            self.end = True
        elif not len(self.bChess[3]):
            self.end = True
        if self.end:
            self.timer.stop()
