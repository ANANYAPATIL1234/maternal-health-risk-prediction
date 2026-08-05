
import tkinter as tk
from tkinter.messagebox import showinfo

def iseven():
    print("you clicked button")

    num=int(t1.get())
    if num%2==0:
        print(f"{num} is Even")
        showinfo("result",f"{num} is even")

    else:
        print(f"{num} is Odd")
        showinfo("result",f"{num} is odd")

window=tk.Tk()

window.geometry('500x500')
window.title("My window")

lbl=tk.Label(window,text="Enter a number")
lbl.place(x=100,y=50)

t1=tk.Entry(window)
t1.place(x=200,y=50)

btn=tk.Button(window,text=" Is Even ? ",bg="cyan",command=iseven)
btn.place(x=200,y=100)

#window.config(bg="blue")
window.mainloop()