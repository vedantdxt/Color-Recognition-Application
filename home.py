# Import required libraries
import sys
import os
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()
    
# Define the geometry of the window
win.geometry("1920x1080")
win.title("Home")
win.configure(bg="black")

def run_extractor():
    os.system('extractor.py')

def run_histogram():
    os.system('histogram.py')

label = Label(win, text = "\nImage Processing & Colour Analysis", bg="black", fg = "red", font=('TW 40 bold italic underline'))
label.pack()

label = Label(win, text = "\nA Python Project by - Aniket, Anurag, Shyam & Vedant | SYMCA @ KKWIEER", bg="black", fg = "white", font=('TW 15 bold italic'))
label.pack()

b1 = Button(win,text = "Colour Extraction", bg="red", fg = "white", font=('TW 15 bold italic'), activeforeground = "red",activebackground = "pink",pady=10, command=run_extractor)  
b1.place(x=500, y=340)

b2 = Button(win, text = "Image Histogram", bg="red", fg = "white", font=('TW 15 bold italic'), activeforeground = "blue",activebackground = "pink",pady=10, command=run_histogram)  
b2.place(x=700, y=340)

b1.pack
b2.pack 

# Bind the function to configure the parent window
win.mainloop()
