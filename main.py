from tkinter import *
import tkinter as tk
import calendar
root = tk.Tk()
root.title('My Personal Calender - Group 10')
root.geometry('600x450')

def show():

        m = int(month.get())
        y = int(year.get())
        output = calendar.month(y,m)

        cal.insert('end',output)

def clear():
        cal.delete(1.0,'end')

def exit():
        root.destroy()


m_label = Label(root,text="Made by Roll No. = 1,3,6,7,8",font=('verdana','10','bold'))
m_label.place(x=180,y=365)

m_label = Label(root,text="Month",font=('verdana','10','bold'))
m_label.place(x=150,y=80)

month = Spinbox(root, from_= 1, to = 12,width="5") 
month.place(x=210,y=80) 
  
y_label = Label(root,text="Year",font=('verdana','10','bold'))
y_label.place(x=290,y=80)

year = Spinbox(root, from_= 2020, to = 3000,width="8") 
year.place(x=340,y=80) 


cal = Text(root,width=21,height=8,relief=RIDGE,borderwidth=10)
cal.place(x=200,y=110)

show = Button(root,text="Show",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=4,command=show)
show.place(x=160,y=280)

clear = Button(root,text="Clear",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=4,command=clear)
clear.place(x=260,y=280)

exit = Button(root,text="Exit",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=4,command=exit)
exit.place(x=360,y=280)
root.mainloop()
