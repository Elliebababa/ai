import chessBoard
import random
chessSize = 56
blackplayer = 1
redplayer = -1
def generateMove(board):
    alivechess = []
    if board.player == redplayer:
        for i in board.rChess.keys():
                if len(board.rChess[i]):
                        alivechess.append(i)
        chess = random.choice(alivechess)
        point = board.rChess[chess][0]
        y =(point//10-1.5)*chessSize
    else:
        for i in board.bChess.keys():
                if len(board.bChess[i]):
                        alivechess.append(i)
        chess = random.choice(alivechess)
        point = board.bChess[chess][0]
        y =(point//10+0.5)*chessSize
    x = (point%10-0.5)*chessSize
    #print(point,x,y)
    return [point,x,y]
