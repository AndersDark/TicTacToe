from window import *

CROSS = 'X'
CIRCLE = 'O'
EMPTY = 'e'

# The board will represent the game state
mainGameBoard = [[EMPTY,EMPTY,EMPTY],
                [EMPTY,EMPTY,EMPTY],
                [EMPTY,EMPTY,EMPTY]]

currentPlayer = CROSS #Cycles between X and O, X starts.

gamePlaying = True

def whoTurn():
    return currentPlayer

def isGamePlaying():
    return gamePlaying

def checkWin(board):
    # Horisontal check
    for row in board:
        if (row[0] == row[1] == row[2] != EMPTY):
            return row[0]
    
    # Vertical check
    for i in range(len(board)):
        if (board[0][i] == board[1][i] == board[2][i] != EMPTY):
            return board[0][i]

    # Diagonal check
    if (board[0][0] == board[1][1] == board[2][2] != EMPTY):
        return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[0][2]

    return EMPTY


def checkDraw(board):
    return not any(EMPTY in row for row in board)

# y\x 0 1 2
#   0 _|_|_
#   1 _|_|_ 
#   2  | | 
def clickOnField(x,y):
    print("click")
    if mainGameBoard[x][y] != EMPTY:    
        return
    
    if isGamePlaying():
        global currentPlayer
        mainGameBoard[x][y] = currentPlayer
        currentPlayer = CROSS if (currentPlayer == CIRCLE) else CIRCLE

def checkGameState(board):
    if not isGamePlaying():
        return

    global gamePlaying
    winner = checkWin(board)
    if winner != EMPTY:
        gamePlaying = False
        print(f"{winner} won!")
    
    elif checkDraw(board):
        gamePlaying = False
        print("It's a draw!")

def resetGame():
    global gamePlaying
    global currentPlayer

    for x in range(len(mainGameBoard)):
        for y in range(len(mainGameBoard[x])):
            mainGameBoard[x][y] = EMPTY

    gamePlaying = True
    currentPlayer = CROSS