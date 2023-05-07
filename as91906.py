from tkinter import *
from tkinter import messagebox 

class GUI:
    def __init__(self, parent):
        self.homeFrame = Frame(parent)
        self.makeOrderFrame = Frame(parent)
        self.viewOrderFrame = Frame(parent)

        b1 = Button(self.homeFrame, text = "Make Order", command=self.makeOrder)
        b1.pack()
        b2 = Button(self.homeFrame, text = "View Orders", command=self.viewOrder)
        b2.pack()
        self.homeFrame.pack()
    
    def makeOrder(self):
        self.homeFrame.destroy()
        print('awed')
    
    def viewOrder(self):
        self.homeFrame.destroy()
        print('aw')
    

if __name__ == "__main__":
    root = Tk()
    StartProgram = GUI(root)
    root.mainloop()