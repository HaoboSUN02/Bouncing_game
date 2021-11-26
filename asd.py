#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import tarfile
from tkinter import*
def user_signup():
    pass
    # menubar.add_cascade(label='menus', menu=menus)
    # menus.add_command(label='restart')
    # menus.add_command(label='go back to your last game')
    # menus.add_command(label='cheating code')
    # signup_window["menu"] = menubar




def user_login():

    file = open('coord.txt','w')
    file.write(enter_username.get())
    file.close()
    os.system('python box.py')

tk=Tk()  #??????tk
tk.title('Bouncing Game')   #????tk??????'game'
tk.geometry('300x200')


text_var = StringVar
enter_username = Entry(tk,textvariable = text_var)#.place(x=160,y=150)
enter_username.grid(row=0, column=1, sticky=E)
login_button = Button(tk,text='login',command = lambda :user_login()).grid(row=0,column=2,sticky=E)
# cheatingcode()


tk.update()    #???????
tk.mainloop()