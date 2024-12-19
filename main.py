# Import the necessary modules:
import tkinter as tk
from tkinter import messagebox

#Create the main application window:
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

#Define the functions for the calculator operations:
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

#Create the display screen:
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

#Create the buttons for the calculator:
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

#Run the main event loop:
root.mainloop()