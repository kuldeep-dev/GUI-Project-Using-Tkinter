from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

def myfunc():
    print("this is a function")

def help():
    # print("I will help you")
    a =tmsg.showinfo("Help","Kuldeep will help you")
    # print(a)

def rate():
    print("rate us")
    value = tmsg.askquestion("was your experience","How was your experience")
    # print(value)
    if value == "yes":
        msg = "Great,for your support"
    else:
        msg = "Tell us"
    tmsg.showinfo("Experience",msg)        


def kuldeep():
    ans = tmsg.askretrycancel("Kuldeep friend","sorry kuldeep")
    if ans:
        print("Please not retry")
    else:
        print("best for cancel")    


mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)


m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Friend Kuldeep",command=kuldeep)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)

# GUI logic
root.mainloop()


