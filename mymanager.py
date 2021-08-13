from tkinter import *
import os
from tkinter import ttk

win = Tk()
win.config(bg='black')
win.title('My Manager')

title_label = Label(win,text="My Manager",font=('helvatica',30,'bold'),bg='black',fg='white')
title_label.grid(row=0,column=0)

#VARIABLE FOR WIDTH OF THE BUTTON
A = 15
def Quitt():
    win.destroy()

#BUTTONS
but1 = Button(win,width = A,text='Device manager',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('devmgmt.msc'))
but1.grid(row=1,column=0)
but2 = Button(win,width = A,text='Control Panel',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('control'))
but2.grid(row=2,column=0)
but3 = Button(win,width = A,text='Network Settings',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('ncpa.cpl'))
but3.grid(row=3,column=0)
but4 = Button(win,width = A,text='Mouse Settings',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('main.cpl'))
but4.grid(row=4,column=0)
but5 = Button(win,width = A,text='Registry Editor',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('regedit'))
but5.grid(row=5,column=0)
but6 = Button(win,width = A,text='System Properties',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('sysdm.cpl'))
but6.grid(row=1,column=1)
but7 = Button(win,width = A,text='Task Manager',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('taskmgr'))
but7.grid(row=2,column=1)
but8 = Button(win,width = A,text='Uninstall',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('appwiz.cpl'))
but8.grid(row=3,column=1)
but9 = Button(win,width = A,text='System Services',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = lambda :os.system('services.msc'))
but9.grid(row=4,column=1)
but10 = Button(win,width = A,text='Exit',font=('helvatica',16,'bold'),bg='#FF131B',fg='#ffffff',command = Quitt)
but10.grid(row=5,column=1)

win.mainloop()
