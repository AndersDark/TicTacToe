from graphics import *

# The board will include objects of the Field class
board = [[None,None,None],
         [None,None,None],
         [None,None,None]]

currentPlayer = "X" #Cycles between X and O, X starts

def checkWin():
    # Horisontal check
    for row in board:
        if (row[0].contain == row[1].contain == row[2].contain != 'e'):
            return True
    
    # Vertical check
    for i in range(len(board)):
        if (board[0][i].contain == board[1][i].contain == board[2][i].contain != 'e'):
            return True

    # Diagonal check
    if (board[0][0].contain == board[1][1].contain == board[2][2].contain != 'e'):
        return True
    
    if (board[0][2].contain == board[1][1].contain == board[2][0].contain != 'e'):
        return True

    return False    


def checkDraw():
    for row in board:
        for field in row:
            if field.contain == 'e': #empty field
                return False
    return True

def disablePlay():
    for row in board:
        for field in row:
            if field.contain == 'e': #empty field
                field.disable()

def click(field):
    # A board field can contain "e" (empty), "X" or "O"
    if field.contain == "e":
        global currentPlayer
        field.contain = currentPlayer

        if currentPlayer == "X":
            field.drawCross()
            currentPlayer = "O"

        else:
            field.drawCircle()
            currentPlayer = "X"

    ### For debug
    for row in board:
        for elem in row:
            print(elem.contain,end=" ")
        print()
    
    print("-------------")
    ###

    if checkWin():
        disablePlay()
        print(f"{field.contain} won!")

    elif checkDraw(): #Board is full and no winner
        print("It's a draw")
