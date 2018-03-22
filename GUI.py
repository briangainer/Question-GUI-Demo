from tkinter import *

class GUI(Frame):
    def __init__(self):
        self.root = Tk()
        super().__init__(self.root)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.geometry("500x500") # set window size
        self.root.title('Research Demo') # add a window title

        self.labels = [] # create labels
        for i in range(4):
            self.labels.append( Label(self.root, text='Question 1', font='helvetica 20') )
            self.labels[i].grid(row=(2*i+1), column=1)

        self.entries = [] # create text boxes
        for j in range(4):
            self.entries.append( Entry(self.root) )
            self.entries[j].grid(row=(2*j+2), column=1, pady=(8, 25))

        self.buttons = [] # create buttons
        for k in range(4):
            self.buttons.append( Button(self.root, text="Submit", command=(lambda n=k: self.pressed(n))) )
            self.buttons[k].grid(row=(2*k+2), column=2, pady=(8, 25))
            
        self.root.mainloop()

    # this method responds to a button press
    def pressed(self, num):
        print(self.entries[num].get())

    ########################
    ## HIDE A SCREEN SECTION
    ## num: the number of the section that you want to hide [1 - 4]
    ## Example to hide the first section -> hideSection(1)
    def hideSection(self, num):
        pass

    ########################
    ## SHOW A SCREEN SECTION
    ## num: the number of the section that you want to show [1 - 4]
    ## Example to show the first section -> showSection(1)
    def showSection(self, num):
        pass

    ##############################
    ## CHANGE A SECTION'S QUESTION
    ## num: the number of the section that has the question [1 - 4]
    ## text: the updated question
    ## Example to change the first question -> changeQuestion(1, 'my new question')
    def changeQuestion(self, num, text):
        pass
