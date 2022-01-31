from graphics import *
from bot import *
from game import *

BOT_PLAYER = CROSS

def main():
    screenSetup()
    while(True):
        root.update()
        
        if (whoTurn() == BOT_PLAYER and isGamePlaying()):
            botPlay()

    
if __name__ == "__main__":
    main()  