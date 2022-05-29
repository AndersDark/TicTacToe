from window import *
from bot import *
from game import *

BOT_PLAYER = CIRCLE

def main():
    screenSetup()
    while(True):
        root.update()
        screenUpdate(mainGameBoard)
        checkGameState(mainGameBoard)
        if(whoTurn() == BOT_PLAYER):
            botPlay()

    
if __name__ == "__main__":
    main()  