from tkinter import *

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

def hello():
    print("Hello Tkinter buttons")

def name():
    print("name Tkinter")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT,padx=25)

b2 = Button(frame,fg="red",text="Tell me name",command=name)
b2.pack(side=LEFT,padx=25)

b3 = Button(frame,fg="red",text="Print Now")
b3.pack(side=LEFT,padx=25)

b4 = Button(frame,fg="red",text="Print Now")
b4.pack(side=LEFT,padx=25)

# GUI logic
root.mainloop()


