from graphics import *

# The board will include objects of the Field class
board = [[None,None,None],
         [None,None,None],
         [None,None,None]]

currentPlayer = "X" #Cycles between X and O, X starts

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