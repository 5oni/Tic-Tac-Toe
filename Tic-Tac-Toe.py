from tkinter import Tk, Menu, filedialog, messagebox, LabelFrame, RIDGE, \
Frame, Entry, W, END, Button, E, Label, Listbox, Scrollbar, \
RIGHT, Y, X, BOTTOM, LEFT

root=Tk()
root.title("Tic-Tac-Toe")
root.geometry("420x500")
root.resizable(0,0)
# root.configure(background="black")
count=1
def clear():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
def game():
    def winner(player_name):
        f1=Frame()
        f1.place(x=0,y=0)
        r=Tk()
        r.geometry("400x200")
        r.configure(background="black")
        lb=Label(r,text=player_name+" is winner",font=("Arial",25),bg="black",fg="white")
        lb.pack()
        
        play_again=Button(r,text="Play Again",font=("Arial",15),command=lambda:[game(),r.destroy()])
        play_again.pack()
        r.mainloop()
    def txt(b):
        global count
        count+=1
        if (count%2==0):
            if (b["text"]==""):
                b["text"]="0"
            
        else:
            if (b["text"]==""):
                b["text"]="X"
        if(b11['text']=="0" and b12['text']=="0" and b13['text']=="0" ):
            winner(" first player")
            
        elif(b21['text']=="0" and b22['text']=="0" and b23['text']=="0" ):
            winner("first player")
        elif(b31['text']=="0" and b32['text']=="0" and b33['text']=="0" ):
            winner("first player")
        elif(b11['text']=="0" and b21['text']=="0" and b31['text']=="0" ):
            winner("first player")
        elif(b12['text']=="0" and b22['text']=="0" and b32['text']=="0" ):
            winner("first player")
        elif(b13['text']=="0" and b23['text']=="0" and b33['text']=="0" ):
            winner("first player")
        elif(b11['text']=="0" and b22['text']=="0" and b33['text']=="0" ):
            winner("first player")
        elif(b13['text']=="0" and b22['text']=="0" and b31['text']=="0" ):
            winner("first player")



        elif(b11['text']=="X" and b12['text']=="X" and b13['text']=="X"):
            winner("Second player")
        elif(b21['text']=="X" and b22['text']=="X" and b23['text']=="X"):
            winner("Second player")
        elif(b31['text']=="X" and b32['text']=="X" and b33['text']=="X"):
            winner("Second player")
        elif(b11['text']=="X" and b21['text']=="X" and b31['text']=="X"):
            winner("Second player")
        elif(b12['text']=="X" and b22['text']=="X" and b32['text']=="X"):
            winner("Second player")
        elif(b13['text']=="X" and b23['text']=="X" and b33['text']=="X"):
            winner("Second player")
        elif(b11['text']=="X" and b22['text']=="X" and b33['text']=="X"):
            winner("Second player")
        elif(b13['text']=="X" and b22['text']=="X" and b31['text']=="X"):
            winner("Second player")

        
    f1=Frame()
    f1.place(x=0,y=0,width=364,height=500)
    un=Label(root,text="Tic-Tac-Toe",fg="black",font=("Arial",20))
    un.grid(row=0,column=0,columnspan=3)
    b11=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b11))
    b11.grid(row=1,column=0)
    b12=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b12))
    b12.grid(row=1,column=1)
    b13=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b13))
    b13.grid(row=1,column=2)
    b21=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b21))
    b21.grid(row=2,column=0)
    b22=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b22))
    b22.grid(row=2,column=1)
    b23=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b23))
    b23.grid(row=2,column=2)
    b31=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b31))
    b31.grid(row=3,column=0)
    b32=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b32))
    b32.grid(row=3,column=1)
    b33=Button(root,width=10,height=5,font=("Arial",15),command=lambda:txt(b33))
    b33.grid(row=3,column=2)
    play_again=Button(root,text="Play Again",font=("Arial",15),command=game)
    play_again.grid(row=4,column=0,columnspan=3)
    
    
game()

play_again=Button(root,text="Play Again",font=("Arial",15),command=game)
play_again.grid(row=4,column=0,columnspan=3)
root.mainloop()
