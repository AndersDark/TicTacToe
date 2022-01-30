

import tkinter as tk

TOP_BAR = 50
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH + TOP_BAR
LINE_THICKNES = 5
BOX_SIZE = (SCREEN_WIDTH-2*LINE_THICKNES)//3

root = tk.Tk();


# y\x 0 1 2
#   0 _|_|_
#   1 _|_|_ 
#   2  | | 


class Field:
    def __init__(self,x,y):
        self.button = tk.Button(root,bg="white",border=False,activebackground="white",command=root.destroy)
        self.button.place(height=BOX_SIZE,width=BOX_SIZE,x=x*BOX_SIZE+x*LINE_THICKNES,y=TOP_BAR+y*BOX_SIZE+y*LINE_THICKNES)

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

    for x in range(3):
        for y in range(3):
            Field(x,y)
