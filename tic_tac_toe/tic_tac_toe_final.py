# -*- coding: utf-8 -*-
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


#游戏状态 0为平局 ﹢MAX为A胜 -MAX为B胜
DRAW = 0
WIN = sys.maxsize
LOSE = -sys.maxsize

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 325)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 54, 12))
        self.label.setObjectName("label")
        self.player = -1
        self.start = False
        self.chess = [0 for j in range(9)]
        self.playerName ={1:'X方',-1:'O方'}
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

    def checkWinning(self,chess,somebody):
    #检查somebody是否胜利
        winningState = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        winFlag = False
        for i in range(8):
            winFlag = True
            for x in winningState[i]:
                if chess[x] != somebody:
                    winFlag = False
                    break
            if winFlag:
                return True
        return False

    def moveTo(self,i):
    #somebody在i处下棋
        if self.start:
            if self.chess[i] == 0:
                icon = QtGui.QIcon()
                if self.player == 1:
                    icon.addPixmap(QtGui.QPixmap("X.png"), QtGui.QIcon.Normal,QtGui.QIcon.On)
                else:
                    icon.addPixmap(QtGui.QPixmap("O.png"), QtGui.QIcon.Normal,QtGui.QIcon.On)
                self.pushButton[i].setIcon(icon)
                self.pushButton[i].setIconSize(QtCore.QSize(80, 80)) 
                self.chess[i] = self.player
                if self.checkWinning(self.chess,self.player):
                    self.start = False
                    QMessageBox().information(self,"提示",str(self.playerName[self.player])+'胜出！',QMessageBox.Ok)
                    self.resetChess()
                else:
                    finished = True
                    for i in range(9):
                        if self.chess[i] == 0:
                            finished = False
                            break
                    if finished:
                        self.start = False
                        QMessageBox().information(self,"提示",'平局！',QMessageBox.Ok)
                        self.resetChess()
                    else:
                        if self.playMode == 'HvsH':
                            self.player *= -1
                        else:
                            if self.player == 1:
                                self.player = -1
                                move = self.minmax(self.chess,-1,0)
                                self.moveTo(move[0])
                            else:
                                self.player = 1
        else:
            QMessageBox().warning(self,"提示","请点击开始！",QMessageBox.Ok)
                  
    def resetChess(self):
    #重置棋盘
        for i in range(9):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("dog.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
            self.pushButton[i].setIcon(icon)
            self.pushButton[i].setIconSize(QtCore.QSize(80, 80))
            self.chess[i] = 0

    def evaluate(self,chess,emptyPosition):
        winningState = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        posCount = 0
        negCount = 0
        for i in range(8):
            pos = 0
            neg = 0
            for x in winningState[i]:
                if chess[x] == 1 or x in emptyPosition:
                    pos += 1
                elif chess[x] == -1 or x in emptyPosition:
                    neg += 1
            if pos == 3:
                posCount+=1
            elif neg == 3:
                posCount+=1
        #print(posCount-negCount)
        return posCount-negCount
                

    def minmax(self,chess,player,depth):
        if (self.checkWinning(chess,1)):
            return [0,sys.maxsize]
        if (self.checkWinning(chess,-1)):
            return [0,-sys.maxsize]
        emptyPosition =[]
        for i in range(9):
            if chess[i] == 0:
                emptyPosition.append(i)
        if emptyPosition ==[]:
            return [0,0]
        
        if depth >=6:
            #print(player,'depth',depth,self.evaluate(chess,emptyPosition))
            return [0,self.evaluate(chess,emptyPosition)]
        else:
            pos = 0
            if player == 1:
                best = -100
                for i in range(len(emptyPosition)):
                    self.chess[emptyPosition[i]] = player
                    v = self.minmax(self.chess,-player,depth+1)
                    #print(v,v[1])
                    if v[1] > best:
                        best = v[1]
                        pos = emptyPosition[i]
                    #print(player,best)
                    self.chess[emptyPosition[i]] =0
            else:
                best = 100
                for i in range(len(emptyPosition)):
                    self.chess[emptyPosition[i]] = player
                    v = self.minmax(self.chess,-player,depth+1)
                    if v[1] < best:
                        best = v[1]
                        pos = emptyPosition[i]
                    self.chess[emptyPosition[i]] =0
            return [pos,best]

    def onStartBtn(self):
            self.resetChess()
            if self.radioButton_4.isChecked():
                self.start = True
                self.playMode = 'HvsH'
            elif self.radioButton_3.isChecked():
                if self.radioButton.isChecked() or self.radioButton_2.isChecked():
                    self.start = True
                    self.playMode = 'HvsC'
                    if self.radioButton_2.isChecked():
                        #后手
                        move = self.minmax(self.chess,-1,0)
                        self.player = -1
                        self.moveTo(move[0])
                    else:
                        self.player = 1
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
