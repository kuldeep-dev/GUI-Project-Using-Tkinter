from tkinter import *
import tkinter.messagebox as tmsg



def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i = 0

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of  a list box")

Button(root,text="Add item", command=add).pack()

# GUI logic
root.mainloop()


