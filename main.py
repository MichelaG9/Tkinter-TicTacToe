from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD

class Mywindow(Tk):
    def __init__(self):
        super(Mywindow, self).__init__()

        self.title("Tic Tac Toe")
        self.w = 400 # width for the Tk self
        self.h = 400 # height for the Tk self

        # get screen width and height
        self.ws = self.winfo_screenwidth() 
        self.hs = self.winfo_screenheight() 

        # calculate x and y coordinates for the Tk self window
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)

        # set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        self.current = ""
        self.playerX = []
        self.playerO = []
        self.label = {}
        self.combinations = [[1,2,3],[1,5,9],[1,4,7],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]

        self.startingFrame()

    def startingFrame(self):
        self.container = Frame(self)
        self.container.pack(side=TOP, fill= "both", expand=True)

        self.label1 = ttk.Label(self.container, text="Tic Tac Toe", font="Poppins, 30")
        self.label1.place(anchor= CENTER, x=200, y=100)
        self.label1 = ttk.Label(self.container, text="X is the first playing", font="Poppins")
        self.label1.place(anchor= CENTER, x=200, y=150)
        self.button = ttk.Button(self.container, text="Press to start", command= self.change, padding=10)
        self.button.place(anchor= CENTER, x=200, y=200)

    def endingFrame(self, winner):
        self.container2.destroy()
        self.current = ""
        self.playerX = []
        self.playerO = []
        self.label = {}

        self.container = Frame(self)
        self.container.pack(side=TOP, fill= "both", expand=True)

        self.label1 = ttk.Label(self.container, text=f"{winner} is the winner", font="Poppins, 30")
        self.label1.place(anchor= CENTER, x=200, y=100)
        self.button = ttk.Button(self.container, text="Restart", command= self.change)
        self.button.place(anchor= CENTER, x=200, y=200)

    def secondFrame(self):
        self.container2 = Frame(self)
        self.container2.pack(side=TOP, fill="both", expand=True)
        self.box = {}

        for i in range(3):
            self.container2.columnconfigure(i, weight=1, minsize=100)
            self.container2.rowconfigure(i, weight=1, minsize=100)

        self.box[1] = Frame(self.container2, bg="yellow")
        self.box[1].grid(row=0, column=0, sticky="nsew")
        self.box[1].columnconfigure(0, weight=1, minsize=100)
        self.box[1].rowconfigure(0, weight=1, minsize=100)
        self.button1 = tk.Button(self.box[1], command= lambda: self.target(1))
        self.button1.grid(row=0, column=0, sticky="nsew")

        self.box[2] = Frame(self.container2)
        self.box[2].grid(row=0, column=1, sticky="nsew")
        self.box[2].columnconfigure(0, weight=1, minsize=100)
        self.box[2].rowconfigure(0, weight=1, minsize=100)
        self.button2 = tk.Button(self.box[2], command= lambda: self.target(2))
        self.button2.grid(row=0, column=0, sticky="nsew")

        self.box[3] = Frame(self.container2)
        self.box[3].grid(row=0, column=2, sticky="nsew")
        self.box[3].columnconfigure(0, weight=1, minsize=100)
        self.box[3].rowconfigure(0, weight=1, minsize=100)
        self.button3 = tk.Button(self.box[3], command= lambda: self.target(3))
        self.button3.grid(row=0, column=0, sticky="nsew")

        self.box[4] = Frame(self.container2)
        self.box[4].grid(row=1, column=0, sticky="nsew")
        self.box[4].columnconfigure(0, weight=1, minsize=100)
        self.box[4].rowconfigure(0, weight=1, minsize=100)
        self.button4 = tk.Button(self.box[4], command= lambda: self.target(4))
        self.button4.grid(row=0, column=0, sticky="nsew")

        self.box[5] = Frame(self.container2)
        self.box[5].grid(row=1, column=1, sticky="nsew")
        self.box[5].columnconfigure(0, weight=1, minsize=100)
        self.box[5].rowconfigure(0, weight=1, minsize=100)
        self.button5 = tk.Button(self.box[5], command= lambda: self.target(5))
        self.button5.grid(row=0, column=0, sticky="nsew")

        self.box[6] = Frame(self.container2)
        self.box[6].grid(row=1, column=2, sticky="nsew")
        self.box[6].columnconfigure(0, weight=1, minsize=100)
        self.box[6].rowconfigure(0, weight=1, minsize=100)
        self.button6 = tk.Button(self.box[6], command= lambda: self.target(6))
        self.button6.grid(row=0, column=0, sticky="nsew")

        self.box[7] = Frame(self.container2)
        self.box[7].grid(row=2, column=0, sticky="nsew")
        self.box[7].columnconfigure(0, weight=1, minsize=100)
        self.box[7].rowconfigure(0, weight=1, minsize=100)
        self.button7 = tk.Button(self.box[7], command= lambda: self.target(7))
        self.button7.grid(row=0, column=0, sticky="nsew")

        self.box[8] = Frame(self.container2)
        self.box[8].grid(row=2, column=1, sticky="nsew")
        self.box[8].columnconfigure(0, weight=1, minsize=100)
        self.box[8].rowconfigure(0, weight=1, minsize=100)
        self.button8 = tk.Button(self.box[8], command= lambda: self.target(8))
        self.button8.grid(row=0, column=0, sticky="nsew")

        self.box[9] = Frame(self.container2)
        self.box[9].grid(row=2, column=2, sticky="nsew")
        self.box[9].columnconfigure(0, weight=1, minsize=100)
        self.box[9].rowconfigure(0, weight=1, minsize=100)
        self.button9 = tk.Button(self.box[9], command= lambda: self.target(9))
        self.button9.grid(row=0, column=0, sticky="nsew")

    def target(self, num):
        if self.current == "O":
            self.label[num] = tk.Label(self.box[num], text="X", font="Poppins 60")
            self.current = "X"
            self.playerX.append(num)
            self.checkWinner()
        elif self.current == "X":
            self.label[num] = tk.Label(self.box[num], text="O", font="Poppins 60")
            self.current = "O"
            self.playerO.append(num)
            self.checkWinner()
        else:
            self.label[num] = tk.Label(self.box[num], text="X", font="Poppins 60")
            self.current = "X"
            self.playerX.append(num)
            self.checkWinner()
        self.label[num].grid(row=0, column=0)

    def checkWinner(self):
        for i in self.combinations:
            if set(i).issubset(set(self.playerX)):
                print("player X is the winner")
                self.label[i[0]].configure(background="yellow", padx= 20)
                self.label[i[1]].configure(background="yellow", padx= 20)
                self.label[i[2]].configure(background="yellow", padx= 20)
                window.after(1000, lambda: self.endingFrame("X"))
                return

            elif set(i).issubset(set(self.playerO)):
                print("player O is the winner")
                self.label[i[0]].configure(background="yellow", padx= 20)
                self.label[i[1]].configure(background="yellow", padx= 20)
                self.label[i[2]].configure(background="yellow", padx= 20)
                window.after(1000, lambda: self.endingFrame("O"))
                return
                

    def change(self):
        self.container.destroy()
        self.secondFrame()

window = Mywindow()
window.mainloop()