from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Messagebox")
root.geometry("655x450")
def myfunc():
    print("This function")

def help():
    print("It will help your")
    tmsg.shownfo("Help","It will help you")

def rate():
    print("rate us!")
    value=tmsg.askquestion("Experience","how was your experience")

    if value=="Yes":
        msg="Great,rate us on our official website"
    else:
        msg="Tell us what went wrong, we will call you soon"
    
    tmsg.showinfo("Experience",msg)



mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New file",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save as",command=myfunc)
m1.add_separator()
m1.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Help",command=help)
m2.add_command(label="rate us",command=rate)
mainmenu.add_cascade(label="Help",menu=m2)
root.config(menu=mainmenu)


root.mainloop()

