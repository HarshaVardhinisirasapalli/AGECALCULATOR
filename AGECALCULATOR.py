import tkinter as tk
from tkinter import *
from datetime import date

root = tk.Tk()
root.title("Age Calculator")
root.geometry("1000x800")

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    age_label = Label(text=f"{nameValue.get()}, your age is {age}", font=("arial", 28))
    age_label.place(x=300, y=500)

Label(text="Name", font=("algerian", 23)).place(x=200, y=200)
Label(text="Year", font=("algerian", 23)).place(x=200, y=250)
Label(text="Month", font=("algerian", 23)).place(x=200, y=300)
Label(text="Date", font=("algerian", 23)).place(x=200, y=350)

nameValue = tk.StringVar()
yearValue = tk.StringVar()
monthValue = tk.StringVar()
dayValue = tk.StringVar()

nameEntry = tk.Entry(root, textvariable=nameValue, width=30, bd=3, font=("arial", 20))
nameEntry.place(x=300, y=200)
yearEntry = tk.Entry(root, textvariable=yearValue, width=30, bd=3, font=("arial", 20))
yearEntry.place(x=300, y=250)
monthEntry = tk.Entry(root, textvariable=monthValue, width=30, bd=3, font=("arial", 20))
monthEntry.place(x=300, y=300)
dayEntry = tk.Entry(root, textvariable=dayValue, width=30, bd=3, font=("arial", 20))
dayEntry.place(x=300, y=350)

Button(text="Calculate Age", font=20, bg="black", fg="white", width=12, height=2, command=calculateAge).place(x=300, y=450)

root.mainloop()
