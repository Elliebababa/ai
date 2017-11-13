# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

#游戏状态 0为平局 ﹢MAX为胜 -MAX为负
DRAW = 0
WIN = sys.maxsize
LOSE = -sys.maxsize

#人为-1，电脑为1
HUMAN = -1
COMPUTER = 1

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 325)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 54, 12))
        self.label.setObjectName("label")
        self.iconNum = -1
        self.start = False
        self.chess = [0 for j in range(9)]
        self.winningState = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        self.playerName ={1:'X方',-1:'O方'}
        self.playerName1 ={1:'你赢了',-1:'你输了'}
        self.playMode = ''
        self.horizontalLayoutWidget =[]
        self.horizontalLayout = []
        for i in range(3):
            horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
            horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40+i*90, 274, 91))
            horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            horizontalLayout.setSpacing(0)
            horizontalLayout.setObjectName("horizontalLayout")
            self.horizontalLayoutWidget.append(horizontalLayoutWidget)
            self.horizontalLayout.append(horizontalLayout)
        
        self.pushButton =[]
        for i in range(9):
                pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget[i//3])
                pushButton.setEnabled(True)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
                pushButton.setSizePolicy(sizePolicy)
                pushButton.setMaximumSize(QtCore.QSize(90, 90))
                pushButton.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("dog.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
                pushButton.setIcon(icon)
                pushButton.setIconSize(QtCore.QSize(80, 80))
                pushButton.setObjectName("pushButton")
                self.horizontalLayout[i//3].addWidget(pushButton)        
                self.pushButton.append(pushButton)

        self.pushButton[0].clicked.connect(lambda:self.moveTo(0))
        self.pushButton[1].clicked.connect(lambda:self.moveTo(1))
        self.pushButton[2].clicked.connect(lambda:self.moveTo(2))
        self.pushButton[3].clicked.connect(lambda:self.moveTo(3))
        self.pushButton[4].clicked.connect(lambda:self.moveTo(4))
        self.pushButton[5].clicked.connect(lambda:self.moveTo(5))
        self.pushButton[6].clicked.connect(lambda:self.moveTo(6))
        self.pushButton[7].clicked.connect(lambda:self.moveTo(7))
        self.pushButton[8].clicked.connect(lambda:self.moveTo(8))

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 40, 60, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(320, 140, 80, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_4)

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(320, 230, 50, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.onStartBtn)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "井字棋"))
        self.radioButton.setText(_translate("Dialog", "先手"))
        self.radioButton_2.setText(_translate("Dialog", "后手"))
        self.radioButton_3.setText(_translate("Dialog", "人机对战"))
        self.radioButton_4.setText(_translate("Dialog", "人人对战"))
        self.pushButton_10.setText(_translate("Dialog", "开始"))

    def moveTo(self,i):
        if self.start:
            if self.chess[i] == 0:
                self.chess[i] = self.iconNum
                icon = QtGui.QIcon()
                if self.iconNum == -1:
                    icon.addPixmap(QtGui.QPixmap("O.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
                else:
                    icon.addPixmap(QtGui.QPixmap("X.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
                self.iconNum *= -1
                self.pushButton[i].setIcon(icon)
                self.pushButton[i].setIconSize(QtCore.QSize(80, 80))
                if self.playMode == 'HvsH':
                    result = self.checkWinning(self.chess)
                    if result[0] > 0:
                        QMessageBox().information(self,"提示","游戏结束！"+ self.playerName[result[1]] +"胜出",QMessageBox.Ok)
                        self.start = False
                        self.resetIcon()
                else:
                    result = self.checkWinning(self.chess)
                    if result[0] > 0:
                        QMessageBox().information(self,"提示","游戏结束！"+ self.playerName1[result[1]],QMessageBox.Ok)
                        self.start = False
                        self.resetIcon()
                    else:
                        self.minmax()
                    
                
        else:
            QMessageBox().warning(self,"提示","请点击开始！",QMessageBox.Ok)
        
                    
    def resetIcon(self):
        for i in range(3):
            for j in range(3):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("dog.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
                self.pushButton[i][j].setIcon(icon)
                self.pushButton[i][j].setIconSize(QtCore.QSize(80, 80))
                self.chess[i][j] = 0

    def checkWinning(self,chess):
    #检查胜出的一方
        count = 0 #满足胜出条件个数
        winner = 0
        for i in range(8):
            pWinner = 0
            flag = 0 #判断为集合中的第几个元素
            for x in self.winningState[i]:
                if flag == 0:
                    pWinner = chess[x//3][x%3]
                    flag += 1
                else:
                    if pWinner != chess[x//3][x%3]:
                        flag = -1#-1无意义
                        break
                    else:
                        flag += 1
                if flag == 3 and pWinner != 0:
                    count+= 1
                    winner = pWinner
                    print(count,pWinner)
                    break
        return [count,winner]

    def gameState(self,chess,depth):
    #看看是否全部旗子都已下满
        
        finished = True
        for i in range(3):
            for j in range(3):
                if chess[i][j] == 0:
                    finished = False
                    break
            if finished == False:
                break

        check = self.checkWinning(chess)
        
        if finished and check[0] == 0:
            return [searchDepth+1,DRAW]
        elif check[0] > 0:
            if check[1] == HUMAN:
                return [searchDepth+1,LOSE]
            else:
                return [searchDepth+1,WIN]
        
        #暂无胜负则估计当前局势
        #预估人胜利的局面
        virChess = chess
        for i in range[3]:
            for j in range[3]:
                if virChess[i][j] == 0:
                    virChess[i][j] = -1
        result = self.checkWinning(virChess)
        humanWinning = result[0]

        #预估机器胜利的局面
        virChess = chess
        for i in range[3]:
            for j in range[3]:
                if virChess[i][j] == 0:
                    virChess[i][j] = 1
        result = self.checkWinning(virChess)
        comWinning = result[0]
        
        return [depth+1,comWinning-humanWinning]           

    def minSearch(self,chess,depth):
        pointState = gameState(chess,depth)
        if pointState[1] == DRAW:
            return 0
        if pointState[0] >= MAXDEPTH or pointState[1] == WIN or pointState[1] == LOSE:
            return pointState[1]
        else:
            bestMin = sys.maxsize
            for i in range(3):
                for j in range(3):
                    if chess[i][j] == 0:
                        chess[i][j] = 1
                        maxS = maxSearch(chess,pointState[0])
                        if maxS < bestMin:
                            bestMin = maxS
                        chess[i][j] = 0
            return bestMin


    def maxSearch(self,chess,depth):
        pointState = gameState(chess,depth)
        if pointState[1] == DRAW:
            return 0
        bestMax = sys.minsize
        for i in range(3):
            for j in range(3):
                if chess[i][j] == 0:
                    chess[i][j] = -1
                    minS = minSearch(chess,pointState[0])
                    if minS < bestMax:
                        bestMax = minS
                    chess[i][j] = 0
        return bestMax
    
    def minmax(self):
        best = -sys.maxsize
        
        for i in range(3):
            for j in range(3):
                if self.chess[i][j] == 0:
                    self.chess[i][j] = 1
                    minS = minSearch(self.chess,0)
                    if minS > best:
                        best = minS
                        move = [i,j]
                    self.chess[i][j] = 0
       
        if best != -sys.maxsize:
            self.moveTo(move[0],move[1])
        else:
            QMessageBox().information(self,"提示","游戏结束！你赢了！",QMessageBox.Ok)
            self.start = False
            self.resetIcon()
        
    def onStartBtn(self):
            self.resetIcon()
            if self.radioButton_4.isChecked():
                self.start = True
                self.playMode = 'HvsH'
            elif self.radioButton_3.isChecked():
                if self.radioButton.isChecked() or self.radioButton_2.isChecked():
                    self.start = True
                    self.playMode = 'HvsC'
                    if self.radioButton_2.isChecked():
                        self.minmax()
                else:
                    QMessageBox().warning(self,"人机对战","请选择先后顺序！",QMessageBox.Ok)
            else:
                QMessageBox().warning(self,"提示","请选择游戏模式！",QMessageBox.Ok)
        
if __name__ == "__main__":   
    app = QApplication(sys.argv)   
    myapp = Ui_Dialog()   #MyForm是自己的窗体类名
    myapp.setupUi(myapp)
    myapp.show()   
    sys.exit(app.exec_())  
