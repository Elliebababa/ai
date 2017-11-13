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
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)
