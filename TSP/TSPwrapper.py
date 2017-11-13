from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from tspui import Ui_Form
from TSPcanvas import TSPCanvas
import numpy as np
import sys

import matplotlib
matplotlib.use('Qt5Agg')  
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import math
import random as r


#ui.py文件需要将添加import "from PyQt5.QtWidgets import *"
#ui.py文件需要将UiForm的object改为对应的继承的类 QWidget

class TSP():
    def __init__(self,X,Y):
        super(TSP,self).__init__()
        self.X = X.copy()
        self.Y = Y.copy()
        self.X[0] = self.X[-1]
        self.Y[0] = self.Y[-1]
        l = len(X)
        self.cityNum = l - 1
        #计算城市间距离，存放在distance中
        self.distance = [[ col for col in range(l)] for row in range(l)]
        for i in range(1,l):
            self.distance[i][i] = 0
            for j in range(i+1,l):
                temp = 111.199*math.pow(pow(X[i]-X[j],2)+pow(Y[i]-Y[j],2)*pow(math.cos((X[i]+X[j])/2/180*math.pi),2),0.5)
                self.distance[i][j] = temp
                self.distance[j][i] = temp
        self.tour = [i+1 for i in range(len(X)-1)]
        self.dis = self.calDis(self.tour)
        self.iterTimes,self.iterDis=[],[]
        self.T = 80
        self.dropRate = 0.6
        self.optMode = 4
        
        #setupUi
        self.ui = Ui_Form()
        self.ui.setupUi(self.ui)
        self.ui.rate1.setText(str(self.dropRate))
        self.ui.T1.setText(str(self.T))

        #setupCanvas
        self.canvas1 = TSPCanvas()
        self.ui.verticalLayout.addWidget(self.canvas1)
        self.line, = self.canvas1.ax.plot(self.X,self.Y,'b-',animated =True)

        self.canvas2 = TSPCanvas()
        self.ui.verticalLayout_2.addWidget(self.canvas2)
        self.line2, = self.canvas2.ax.plot(self.iterTimes,self.iterDis,'b-',animated =True)
        
        #setUpBtn
        self.ui.radioButton_5.setChecked(True)
        self.ui.radioButton.setChecked(True)
        self.ui.pushButton.setEnabled(False)
        
        #bindButton
        self.ui.startButton.clicked.connect(self.on_start)
        self.ui.pushButton.clicked.connect(self.on_pause)

    def resetUp(self):
        self.tour = [i+1 for i in range(len(self.X)-1)]
        self.dis = self.calDis(self.tour)
        #setupCanvas
        self.canvas1.ax.clear()
        self.line, = self.canvas1.ax.plot(self.X,self.Y,'b-',animated =True)
        self.canvas2.ax.clear()
        self.iterTimes,self.iterDis=[],[]
        self.line2, = self.canvas2.ax.plot(self.iterTimes,self.iterDis,'b-',animated =True)
        
       

    def update(self,frame):
        self.ls()
        x = [self.X[i] for i in self.tour]
        x.append(x[0])
        y = [self.Y[i] for i in self.tour]
        y.append(y[0])
        self.line.set_data(x, y)
        self.iterTimes.append(frame)
        self.iterDis.append(self.dis)

        xmin, xmax = self.canvas2.ax.get_xlim()
        if frame >= xmax:
            self.canvas2.ax.set_xlim(xmin, 2*xmax)
        
        self.line2.set_data(self.iterTimes, self.iterDis)
        return self.line,self.line2,

    def update2(self,frame):
        self.sa()
        x = [self.X[i] for i in self.curTour]
        x.append(x[0])
        y = [self.Y[i] for i in self.curTour]
        y.append(y[0])
        self.line.set_data(x, y)
        self.iterTimes.append(frame)
        self.iterDis.append(self.curDis)

        xmin, xmax = self.canvas2.ax.get_xlim()
        if frame >= xmax:
            self.canvas2.ax.set_xlim(xmin, 2*xmax)

        ymin, ymax = self.canvas2.ax.get_ylim()
        if self.curDis >= ymax:
            self.canvas2.ax.set_ylim(ymin, self.curDis)
        
        self.line2.set_data(self.iterTimes, self.iterDis)
        return self.line,self.line2,

    def init(self):
        #self.canvas2.ax.autoscale()
        self.canvas2.ax.set_xlim(0, 100)
        self.canvas2.ax.set_ylim(40000,60000)
        self.canvas2.ax.set_yticks([40000,60000])
        return self.line2,

    
    def on_start(self):
        
        #initSetup
        self.resetUp()
        #setUpBtn
        self.ui.pushButton.setEnabled(False)
        self.ui.startButton.setDown(True)
        self.ui.startButton.setEnabled(False)
        self.ui.radioButton_2.setEnabled(False)
        self.ui.radioButton_6.setEnabled(False)
        self.ui.radioButton_3.setEnabled(False)
        self.ui.radioButton_4.setEnabled(False)
        self.ui.radioButton_5.setEnabled(False)
        self.ui.radioButton.setEnabled(False)
        self.ui.T1.setEnabled(False)
        self.ui.rate1.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        if self.ui.radioButton_2.isChecked():#LS
            if self.ui.radioButton_6.isChecked():#SWAP2
                self.optMode = 1
            elif self.ui.radioButton_3.isChecked():#2OPT
                self.optMode = 2
            elif self.ui.radioButton_4.isChecked():#OPOPT
                self.optMode = 3
            elif self.ui.radioButton_5.isChecked():#COMBINE
                self.optMode = 4
            self.animation = FuncAnimation(self.canvas1.fig, self.update,interval = 0,blit=True,frames = 40000,repeat=False)
            self.animation = FuncAnimation(self.canvas2.fig, self.update,init_func=self.init,interval = 0,blit=True,frames = 40000,repeat=False)
        elif self.ui.radioButton.isChecked():#SA
            self.dropRate = float(self.ui.rate1.text())
            self.T = float(self.ui.T1.text())
            self.animation = FuncAnimation(self.canvas1.fig, self.update2,interval = 0,blit=True,frames = 40000,repeat=False)
            self.animation = FuncAnimation(self.canvas2.fig, self.update2,init_func=self.init,interval = 0,blit=True,frames = 40000,repeat=False)

    def on_pause(self):
        self.animation.event_source.stop()
        self.ui.pushButton.setEnabled(False)
        self.ui.startButton.setEnabled(True)
        self.ui.startButton.setDown(False)
        self.ui.radioButton_2.setEnabled(True)
        self.ui.radioButton_6.setEnabled(True)
        self.ui.radioButton_3.setEnabled(True)
        self.ui.radioButton_4.setEnabled(True)
        self.ui.radioButton_5.setEnabled(True)
        self.ui.radioButton.setEnabled(True)
        self.ui.T1.setEnabled(True)
        self.ui.rate1.setEnabled(True)
        
    def ls(self):
        if (self.optMode == 1):
            newTour,newDis = self.swap2(self.tour)
        elif (self.optMode == 2):
            newTour,newDis = self.opt2(self.tour)
        elif (self.optMode == 3):
            newTour,newDis = self.oropt(self.tour)
        elif (self.optMode == 4):
            newTour,newDis = self.combine(self.tour)
        
        if newDis < self.dis:
            self.dis = newDis
            self.tour = newTour.copy()
            str = "次数:%d"%(self.iterTimes[-1]+1)+" 距离:%d"%self.dis
            self.ui.listWidget.addItem(str)
            self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)

            
    def swap2(self,tour):
        newTour = tour.copy()
        pos = r.sample(range(self.cityNum),2)
        newTour[pos[0]],newTour[pos[1]] = newTour[pos[1]],newTour[pos[0]]
        newDis = self.calDis(newTour)
        return newTour,newDis

    def oropt(self,tour):
        newTour = tour.copy()
        pos = r.sample(range(self.cityNum),3)
        pos.sort()
        tmp1 = newTour[pos[0]:pos[1]]
        tmp2 = newTour[pos[1]:pos[2]+1]
        newTour[pos[0]:pos[2]+1] = tmp2+tmp1
        newDis = self.calDis(newTour)
        return newTour,newDis

    def opt2(self,tour):
        newTour = tour.copy()
        pos = r.sample(range(len(self.X)),2)
        pos.sort()
        tmp1 = newTour[pos[0]:pos[1]+1]
        tmp1.reverse()
        newTour[pos[0]:pos[1]+1] = tmp1
        newDis = self.calDis(newTour)
        return newTour,newDis

    def combine(self,tour):
        newTour1,newDis1 = self.opt2(tour)
        newTour2,newDis2 = self.oropt(tour)
        newTour3,newDis3 = self.swap2(tour)

        if (newDis1 < newDis2):
            newDis = newDis1
            newTour = newTour1.copy()
        else:
            newDis = newDis2
            newTour = newTour2.copy()

        if (newDis > newDis3):
            newDis = newDis3
            newTour = newTour3.copy()
        return newTour,newDis


    def calDis(self,t):
        totalDis = 0
        for i in range(len(t) - 2):
            totalDis += self.distance[t[i]][t[i+1]]
        totalDis += self.distance[t[-1]][t[0]]
        return totalDis

    def sa(self,iterTimes = 200):
        #外循环
        if len(self.iterTimes) % iterTimes == 0: 
            self.curDis = self.dis
            self.curTour = self.tour.copy()
            if len(self.iterTimes) > 0:
                self.T = self.T*self.dropRate
        #内循环
        else:
            newTour,newDis = self.combine(self.curTour)
            
            if newDis < self.curDis:
                self.curDis = newDis
                self.curTour = newTour.copy()
                if newDis < self.dis:
                    self.dis = newDis
                    self.tour = newTour.copy()
            elif r.random() < math.exp((self.curDis-newDis)/self.T):
                self.curDis = newDis
                self.curTour = newTour.copy()

        str = "温度:%.2f"%(self.T)+" 距离:%d"%self.curDis
        self.ui.listWidget.addItem(str)
        self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
        
    

#直接调用新的ui.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    #import data
    #读取数据，city_list[1:-1]中存放所有city对象
    city_list=[0,]
    X = [0,]
    Y = [0,]
    
    file = open("gr202.tsp", "r")
    lines = file.readlines()
    for line in lines[7:len(lines)-1]:
        params = line.strip().split()
        X.append(float(params[1]))
        Y.append(float(params[2]))
        file.close()
        l = len(city_list)

    #TSP
    ex = TSP(X[1:],Y[1:])
    
    #ex = Ui_Form()
    #ex.setupUi(ex)
    ex.ui.show()
    sys.exit(app.exec_())
