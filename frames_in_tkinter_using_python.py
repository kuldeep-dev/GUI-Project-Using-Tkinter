from tkinter import *

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

f1 = Frame(root,bg="red",borderwidth=6)
f1.pack(side=LEFT)

l = Label(f1,text="Project using Tkinter")
l.pack()

# GUI logic
root.mainloop()


