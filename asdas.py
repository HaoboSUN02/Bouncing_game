from tkinter import*
import os

def start():
    os.system('python asd.py')

def continue_button():
    os.system('python continue.py')

def score_board():
    os.system('python rank.py')

tk=Tk()  #创建框架对象tk
tk.title('frame')   #框架对象tk显示的名字为'game'
tk.geometry('800x800')
photo = PhotoImage(file = "background.png")
the_label = Label(image=photo,text="The Ball Game",compound=CENTER).pack()



# tk.L(tk,text = 'User name: ').place(x=50,y=150)
frame1 = Frame(tk)



start_button = Button(tk,text='start a new game',command = lambda: start())
the_continue_button = Button(tk,text='continue the last game',command = lambda: continue_button())

rank_button = Button(tk,text='see the score board',command = lambda: score_board())
start_button.pack()
the_continue_button.pack()
rank_button.pack()



tk.update()    #显示框架的变化
tk.mainloop()