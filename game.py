from graphics import *

CROSS = 'X'
CIRCLE = 'O'
EMPTY = 'e'

# The board will include objects of the Field class
board = [[None,None,None],
         [None,None,None],
         [None,None,None]]

currentPlayer = CROSS #Cycles between X and O, X starts.

gamePlaying = True


def whoTurn():
    return currentPlayer

def isGamePlaying():
    return gamePlaying

def checkWin():
    # Horisontal check
    for row in board:
        if (row[0].contain == row[1].contain == row[2].contain != EMPTY):
            return True
    
    # Vertical check
    for i in range(len(board)):
        if (board[0][i].contain == board[1][i].contain == board[2][i].contain != EMPTY):
            return True

    # Diagonal check
    if (board[0][0].contain == board[1][1].contain == board[2][2].contain != EMPTY):
        return True
    
    if (board[0][2].contain == board[1][1].contain == board[2][0].contain != EMPTY):
        return True

    return False    


def checkDraw():
    for row in board:
        for field in row:
            if field.contain == EMPTY:
                return False
    return True


def disablePlay():
    for row in board:
        for field in row:
            if field.contain == EMPTY:
                field.disable()


def click(field):
    # A board field can contain EMPTY, CROSS or CIRCLE
    if field.contain == EMPTY:
        global currentPlayer
        field.contain = currentPlayer

        if currentPlayer == CROSS:
            field.drawCross()
            currentPlayer = CIRCLE

        else:
            field.drawCircle()
            currentPlayer = CROSS

    ### For debug
    for row in board:
        for elem in row:
            print(elem.contain,end=" ")
        print()
    
    print("-------------")
    ###

    global gamePlaying

    if checkWin():
            gamePlaying = False
            disablePlay()
            print(f"{field.contain} won!")

    elif checkDraw(): #Board is full and no winner
        gamePlaying = False
        print("It's a draw")

def resetGame():
    global gamePlaying
    global currentPlayer

    for row in board:
        for field in row:
            field.reset()

    gamePlaying = True
    currentPlayer = CROSS

    #DEBUG
    print("###############")
    print("-----RESET-----")
    print("###############")
