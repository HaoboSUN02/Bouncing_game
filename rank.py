from tkinter import*


tk=Tk()
tk.title('Score Board')
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
file = open('userdata.txt','r')
rank=[]
lines = file.readlines()
for line in lines:
    if line == "\n":
        continue
    line = line.rstrip()

    pos = line.find(':')
    rank.append((int(line[0:pos]),line[pos:]))
rank.sort(reverse=True)
print(rank)


txt = "The Score Board"
first_txt = "1."+ str(rank[0])
second_txt = "2."+ str(rank[1])
third_txt = "3."+ str(rank[2])
forth_txt = "4."+ str(rank[3])
fifth_txt = "5."+ str(rank[4])
scoreText = canvas.create_text(250, 10, fill="green", font="Times 20 italic bold", text=txt)
first = canvas.create_text(100, 50, fill="green", font="Times 20 italic bold", text=first_txt)
second = canvas.create_text(100, 100, fill="green", font="Times 20 italic bold", text=second_txt)
third = canvas.create_text(100, 150, fill="green", font="Times 20 italic bold", text=third_txt)
fouth = canvas.create_text(100, 200, fill="green", font="Times 20 italic bold", text=forth_txt)
fifth = canvas.create_text(100, 250, fill="green", font="Times 20 italic bold", text=fifth_txt)


canvas.pack()
tk.update()
tk.mainloop()