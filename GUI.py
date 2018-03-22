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
            self.labels.append( Label(self.root, text='Question', font='helvetica 20') )
            self.labels[i].grid(row=(2*i+1), column=1)

        self.entries = [] # create text boxes
        for j in range(4):
            self.entries.append( Entry(self.root) )
            self.entries[j].grid(row=(2*j+2), column=1, pady=(8, 25))

        self.buttons = [] # create buttons
        self.temp = [IntVar() for _ in range(4)]
        for k in range(4):
            self.buttons.append( Button(self.root, text="Submit", command=(lambda n=k: self.temp[n].set(1))) )
            self.buttons[k].grid(row=(2*k+2), column=2, pady=(8, 25))

    ######################################
    ## RETURN AN INPUT STRING FROM THE GUI
    ## num: the text box to get input from [1 - 4]
    ## Example to get input from the first text box -> getInput(1)
    def getInput(self, num):
        self.buttons[num-1].wait_variable(self.temp[num-1]) # wait for press
        return self.entries[num-1].get()

    ##############################
    ## CHANGE A SECTION'S QUESTION
    ## num: the number of the section that has the question [1 - 4]
    ## text: the updated question
    ## Example to change the first question -> changeQuestion(1, 'my new question')
    def changeQuestion(self, num, text):
        self.labels[num-1]['text'] = text
