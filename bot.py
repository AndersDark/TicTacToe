from game import *

def botPlay():
    print("Bot: ")
    for row in board:
        for field in row:
            if field.contain == 'e':
                click(field)
                return