import matplotlib
matplotlib.use('Qt5Agg')  
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  



class TSPCanvas(FigureCanvas):
    def __init__(self, parent= None, width = 10, height= 8,dpi = 100):
        self.fig = Figure(figsize = (width,height),dpi = dpi)
        #self.plt = self.fig.add_subplot(111)
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        #self.plt.axis('off')
        #self.ax = self.fig.add_subplot(111)#将画板划分为1行1列在第1个位置添加子图        
        #self.plotTour(X,Y,'b-')  
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)
        
       # FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets,QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)
        #self.plt.clear()
    def plotTour(self,x,y,dtype):
        self.ax.clear()
        self.ax.plot(x,y,dtype)
        self.ax.axis('off')
        print('dd')
