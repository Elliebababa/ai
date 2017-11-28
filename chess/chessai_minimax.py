import chessBoard
import random
import sys
import chessBoard
from time import sleep
chessSize = 56
chessAreaX =[0,0, 57, 115, 173, 231, 288, 346, 404, 462]
chessAreaY =[0,0, 57, 115, 172, 230, 290, 348, 405, 463, 520]
chessList = ['BA','BB','BC','BK','BN','BP','BR','RA','RB','RC','RK','RN','RP','RR']
bChess = {0:[14,16],1:[13,17],2:[32,38],3:[15],4:[12,18],5:[41,43,45,47,49],6:[11,19]}
rChess = {7:[104,106],8:[103,107],9:[82,88],10:[105],11:[102,108],12:[71,73,75,77,79],13:[101,109]}
basicvalue =[250,250,350,10000,350,100,500]
flexvalue =[1,1,6,0,12,15,6]
blackPlayer = 1
redPlayer = -1


class vBoard():
    def __init__(self,board):
        self.focus = -1
        self.player = redPlayer
        self.bChess={i:[] for i in range(7)}
        self.rChess={i+7:[] for i in range(7)}
        #摆放棋子
        self.board = {(i+1)*10 + j+1 : -1 for i in range (10) for j in range(9)}
        for i in board:
            if not board[i] == -1:
                self.board[i] = board[i] 
                if board[i] <= 6:
                    self.bChess[board[i]].append(i)
                else:
                    self.rChess[board[i]].append(i)
        self.rv = 0
        self.bv = 0

    def legalMove(self,ori,des):
        chessType = self.board[ori] % 7
        if self.board[ori] // 7 == 0:
            chesscolor = blackPlayer
        else:
            chesscolor = redPlayer
        legal = False
        oriX = ori%10
        oriY = ori//10
        desX = des%10
        desY = des//10
        #棋盘范围
        if not (desX in range(1,10) and desY in range(1,11)):
            return False
        #没有移动
        if oriX == desX and oriY == desY:
            return False

        #判断区域是否可下
        #不能有自己的棋子
        if chesscolor == blackPlayer:#黑方
            if self.board[des] in range(0,7):
                return False
        if chesscolor == redPlayer:#红方
            if self.board[des] in range(7,14):
                return False

        #按规则行走
        if chessType == 0:#士 仅能在米字格内行走米字
            if abs(desX - 5) <=1 and (abs(desY - 2)<= 1 or abs(desY - 9)<= 1) :
                if abs(desX - oriX)+abs(desY - oriY) == 1:
                    legal = True
                if (oriX+oriY) % 2 == (chesscolor + 1)//2:
                    if abs(desX - oriX) == 1 and abs(desY - oriY) == 1:
                        legal = True
                  
        elif chessType == 1:#象 仅能在河内走田字 田字中间不能隔着棋子
            if (chesscolor == blackPlayer and desY <= 5) or (chesscolor == redPlayer and desY >= 6):
                if abs(desX - oriX) == 2  and abs(desY - oriY) == 2:
                    if self.board[(desX + oriX)/2+(desY + oriY)/2*10] == -1:
                        legal = True

        elif chessType == 2:#炮 不吃棋子可以直走 直走中间不能隔着棋子 吃棋子要隔着一只棋子
            if (desX == oriX):
                count = -1
                if desY < oriY:
                    sPos,ePos = desY,oriY
                else:
                    ePos,sPos = desY,oriY
                for i in range(sPos,ePos+1):
                    if self.board[desX+i*10] != -1:
                        count+=1
            elif (desY == oriY) :
                count = -1
                if desX < oriX:
                    sPos,ePos = desX,oriX
                else:
                    ePos,sPos = desX,oriX
                for i in range(sPos,ePos+1):
                    if self.board[desY*10+i] != -1:
                        count+=1
                    else:
                        break
            if (self.board[des] != -1 and count == 2) or (self.board[des] == -1 and count == 0):
                legal = True
                            

        elif chessType == 3:#将 仅能在米字格内行走直线
            if abs(desX - 5) <=1 and (abs(desY - 2)<= 1 or abs(desY - 9)<= 1) :
                if abs(desX - oriX)+abs(desY - oriY) == 1:
                    legal = True
            if (chesscolor == blackPlayer and desX == self.rChess[10][0]%10) or (chesscolor == redPlayer and desX == self.bChess[3][0]%10):
                count = 0
                for i in range(self.bChess[3][0]//10+1,self.rChess[10][0]//10):
                    if not self.board[i*10+desX] == -1:
                        count +=1
                if count == 0:
                    legal = False  



                    

        elif chessType == 4:#马 走日字 不能绊马脚
            if abs(desX - oriX) > 0 and abs(desY - oriY) > 0 and abs(desX - oriX)+abs(desY - oriY) == 3:
                if abs(desY - oriY) ==2:
                    if self.board[oriX+(desY + oriY)/2*10] == -1:
                        legal = True
                else:
                    if self.board[oriY*10+(desX + oriX)/2] == -1:
                        legal = True            

                    
        elif chessType == 5:#卒 过河前直走 过河后任意走 不能后退

            if (chesscolor == blackPlayer and desY <= 5) or (chesscolor == redPlayer and desY >= 6):
                over = False
            else:
                over = True

            if abs(desX - oriX)+abs(desY - oriY) == 1:
                legal = True

            if not over and not (desX == oriX):#未过河不能打横走
                legal = False

            if (chesscolor == blackPlayer and desY < oriY) or (chesscolor == redPlayer and desY > oriY):#不能后退
                legal = False

            
                    

        elif chessType == 6:#车 直走 中间不能隔着棋子
            if (desX == oriX):
                count = 0
                if desY < oriY:
                    sPos,ePos = desY,oriY
                else:
                    ePos,sPos = desY,oriY
                            
                for i in range(sPos+1,ePos):
                    if self.board[desX+i*10] != -1:
                        count+=1
            elif (desY == oriY) :
                count = 0
                if desX < oriX:
                    sPos,ePos = desX,oriX
                else:
                    ePos,sPos = desX,oriX
                for i in range(sPos+1,ePos):
                    if self.board[desY*10+i] != -1:
                        count+=1
            if (count == 0):
                legal = True  
            else:
                legal = False

            if not (desX == oriX or desY == oriY):
                legal = False          
        
        #将帅不能照面
        if (not chessType == 3 and self.rChess[10][0]%10== self.bChess[3][0]%10 == oriX and not desX == oriX):
            count = 0
            for i in range(self.bChess[3][0]//10+1,self.rChess[10][0]//10):
                if not self.board[i*10+oriX] == -1:
                    count +=1
            if count == 1:
                legal = False

        return legal
                    
    def move(self,ori,des):
        if self.board[ori] // 7 == 0:
            chesscolor = blackPlayer
        else:
            chesscolor = redPlayer
        if not self.board[des] == -1:#对手棋子被吃掉
            if chesscolor == redPlayer:
                self.bChess[self.board[des]].remove(des)
            else:
                self.rChess[self.board[des]].remove(des)
        if chesscolor == redPlayer:
            #时print(ori,des,self.board,self.board[ori])
            c = self.board[ori]
            i = self.rChess[c].index(ori)
            self.rChess[c][i] = des
        else:
            c = self.board[ori]
            i = self.bChess[c].index(ori)
            self.bChess[c][i] = des
        self.board[des] = self.board[ori]
        self.board[ori] = -1
        self.player = -self.player #成功移动交换玩家
                    

class chessai():
    def __init__(self,board,Maxdepth):
        self.board = vBoard(board)
        self.Maxdepth = Maxdepth

    def generateMove(self,callback):
        res = self.minmax(-1,0,-sys.maxsize,sys.maxsize)
        (ori,des) = res[1]
        X = (des%10-0.5)*chessSize
        Y = (des//10-0.5)*chessSize
        sleep(2)
        callback(ori,X,Y)

    def minmax(self,player,depth,alpha,beta):
       
        #结束状态
        if not len(self.board.rChess[10]):
            self.board.end = True
            return [sys.maxsize-1,(0,0)]
        elif not len(self.board.bChess[3]):
            self.board.end = True
            return [-sys.maxsize+1,(0,0)]

        #限制搜索深度
        if depth >= self.Maxdepth:
            return [self.evaluate(self.board),(0,0)]
        else:
            #生成可行的顶点
            mov =[]
            self.getMovs(player,mov)
            random.shuffle(mov)
        bestMov = ()
        #min方，电脑
        if player == redPlayer:
            for (ori,des) in mov:
                tmp = self.board.board[des]   

                #print('depth',depth,'move to call',ori,des)                 
                self.board.move(ori,des)
                b = self.minmax(-player,depth+1,alpha,beta)
                if b[0] <beta:
                    beta = b[0]
                    bestMov =(ori,des)
                #    print('bestMov',bestMov,(ori,des))
                #undoMove(i)

                #print('depth',depth,'undo to call',ori,des)
                self.board.move(des,ori)
                if not tmp == -1:
                    self.board.bChess[tmp].append(des)
                    self.board.board[des] = tmp
                #剪枝
                if beta < alpha:
                    break

            return [beta,bestMov]

        #max方，人
        else:
            for (ori,des) in mov:
                tmp = self.board.board[des]
                #print('depth',depth,'move to call',ori,des)
                self.board.move(ori,des)



                a = self.minmax(-player,depth+1,alpha,beta)
                if a[0] >= alpha:
                    alpha = a[0]
                    bestMov = (ori,des)                
                #undoMove(i)
                #print('human depth',depth,'undo to call',ori,des)
                self.board.move(des,ori)
                if not tmp == -1:
                    self.board.rChess[tmp].append(des)
                    self.board.board[des] = tmp

                if alpha > beta:
                    break
                    
            return [alpha,bestMov]

    def getMovs(self,player,mov):
        b = self.board
        alivechess = []
        if b.player == redPlayer:
            for i in b.rChess.keys():
                if len(b.rChess[i]):
                    for pos in b.rChess[i]:
                        alivechess.append(pos)
        else:
            for i in b.bChess.keys():
                if len(b.bChess[i]):
                    for pos in b.bChess[i]:
                        alivechess.append(pos)
        board = b.board
        for pos in alivechess:
            i = board[pos]
            chessType = i % 7
            if i // 7 == 0:
                chesscolor = blackPlayer
            else:
                chesscolor = redPlayer

            #按规则行走
            if chessType == 0:#士 仅能在米字格内行走米字
                dir_ = [-11,-10,-9,-1,+1,+9,10,11]
                for d in dir_:
                    des = pos+d
                    if b.legalMove(pos,des):
                        mov.append((pos,des))
                      
            elif chessType == 1:#象 仅能在河内走田字 田字中间不能隔着棋子
                dir_ = [-22,-18,18,22]
                for d in dir_:
                    des = pos+d
                    if b.legalMove(pos,des):
                        mov.append((pos,des))

            elif chessType == 2 or chessType == 6:#炮 c车
                for d in range(9):
                    des = pos//10*10+d+1
                    if b.legalMove(pos,des):
                        mov.append((pos,des))
                for d in range(10):
                    des = pos%10+(d+1)*10
                    if b.legalMove(pos,des):
                        mov.append((pos,des))
                                

            elif chessType == 3:#将 仅能在米字格内行走直线
                dir_ = [-10,-1,+1,+10]
                for d in dir_:
                    des = pos+d
                    if b.legalMove(pos,des):
                        mov.append((pos,des))
                        

            elif chessType == 4:#马 走日字 不能绊马脚
                dir_ = [-12,-21,-19,-8,12,21,19,8]
                for d in dir_:
                    des = pos+d
                    if b.legalMove(pos,des):
                        mov.append((pos,des))
                        
            elif chessType == 5:#卒 过河前直走 过河后任意走 不能后退
                dir_ = [-10,-1,+1,+10]
                for d in dir_:
                    des = pos+d
                    if b.legalMove(pos,des):
                        mov.append((pos,des))

    def evaluate(self,b):
        bv = 0
        rv = 0
        for i in range(7):
            bv += basicvalue[i]*len(b.bChess[i])
            rv += basicvalue[i]*len(b.rChess[i+7])
        return bv-rv
