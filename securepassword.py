from tkinter import *
from tkinter.ttk import Combobox
import random


secure=(('a' , '!!'),
          ('b' , '@'),
          ('c' , '#'),
          ('d' , '$'),
          ('e' , '^'),
          ('f' , '}'),
          ('g', ']'),
          ('h' , ')'),
          ('i' , '*'),
          ('j' , '='),
          ('k' , '+'),
          ('l' , '-'),
          ('m' , '_'),
          ('n' , '>'),
          ('o' , '<'),
          ('p' , '.'),
          ('q' , '%'),
          ('r' , '&'),
          ('s' , '('),
          ('t' , '{'),
          ('u' , '['),
          ('x' , '?'),
          ('y' , ','),
          ('z' , '|'),)
def securePassword(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password

 

if __name__== "__main__":
    password=input("enter the password of your choice")
    password=securePassword(password)
    print(f"your new password is {password}")
    
    
from tkinter import *

win= Tk()
#Set the geometry of tkinter frame
Label(win,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)
win.geometry("750x250")
def get_value():
   e_text=password
   Label(win, text=e_text, font= ('Century 15 bold')).pack(pady=20)
#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)
#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= get_value)
button.pack()
win.mainloop()
