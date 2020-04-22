~# import tk,ttk
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win=tk.Tk()   
win.title("KUMBH HARIDWAR")#change the titile of our window

f1=ttk.LabelFrame(win,text="ENTER TOURIST'S DETAILS BELOW")
f1.grid(row=4,column=0,padx=40,pady=40)




# create labels
label=ttk.Label(win,text="WELCOME TO MAHAKUMBH 2021 HARIDWAR",font="comicsansms 30 bold",foreground="orange")
label.grid(row=0,column=9)

label=ttk.Label(win,text="HAR HAR GANGE",font="comicsansms 40 bold",foreground="red")
label.grid(row=2,column=9)

label=ttk.Label(win,text="30 JUNE 2021 - 15 JULY 2021",font="comicsansms 8 bold",foreground="red")

label.grid(row=3,column=9)




name_label=ttk.Label(f1,text="Enter tourist's name:",font="comicsansms 12 bold")
name_label.grid(row=4,column=0,sticky=tk.W)

phone_label=ttk.Label(f1,text="Enter tourist's mobile number:",font="comicsansms 12 bold")
phone_label.grid(row=5,column=0,sticky=tk.W)

person_label=ttk.Label(f1,text="Number of person with you:",font="comicsansms 12 bold")
person_label.grid(row=6,column=0,sticky=tk.W)#sticky----> FOR KEEP OUR TEXT LEFTY SIDE 

aadhar_label=ttk.Label(f1,text="Enter tourist's aadhar number",font="comicsansms 12 bold")
aadhar_label.grid(row=7,column=0,sticky=tk.W)


gender_label=ttk.Label(f1,text="Select tourist's gender:",font="comicsansms 12 bold")
gender_label.grid(row=8,column=0,sticky=tk.W)


state_label=ttk.Label(f1,text="Select tourist's state:",font="comicsansms 12 bold")
state_label.grid(row=9,column=0,sticky=tk.W)


city_label=ttk.Label(f1,text="Select tourist's city:",font="comicsansms 12 bold")
city_label.grid(row=10,column=0,sticky=tk.W)



#create the entry box....
name_var=tk.StringVar()
name_entrybox=ttk.Entry(f1,width=20,textvariable=name_var)
name_entrybox.grid(row=4,column=1)
name_entrybox.focus()

phone_var=tk.StringVar()
phone_entrybox=ttk.Entry(f1,width=20,textvariable=phone_var)
phone_entrybox.grid(row=5,column=1)

person_var=tk.StringVar()
person_entrybox=ttk.Entry(f1,width=20,textvariable=person_var)
person_entrybox.grid(row=6,column=1)


aadhar_var=tk.StringVar()
aadhar_entrybox=ttk.Entry(f1,width=20,textvariable=aadhar_var)
aadhar_entrybox.grid(row=7,column=1)

city_var=tk.StringVar()
city_entrybox=ttk.Entry(f1,width=20,textvariable=city_var)
city_entrybox.grid(row=10,column=1)





#create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(f1,width=20,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Male","Female","Other")
gender_combobox.current(0)
gender_combobox.grid(row=8,column=1)



state_var=tk.StringVar()
state_combobox=ttk.Combobox(f1,width=20,textvariable=state_var,state="readonly")
state_combobox["values"]=("Andra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
"Gujarat","Haryana","Himachal Pradesh",
"Jammu and Kashmir","Jharkhand","Karnataka","Kerala",
"Madya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
"Nagaland",
"Orissa","Punjab","Rajasthan","Sikkim","Tamil Nadu",
"Telagana","Hyderabad","Tripura","Uttrakhand",
"Uttar Pradesh","West Bengal"

)
state_combobox.current(0)
state_combobox.grid(row=9,column=1)


#radio button
# # student, teacher
# usertype=tk.StringVar()
# radiobtn1=ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
# radiobtn1.grid(row=4,column=0)

# radiobtn2=ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
# radiobtn2.grid(row=4,column=1)

# create check button
checkbtn_var=tk.IntVar( )
checkbtn=ttk.Checkbutton(f1,text="all checked",variable=checkbtn_var)
checkbtn.grid(row=12,columnspan=3)
# # create  button
def action():
    username=name_var.get()
    userphone=phone_var.get()
    userperson=person_var.get()
    usergender=gender_var.get()
    userstate=state_var.get()
    usercity=city_var.get()
    useraadhar=aadhar_var.get()
    # user_type=usertype.get()
    if checkbtn_var.get()==0:
        checked="NO"
    else:
        checked="YES"
        print(username,userphone,userperson,usergender,userstate,usercity,useraadhar,checked)

        with open("project1.txt","a") as f:
            f.write(f"{username},{userphone},{userperson},{usergender},{userstate},{usercity},{useraadhar},{checked}\n")
        
        name_entrybox.delete(0,tk.END)
        phone_entrybox.delete(0,tk.END)                        #FOR DELETE THE VALUE AFTER WE ADD OUR DATA IN OUR PARTICULAR FILE
        person_entrybox.delete(0,tk.END)
        aadhar_entrybox.delete(0,tk.END)
        city_entrybox.delete(0,tk.END)
        

        name_label.configure(foreground="Blue")                    #foe change the colour of our label


submit_button=ttk.Button(f1,text="Submit",command=action)
submit_button.grid(row=13,column=0)


win.mainloop()










