# run this file to create a gui

from GUI import GUI # import the gui class file

gui = GUI() # create the GUI

def main():
    gui.showQuestion(1, 'This is question 1') # change a section's question
    answer = gui.getInput(1) # get input answer from a section, code pauses here until input is given
    print(answer)

    gui.showQuestion(2, 'This is question 2')
    answer = gui.getInput(2)
    print(answer)

    gui.showQuestion(3, 'This is question 3')
    answer = gui.getInput(3)
    print(answer)

    gui.showQuestion(4, 'This is question 4')
    answer = gui.getInput(4)
    print(answer)

    gui.clearScreen() # clear the screen
    print('### end of main method ###')



gui.after(500, main)
gui.root.mainloop()
