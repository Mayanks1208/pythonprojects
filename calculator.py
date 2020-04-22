from tkinter import *


def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    
    elif text=="c":
        scvalue.set("")
        screen.update()

    else:~
        scvalue.set(scvalue.get()+text)
        screen.update()


root=Tk()
root.geometry("544x600")

root.title("Calculator")
root.resizable(0,0)


scvalue=StringVar()
scvalue.set(" ")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold",relief=GROOVE)

screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="GREY")
b=Button(f,text="9",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="GREY")
b=Button(f,text="6",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="GREY")
b=Button(f,text="3",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="GREY")
b=Button(f,text="0",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="00",padx=35,pady=20,font="lucida 20 bold",relief=GROOVE)
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="c",padx=28,pady=18,font="lucida 25 bold",relief=GROOVE)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="GREY")
b=Button(f,text="/",padx=28,pady=18,font="lucida 25 bold")
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=28,pady=18,font="lucida 25 bold")
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=28,pady=18,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="GREY")
b=Button(f,text="+",padx=28,pady=18,bg="red",fg="white",font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=28,pady=18,font="lucida 25 bold")
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=29,pady=18,font="lucida 25 bold")
b.pack(side=LEFT,padx=21,pady=5)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()









