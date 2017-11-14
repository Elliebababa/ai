import queue
import numpy
import sys
import time
import cantor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from time import sleep

dis=  [[0,1,2,1,2,3,2,3,4],
                   [1,0,1,2,1,2,3,2,3],
                   [2,1,0,3,2,1,4,3,2],
                   [1,2,3,0,1,2,1,2,3],
                   [2,1,2,1,0,1,2,1,2],
                   [3,2,1,2,1,0,3,2,1],
                   [2,3,4,1,2,3,0,1,2],
                   [3,2,3,2,1,2,1,0,1],
                   [4,3,2,3,2,1,2,1,0]]

move = [[1,3],
        [0,2,4],
        [1,5],
        [0,4,6],
        [1,3,5,7],
        [2,4,8],
        [3,7],
        [4,6,8],
        [5,7]]


#2 1 4 3 6 5 7 8 0
#4 3 1 2 5 6 7 8 0
#5 6 7 8 0 2 1 3 4 约2s
class EightFigure():
    def __init__(self,stateList,lastList,finalState,h,depth = 999999):
        self.depth = depth
        if h == 1:
            self.value = self.evaluate(stateList,finalState)
        else:
            self.value = self.evaluate2(stateList,finalState)
        self.stateList = stateList.copy()
        self.lastList = lastList.copy()
        self.pos = cantor.cantor_encode(9,stateList)

    def __lt__(self,other):#相同的值则先生成的优先
        return self.value < other.value

    def __eq__(self,other):
        return self.stateList == other.stateList
        
    def evaluate(self,stateList,finalState):
        value = 0
        for i in range(9):
            finalPos = finalState.index(stateList[i])
            #curPos = i
            value += dis[i][finalPos]
        if value == 0:
            return 0
        else:
            return value+self.depth

    def evaluate2(self,stateList,finalState):
        value = 0
        for i in range(9):
            if not (stateList[i] ==finalState[i]):
                value +=1
        if value == 0:
            return 0
        else:
            return value+self.depth

class SolveNine():
    def __init__(self,h):
 #       self.initState = [8,2,4,6,1,3,7,5,0]
        self.initState = [5,6,7,8,0,2,1,3,4]
        self.finalState = [1,2,3,8,0,4,7,6,5]
        self.closeList = {}
        self.openList = {}
        self.h = h
    def printPath(self,last):
        path = []
        path.append(last)
        curDepth = last.depth
        while (curDepth > 0):
            i = cantor.cantor_encode(9,last.lastList)
            last = self.closeList[i]
            path.append(last)
            curDepth = self.closeList[i].depth
        path = path[::-1]
        return path
        #for p in path:
        #    print(numpy.array(p.stateList).reshape(3,3),'\n')
        
            
    def run(self,callback):
        h = self.h
        p0 = 0
        pt = 0
        
        #有解
        #strTime = time.time()
        s0 = EightFigure(self.initState,[],self.finalState,h = h,depth = 0)
        st = EightFigure(self.finalState,[],self.finalState,h = h)
        openQue = queue.PriorityQueue()
        openQue.put(s0)
        self.openList[cantor.cantor_encode(9,self.initState)] = s0

        while (len(self.openList)):
            #由于优先级队列没有删除重复元素 所以需要挑出没有检查过的结点
            top = openQue.get()
            while top.pos in self.closeList:
                top = openQue.get()
            
            self.openList.pop(top.pos)
            self.closeList[top.pos] = top

            str1 = str(len(self.openList))
            str2 = str(len(self.openList)+len(self.closeList))
            str3 = str(top.value)
            diglist = top.stateList.copy()
            callback(str1,str2,str3,diglist)

            if top.value == 0:#结束
                #print(top.depth)
                path = self.printPath(top).copy()
                callback("","","",path)
                return
            
            for i in range(9):
                pos = top.stateList.index(i)
                for nextPos in move[pos]:
                    newState = top.stateList.copy()
                    newState[pos],newState[nextPos] = newState[nextPos],newState[pos]
                    newpos = cantor.cantor_encode(9,newState)
                    if newpos not in self.closeList:
                        new = EightFigure(newState,top.stateList,self.finalState,h = h,depth = top.depth+1)
                        openQue.put(new)
                        if newpos not in self.openList:
                            self.openList[newpos] = new
                            
                    else:
                        i = cantor.cantor_encode(9,top.stateList)
                        if self.closeList[i].depth >  top.depth+1:
                            self.closeList[i].depth = top.depth+1
                            self.closeList[i].lastList = top.stateList.copy()
            
        #print(time.time()-strTime)

