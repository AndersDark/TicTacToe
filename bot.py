from game import *

def botPlay():
    if not isGamePlaying():
        return
    for x, row in enumerate(mainGameBoard):
        for y, field in enumerate(row):
            if field == EMPTY:
                clickOnField(x,y)
                return

def boardCopy():
    simpleBoard = []
    for row in mainGameBoard:
        simpleBoard.append(row)
    
    print(simpleBoard)

    return simpleBoard

def getNumberOfEmptyCells(board):
    count = 0
    for row in board:
        for field in row:
            if field == EMPTY:
                count += 1
    return count

def getBoardPoint(board, maxPlayer):
    if checkDraw(board):
        return 0
    elif checkWin(board) == maxPlayer:
        return 1
    elif checkWin(board) != maxPlayer:
        return -1
    else:
        return 0
        
    



def minimax(board, maxTurn, score, maxPlayer):
    # base case
    if (getBoardPoint(board, maxPlayer) != 0 or getNumberOfEmptyCells(board) == 0):
        return getBoardPoint(board, maxPlayer)
    
    if maxTurn:
        pass
