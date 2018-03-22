# run this file to create a gui

from GUI import GUI # import the gui class file

gui = GUI() # create the GUI

def main():
    gui.changeQuestion(1, 'This is question 1') # change a section's question
    answer = gui.getInput(1) # get input answer from a section, code pauses here until input is given
    print(answer)

    # this code will run after an input is given
    gui.changeQuestion(2, 'This is question 2')
    gui.changeQuestion(3, 'This is question 3')
    gui.changeQuestion(4, 'This is question 4')



gui.after(1000, main)
gui.root.mainloop()
