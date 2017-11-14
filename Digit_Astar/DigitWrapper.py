from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from threading import Thread
from DigitUI import Ui_Form
import EightDigit
import NineDigit
import numpy as np
import cantor
import sys
from time import sleep
class EightDig():
    def __init__(self):
        #setupUi
        self.ui = Ui_Form()
        self.ui.setupUi(self.ui)

        self.ui.startButton.clicked.connect(self.on_start)
        self.ui.endButton.clicked.connect(self.on_end)


    def on_start(self):
        if self.ui.radioButton8.isChecked():
        
            s1 = EightDigit.SolveEight(1)
            t1 = Thread(target = s1.run,args = (self.setlineEdit,))
           

            s2 = EightDigit.SolveEight(2)
            t2 = Thread(target = s2.run,args = (self.setlineEdit2,))

            t1.start()
            t2.start()
            t1.join()
            t2.join()

        elif self.ui.radioButton9.isChecked():

            s1 = NineDigit.SolveNine(1)
            t1 = Thread(target = s1.run,args = (self.setlineEdit,))
           

            s2 = NineDigit.SolveNine(2)
            t2 = Thread(target = s2.run,args = (self.setlineEdit2,))

            t1.start()
            t2.start()
            t1.join()
            t2.join()

    def setlineEdit2(self,i,j,k,diglist):
        if not (i ==""):
            self.ui.lineEdit_4.setText(i)
            self.ui.lineEdit_5.setText(j)
            self.ui.lineEdit_6.setText(k)
            self.ui.lcdNumber_2_1.setProperty("intValue", diglist[1])
            self.ui.lcdNumber_2_2.setProperty("intValue", diglist[2])
            self.ui.lcdNumber_2_3.setProperty("intValue", diglist[3])
            self.ui.lcdNumber_2_4.setProperty("intValue", diglist[4])
            self.ui.lcdNumber_2_5.setProperty("intValue", diglist[5])
            self.ui.lcdNumber_2_6.setProperty("intValue", diglist[6])
            self.ui.lcdNumber_2_7.setProperty("intValue", diglist[7])
            self.ui.lcdNumber_2_8.setProperty("intValue", diglist[8])
            self.ui.lcdNumber_2_0.setProperty("intValue", diglist[0])
            


    def setlineEdit(self,i,j,k,diglist):
        if not (i ==""):
            self.ui.lineEdit.setText(i)
            self.ui.lineEdit_2.setText(j)
            self.ui.lineEdit_3.setText(k)
            self.ui.lcdNumber_1_1.setProperty("intValue", diglist[1])
            self.ui.lcdNumber_1_2.setProperty("intValue", diglist[2])
            self.ui.lcdNumber_1_3.setProperty("intValue", diglist[3])
            self.ui.lcdNumber_1_4.setProperty("intValue", diglist[4])
            self.ui.lcdNumber_1_5.setProperty("intValue", diglist[5])
            self.ui.lcdNumber_1_6.setProperty("intValue", diglist[6])
            self.ui.lcdNumber_1_7.setProperty("intValue", diglist[7])
            self.ui.lcdNumber_1_8.setProperty("intValue", diglist[8])
            self.ui.lcdNumber_1_0.setProperty("intValue", diglist[0])
            self.ui.repaint()
        else:
            self.ui.listWidget.addItem("最优路径")
            for p in diglist:
                #self.ui.listWidget.addItem("strrr")
                item1 = str(p.stateList[0:3])
                item2 = str(p.stateList[3:6])
                item3 = str(p.stateList[6:9])
                self.ui.listWidget.addItem(item1)
                self.ui.listWidget.addItem(item2)
                self.ui.listWidget.addItem(item3)
                self.ui.listWidget.addItem(" ")
                #print("123")
                self.ui.listWidget.setCurrentRow(self.ui.listWidget.count()-1)
                self.ui.repaint()
                #print("456")
    def on_end(self):
        sleep(9999999)
        '''
        for i in range(5):
            self.ui.listWidget.addItem(str([1,2,3]))
            self.ui.listWidget.addItem("str")
        #self.ui.repaint()
        print("onend")
        '''
        pass
        

#直接调用新的ui.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EightDig()
    ex.ui.show()
    sys.exit(app.exec_())
