from game import *

def botPlay():
    print("Bot: ")
    for row in board:
        for field in row:
            if field.contain == EMPTY:
                click(field)
                return