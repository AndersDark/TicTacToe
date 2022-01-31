from graphics import *
from bot import *
from game import *


def main():
    screenSetup()
    while(True):
        root.update()
        
        if (whoTurn() == 'O' and isGamePlaying()):
            botPlay()

    
if __name__ == "__main__":
    main()  