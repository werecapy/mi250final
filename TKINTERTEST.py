from tkinter import *
import sys
import time
import os
#--------Display functions-----
def clear_window():
    """Destroy all widgets in the window"""
    for widget in myroot.winfo_children():
        widget.destroy()
def user_input():
    """User info is put in here"""
    clear_window()
    frame=Frame(myroot)
    frame.pack(padx=5, pady=5)
    #Page label
    Label(frame, text="Who are you?", fg="blue", bg="red").pack(padx=5, pady=5)
    #Name entry
    Label(frame, text="Name:", fg="blue", bg="red").pack(padx=5, pady=5)
    name_entry = Entry(frame, width=40)
    name_entry.pack(padx=5, pady=5)
    name_entry.focus

    Button(frame, text="Submit", command=lambda:(f"So your name is {name_entry.get()}")
           ).pack(padx=5, pady=5)

def quit():
    pass

def start_menu():


    frame = Frame(myroot)
    frame.pack(padx=5, pady=5)
    Label(frame, text="Welcome to Mascot Dating Simulator!").pack(padx=5, pady=5)
    Button(frame, text="Start", command=user_input).pack(padx=5, pady=5)
    Button(frame, text="Quit", command=quit).pack(padx=5, pady=5)




# Initialize main window
myroot = Tk()
myroot.title("Mascot Dating Simulator")
myroot.geometry("500x500")
myroot.resizable(False, False)

start_menu()

myroot.mainloop()