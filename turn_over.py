#Turn over notepad widget for work. sgashburn@gmail.com, 8/30/2020
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext



def clearTextInput():
    textentry_1.delete("1.0","end")


# GUI window with buttons 
if __name__ == "__main__":
	 
# create a GUI window 
    gui = Tk() 
    #create label
    Label (gui, text="Turnover Notes", bg="blue4", fg="white", font= "none 20 bold") .grid(row=1, column=0, pady = 10)

    #create a text entry box
    textentry_1 = scrolledtext.ScrolledText(gui, wrap = tk.WORD, bd = "5", width = 70, height = 15, font = ("Times New Roman", 15))
    textentry_1.grid(row=2, column=0, pady = 10, padx = 10)
    textentry_1.configure(font = ("times new roman", 20, "bold"))
                                      
      
    # set the background colour of GUI window 
    gui.configure(background="blue4") 
  
    # set the title of GUI window 
    gui.title("SHIFT TURNOVER") 
    
    # set the configuration of GUI window 
    gui.geometry("1030x620") 
    
    #puts the cursor on the field
    textentry_1.focus()
 
    #button to clear the text field
    btnRead=tk.Button(gui, height=1, width=10, text="Clear", 
                    command=clearTextInput)
    btnRead.grid(row = 3, column = 0)

    # start the GUI 
    gui.mainloop() 
    
    
    
