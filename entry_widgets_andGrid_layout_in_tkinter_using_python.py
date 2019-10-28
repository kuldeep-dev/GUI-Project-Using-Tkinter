from tkinter import *


def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

# Grid layout

user = Label(root,text="Username")
password = Label(root,text="Password")

user.grid()
password.grid(row=1)

# variable classes in tkinter
# Boolean var , DoubleVar , IntVar , StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()



# GUI logic
root.mainloop()


