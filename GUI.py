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

        self.labels = [] # create labels [ [ Label, (row, col) ] ]
        for i in range(4):
            self.labels.append( [ Label(self.root, text='Question', font='helvetica 20'), (2*i+1, 1) ] )
            #self.labels[i][0].grid(row=(2*i+1), column=1)

        self.entries = [] # create text boxes [ [Entry, (row, col) ] ]
        for j in range(4):
            self.entries.append( [ Entry(self.root), (2*j+2, 1) ] )
            #self.entries[j][0].grid(row=(2*j+2), column=1, pady=(8, 25))

        self.buttons = [] # create buttons [ [ Button, (row, col) ] ]
        self.temp = [IntVar() for _ in range(4)]
        for k in range(4):
            self.buttons.append( [ Button(self.root, text="Submit", command=(lambda n=k: self.temp[n].set(1))), (2*k+2, 2) ] )
            #self.buttons[k].grid(row=(2*k+2), column=2, pady=(8, 25))

    ######################################
    ## RETURN AN INPUT STRING FROM THE GUI
    ## num: the text box to get input from [1 - 4]
    ## Example to get input from the first text box -> getInput(1)
    def getInput(self, num):
        self.buttons[num-1][0].wait_variable(self.temp[num-1]) # wait for press
        return self.entries[num-1][0].get()

    ##############################
    ## CHANGE A SECTION'S QUESTION
    ## num: the number of the section that has the question [1 - 4]
    ## text: the updated question
    ## Example to change the first question -> changeQuestion(1, 'my new question')
    def showQuestion(self, num, text):
        index = num - 1
        self.labels[index][0]['text'] = text # set question
        self.labels[index][0].grid(row=self.labels[index][1][0], column=self.labels[index][1][1]) # show label
        self.entries[index][0].grid(row=self.entries[index][1][0], column=self.entries[index][1][1], pady=(8, 25)) # show entry
        self.buttons[index][0].grid(row=self.buttons[index][1][0], column=self.buttons[index][1][1], pady=(8, 25)) # show button


    #######################
    ## CLEAR THE GUI SCREEN
    def clearScreen(self):
        pass
