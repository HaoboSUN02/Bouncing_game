#!/usr/bin/python
# -*- coding: latin-1 -*-
import random
import time
from tkinter import *



class Ball:
 def __init__(self,canvas,bouncing_line,color):
     self.canvas=canvas
     self.bouncing_line=bouncing_line
     self.canvas_height=self.canvas.winfo_height()
     self.canvas_width=self.canvas.winfo_width()
     self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
     self.canvas.move(self.id, 245, 100)
     starts = [-3, -2, -1, 1, 2, 3]
     random.shuffle(starts)
     self.x = starts[0]
     self.y = -3
     self.hit_bottom=False


 def hit_line(self,position):
     line_position=self.canvas.coords(self.bouncing_line.id)
     if position[2]>=line_position[0] and position[0]<=line_position[2]:
         if position[3]>=line_position[1] and position[3]<=line_position[3]:
             return True
     return False


 def moving(self):
     global score
     self.canvas.move(self.id,self.x,self.y)
     position=self.canvas.coords(self.id)
     if position[1]<=0:
         self.y=3
         if score > 0 and score%10==0:
             self.y += 3
     if position[3]>=self.canvas_height: #?????????? ???hit_bottom?True
         self.hit_bottom=True
     if self.hit_line(position)==True: #???????????Y???????
         self.y=-3
         score += 1
         txt = name[0] + " score: " + str(score)
         canvas.itemconfigure(scoreText, text=txt)
         if score%5==0:
             self.y -= 3
     if position[0]<=0:    #??????????????X?????????3???
         self.x=3
         if score > 0 and score%10==0:
             self.x += 3
     if position[2]>=self.canvas_width:   #??????????????????????3???
         self.x=-3
         if score > 0 and score%10==0:
             self.x -= 3







class Line:     #????paddle?
 def __init__(self,canvas,color):  #paddle???????????????????
     self.bosskey=False
     self.canvas=canvas   #?canvas????self.canvas
     self.id=canvas.create_rectangle(0,0,100,10,fill=color)   #???????????????self.id
     self.canvas.move(self.id,200,300)      #???????200?300??
     self.x=0    #
     self.canvas_width=self.canvas.winfo_width()    #????????canvas_width??
     self.canvas.bind_all('<KeyPress-Left>',self.turn_left)   #?bind_all()?????????tun_left??
     self.canvas.bind_all('<KeyPress-Right>',self.turn_right)  #???????turn_right??
     self.canvas.bind_all('<a>',self.cheating)
     self.canvas.bind_all('<b>',self.boss_key)
     self.canvas.bind_all('<s>',self.save)
 def turn_left(self,evt):#???evt???????????????????????
     self.x=-10

 def turn_right(self,evt):  #?????????????5???
     self.x=10

 def cheating(self,evt):

     global score
     score += 100


 def save(self,evt):
     global score
     coords = open('coord.txt', 'a')
     name = coords.write(str(score))
     coords.close()


 def boss_key(self,evt):
     if self.bosskey==False:
         self.bosskey=True
         self.boss_window = Tk()
         self.boss_window.title('python work')
         self.boss_window.geometry('1920x1080')
         self.boss_photo = PhotoImage(file="screenshot.png")
         self.the_boss_label = Label(self.boss_window,image=self.boss_photo, compound=CENTER).pack()
         # boss_window.update()
         self.boss_window.mainloop()
     else:
         self.bosskey=False
         self.boss_window.destroy()





 def moving(self):   #????draw??
     self.canvas.move(self.id,self.x,0)  #??????????self.x?????
     position=self.canvas.coords(self.id)   #????????????????pos???
     if position[0]<=0:       #????x???0????????
         self.x=0
     elif position[2]>=self.canvas_width:  #???????????????????????0
         self.x=0






# def cheating():
#     cheating_window = Toplevel()
#     cheating_window.title('cheating code')
#     cheating_window.geometry('160x150')
#     enter_cheating_code = Entry(cheating_window).place(x=16, y=15)
#     image = PhotoImage(file = "screenshot.png")


def menu():
    menubar = Menu(tk)
    menus = Menu(menubar)

    menubar.add_cascade(label='menus',menu = menus)
    # menus.add_command(label = 'restart')
    menus.add_command(label = 'go back to your last game')
    # menus.add_command(label = 'cheating code',command = lambda:cheating())
    tk["menu"] = menubar


file = open('coord.txt','r')
lines = file.readline()
name = lines.split()
# file.close()

#??????????????????????
tk=Tk()  #??????tk
tk.title('Bouncing Game')   #????tk??????'game'
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)  #????canvas???tk?????
score = 0
txt = name[0] + " Score: " + str(score)
instru="move left <-\n" \
       "move right ->\n" \
       "boss key <b>\n" \
       "cheating button <a> (+100score)\n" \
       "save button <s>\n" \
       "click the menu at the top to stop"
scoreText = canvas.create_text(250, 10, fill="red", font="Times 20 italic bold", text=txt)
instructions = canvas.create_text(350,100,fill="red",font="Times 20 italic bold", text=instru)

menu()
canvas.pack()  #???????
tk.update()    #???????


#???????ball??????ball??????????
bouncing_line=Line(canvas,"red")  #????????paddle?
ball=Ball(canvas,bouncing_line,'green') #????????ball?

if __name__ == "__main__":
    while True:   #???while??????????????
     if ball.hit_bottom==False:  #???????????????
         ball.moving()   #??ball?????draw??
         bouncing_line.moving()#??paddle?????draw??
         tk.update_idletasks()
         tk.update()    #????
         time.sleep(0.01) #??0.01?

     elif ball.hit_bottom==True:  #?????????

         canvas.create_text(200,300,text='game over, your final score is '+str(score),font=('Times',22)) #??200?100?????????...????22?
         write_score = open('userdata.txt', 'a')
         your_score = write_score.write(  str(score) +':'+ name[0]+'\n')
         write_score.close()
         break
         # your_score = write_score.write(str(score))
     tk.update()  #????


tk.mainloop()