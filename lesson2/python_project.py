
#15/09/2022

#****************************************************
# Python Calculator with GUI (Graphic User Interface)
#****************************************************

from cProfile import label
from tkinter import *
from turtle import width # import the tkinter library

def button_press(num):   # defining each button press
    pass

def clear():
    pass

def clear():
    pass




# Designing the user interface

window = Tk()
window.title("python Calculator")
window.geometry("500x500")
window.configure(bg="871b548")

equation_text = ""

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('console', 20), bg="white") width=24, height=2
label.pack()

frame = frame(window)
frame.pack()

button1 - Button ( frame, text=1, height=1, width=1, font=35)
