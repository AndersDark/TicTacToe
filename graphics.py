
from game import *
import tkinter as tk
from PIL import Image, ImageTk

TOP_BAR = 50
SCREEN_WIDTH = 610
SCREEN_HEIGHT = SCREEN_WIDTH + TOP_BAR
LINE_THICKNES = 5
BOX_SIZE = (SCREEN_WIDTH-2*LINE_THICKNES)//3

root = tk.Tk();


# y\x 0 1 2
#   0 _|_|_
#   1 _|_|_ 
#   2  | | 


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_px = x*BOX_SIZE+x*LINE_THICKNES
        self.y_px = TOP_BAR+y*BOX_SIZE+y*LINE_THICKNES

        self.button = tk.Button(root,bg="white",border=False,activebackground="white",command= lambda: click(self))
        self.button.place(height=BOX_SIZE,width=BOX_SIZE,x=self.x_px,y=self.y_px)

        self.contain = "e" # could be "X", "O" or "empty"

        self.crossLabel, self.circleLabel = imageLoad()


    def drawCross(self):
        self.crossLabel.place(x=self.x_px, y=self.y_px)

    def drawCircle(self):
        self.circleLabel.place(x=self.x_px, y=self.y_px)

    def disable(self):
        self.button.config(command= lambda : None)

        ### Debug
        print(f"button {self.x}, {self.y} is disabled")


def screenSetup():
    root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
    root.resizable(False,False)
    
    canvas = tk.Canvas(root,width=SCREEN_WIDTH,height=SCREEN_HEIGHT,bg="white")
    canvas.pack()

    # Lines to make the board
    canvas.create_rectangle(BOX_SIZE,TOP_BAR,BOX_SIZE+LINE_THICKNES,SCREEN_HEIGHT,fill='black')
    canvas.create_rectangle(2*BOX_SIZE+LINE_THICKNES,TOP_BAR,2*BOX_SIZE+2*LINE_THICKNES,SCREEN_HEIGHT,fill='black')
    canvas.create_rectangle(0,TOP_BAR+BOX_SIZE,SCREEN_WIDTH,TOP_BAR+BOX_SIZE+LINE_THICKNES,fill='black')
    canvas.create_rectangle(0,TOP_BAR+2*BOX_SIZE+LINE_THICKNES,SCREEN_WIDTH,TOP_BAR+2*BOX_SIZE+2*LINE_THICKNES,fill='black')

    for y in range(3):
        for x in range(3):
            board[y][x] = Field(x,y)

def imageLoad():
    crossImage = ImageTk.PhotoImage(Image.open("./assets/cross.png"))
    crossLabel = tk.Label(image=crossImage,bg="white",border=False)
    crossLabel.image = crossImage

    circleImage = ImageTk.PhotoImage(Image.open("./assets/circle.png"))
    circleLabel = tk.Label(image=circleImage,bg="white",border=False)
    circleLabel.image = circleImage

    return crossLabel, circleLabel