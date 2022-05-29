
from game import *
import tkinter as tk
from PIL import Image, ImageTk

TOP_BAR = 100
SCREEN_WIDTH = 610
SCREEN_HEIGHT = SCREEN_WIDTH + TOP_BAR
LINE_THICKNES = 5
BOX_SIZE = (SCREEN_WIDTH-2*LINE_THICKNES)//3

root = tk.Tk();

buttons = [[None,None,None],
           [None,None,None],
           [None,None,None]]

# y\x 0 1 2
#   0 _|_|_
#   1 _|_|_ 
#   2  | | 

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


    resetButton = tk.Button(root,bg="blue",border=False,activebackground="blue", fg="white", text="RESET", command=resetGame)
    resetButton.place(height=TOP_BAR*3//4, width=SCREEN_WIDTH//6, x=SCREEN_WIDTH*2/3, y=TOP_BAR//8)

    for y in range(3):
        for x in range(3):
            buttons[x][y] = Button(x,y)

def screenUpdate(board):
    for (row, buttonRow) in zip(board, buttons):
        for field, button in zip(row, buttonRow):
            if(field == CROSS and button.isEmpty):
                button.drawCross()
            
            elif(field == CIRCLE and button.isEmpty):
                button.drawCircle()

            elif(field == EMPTY and not button.isEmpty):
                button.reset()

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_px = x*BOX_SIZE+x*LINE_THICKNES
        self.y_px = TOP_BAR+y*BOX_SIZE+y*LINE_THICKNES

        self.button = tk.Button(root,bg="white",border=False,activebackground="white",command= lambda: clickOnField(self.x,self.y))
        self.button.place(height=BOX_SIZE,width=BOX_SIZE,x=self.x_px,y=self.y_px)

        self.crossLabel, self.circleLabel = imageLoad()

        self.isEmpty = True


    def drawCross(self):
        self.crossLabel.place(x=self.x_px, y=self.y_px)
        self.isEmpty = False

    def drawCircle(self):
        self.circleLabel.place(x=self.x_px, y=self.y_px)
        self.isEmpty = False

    def reset(self):
        self.crossLabel.place_forget()
        self.circleLabel.place_forget()
        self.isEmpty = True

def imageLoad():
    crossImage = ImageTk.PhotoImage(Image.open("./assets/cross.png"))
    crossLabel = tk.Label(image=crossImage,bg="white",border=False)
    crossLabel.image = crossImage

    circleImage = ImageTk.PhotoImage(Image.open("./assets/circle.png"))
    circleLabel = tk.Label(image=circleImage,bg="white",border=False)
    circleLabel.image = circleImage

    return crossLabel, circleLabel