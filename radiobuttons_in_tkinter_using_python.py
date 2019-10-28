from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

var = IntVar()
# var.set(1)
Label(root,text="what is your subject?",justify=LEFT,padx=14,font="lucida 19 bold").pack()

def order():
    tmsg.showinfo("Subjects",f"your subject is {var.get()}")

# normal
# radio = Radiobutton(root,text="Math",padx=14,variable=var,value=1).pack(anchor="w")
# radio = Radiobutton(root,text="Science",padx=14,variable=var,value=2).pack(anchor="w")
# radio = Radiobutton(root,text="English",padx=14,variable=var,value=3).pack(anchor="w")
# radio = Radiobutton(root,text="Hindi",padx=14,variable=var,value=4).pack(anchor="w")

# using for loop
list1=["math","science","english","hindi"]
var = StringVar()
var.set("radio")


for item in list1:
    radio = Radiobutton(root,text=f"{item}",variable=var,value=f"{item}",font="licida 9").pack(anchor="w")

Button(text="Your subject",command=order).pack()

# GUI logic
root.mainloop()


