from tkinter import *

win=Tk()
win.geometry("250x250")
win.title("Frame changer")
# win.resizable(FALSE,FALSE)

def frame1():
    first_frame=Frame(win,bg="yellow")
    first_frame.place(x=0,y=0,width=250,height=250)
    Button(first_frame,text="Go to the form >",bg="black",fg="white",command=frame2).place(x=80,y=100)


def frame2():
    second_frame=Frame(win,bg="red")
    second_frame.place(x=0,y=0,width=250,height=250)
    Button(second_frame,text="Go to the form >",bg="black",fg="white",command=frame1).place(x=80,y=100)



if __name__=="__main__":
    frame1()

win.mainloop()


