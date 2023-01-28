from tkinter import *
import time

root = Tk()

root.title("Heure")
root.geometry("1920x1040")
root.config(bg="white")

def horloge():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    

    Label_heure.config(text=h)
    Label_minute.config(text=m)
    Label_seconde.config(text=s)

    Label_heure.after(200, horloge)

     #h
Label_heure= Label(root, text="12", font=("times new roman", 50, "bold"), bg="white")
Label_heure.place(x=600, y=300, width=200, height=130)

heure = Label(root, text="heure", font=("times new roman", 20, "bold"), bg="white")
heure.place(x=600, y=450, width=200, height=30)

     #m
Label_minute= Label(root, text="12", font=("times new roman", 50, "bold"), bg="white")
Label_minute.place(x=850, y=300, width=200, height=130)

minute = Label(root, text="minute", font=("times new roman", 20, "bold"), bg="white")
minute.place(x=850, y=450, width=200, height=30)

     #s
Label_seconde= Label(root, text="12", font=("times new roman", 50, "bold"), bg="white")
Label_seconde.place(x=1100, y=300, width=200, height=130)

seconde = Label(root, text="seconde", font=("times new roman", 20, "bold"), bg="white")
seconde.place(x=1100, y=450, width=200, height=30)

horloge()

root.mainloop()