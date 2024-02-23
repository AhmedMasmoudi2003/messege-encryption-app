from tkinter import *
import clipboard
import pyperclip

def paste():
    field.insert(END,pyperclip.paste())
def copy():
    pyperclip.copy(field.get("1.0",END))
def clear():
    field.delete(1.0,END)
def encryption():
    x = field.get("1.0",END)
    y = ""

    for i in range (len(x)) :
    
        if ord(x[i].upper())%2==0 :#positif
            y += chr(ord(x[i])-1)
        elif ord(x[i].upper())%2==1:#negatif
            y += chr(ord(x[i])+1)
        
    field.delete(1.0,END)
    field.insert(END,y)
    
def decryption():
    x = field.get("1.0",END)
    y = ""

    for i in range (len(x)) :
    
        if ord(x[i].upper())%2==0 :#positif
            y += chr(ord(x[i])-1)
        elif ord(x[i].upper())%2==1:#negatif
            y += chr(ord(x[i])+1)
        
    field.delete(1.0,END)
    field.insert(END,y)
    
#window settings-------------------------------------------------------------------------------------------------------------
screen = Tk()
screen.title("Hanashi Encryption 1.0")
screen.geometry("800x600")
screen.resizable(False,False)

#background image-------------------------------------------------------------------------------------------------------------
bgimage=PhotoImage(file="Hanashi Encryption background.png")
bgLabel=Label(screen,image=bgimage)
bgLabel.pack()
screen.iconbitmap('Hanashi_Encryption_icon.ico')

#label-------------------------------------------------------------------------------------------------------------
label = Label(text="Write your text here :",font=("Segoe UI", 12),fg="white",bg="#1d4796")
label.place(x=30,y=75)

#text field-------------------------------------------------------------------------------------------------------------
field = Text(width=19,height=7,bd=3,font=("Segoe UI", 22))
field.place(x=25,y=115)

#buttons-------------------------------------------------------------------------------------------------------------
copy_btn = Button(text="Copy",fg="white",bg="#1d4796",height=1,pady=7,width=10,font=("Segoe UI", 12),command=copy)
copy_btn.place(x=350,y=115)

paste_btn = Button(text="Paste",fg="white",bg="#1d4796",height=1,pady=7,width=10,font=("Segoe UI", 12),command=paste)
paste_btn.place(x=350,y=183)

clear_btn = Button(text="Clear",fg="white",bg="#1d4796",height=1,pady=7,width=10,font=("Segoe UI", 12),command=clear)
clear_btn.place(x=350,y=250)

encryption_btn = Button(text="Encryption",fg="white",bg="#1d4796",height=1,pady=7,width=10,font=("Segoe UI", 12),command=encryption)
encryption_btn.place(x=70,y=415)

decryption_btn = Button(text="Decryption",fg="white",bg="#1d4796",height=1,pady=7,width=10,font=("Segoe UI", 12),command=decryption)
decryption_btn.place(x=190,y=415)

screen.mainloop()













