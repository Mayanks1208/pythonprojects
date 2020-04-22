from tkinter import *
import time

def times():
    current_time=time.strftime("%I: %M: %S: %p")
    clock_lbl=Label(root,font = "berlin 80 bold", bg = "white" ,fg="black",text=current_time)
    clock_lbl.after(200,times)
    clock_lbl.grid(row = 0, column = 1)

root=Tk()
root.title("Digital clock")
root.resizable(FALSE,FALSE)
times()
root.mainloop()
