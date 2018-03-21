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
        # 1st section
        self.label_1 = Label(self.root, text='This is the First Question', font='helvetica 20')
        self.entry_1 = Entry(self.root)
        self.button_1 = Button(self.root, text="Submit", command=self.press_1)
        self.label_1.grid(row=1, column=1)
        self.entry_1.grid(row=2, column=1, pady=(8, 25))
        self.button_1.grid(row=2, column=2, pady=(8, 25))
        # 2nd section
        self.label_2 = Label(self.root, text='This is the Second Question', font='helvetica 20')
        self.entry_2 = Entry(self.root)
        self.button_2 = Button(self.root, text="Submit", command=self.press_2)
        self.label_2.grid(row=3, column=1)
        self.entry_2.grid(row=4, column=1, pady=(8, 25))
        self.button_2.grid(row=4, column=2, pady=(8, 25))
        # 3rd section
        self.label_3 = Label(self.root, text='This is the Third Question', font='helvetica 20')
        self.entry_3 = Entry(self.root)
        self.button_3 = Button(self.root, text="Submit", command=self.press_3)
        self.label_3.grid(row=5, column=1)
        self.entry_3.grid(row=6, column=1, pady=(8, 25))
        self.button_3.grid(row=6, column=2, pady=(8, 25))
        # 4th section
        self.label_4 = Label(self.root, text='This is the Fourth Question', font='helvetica 20')
        self.entry_4 = Entry(self.root)
        self.button_4 = Button(self.root, text="Submit", command=self.press_4)
        self.label_4.grid(row=7, column=1)
        self.entry_4.grid(row=8, column=1, pady=(8, 25))
        self.button_4.grid(row=8, column=2, pady=(8, 25))
        self.root.mainloop() # code after this line will execute after window is closed

    # these 4 methods print what is in the text box next to it
    def press_1(self):
        print(self.entry_1.get())

    def press_2(self):
        print(self.entry_2.get())

    def press_3(self):
        print(self.entry_3.get())

    def press_4(self):
        print(self.entry_4.get())
