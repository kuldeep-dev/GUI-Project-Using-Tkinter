from tkinter import *
root = Tk()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text )
        screen.update()


root.geometry("540x600")
root.title("Calculator by Kuldeep")
# root.wm_iconbitmap("1.ico") if icon available

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="licida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

# button 9,8,7
f1 = Frame(root,bg="grey")
b = Button(f1,text="9",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="8",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="7",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()

# button 6,5,4
f1 = Frame(root,bg="grey")
b = Button(f1,text="6",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="5",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="4",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()


# button 3,2,1
f1 = Frame(root,bg="grey")
b = Button(f1,text="3",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="2",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="1",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()

# button 0,-,*
f1 = Frame(root,bg="grey")
b = Button(f1,text="0",padx=13,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="-",padx=13,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="*",padx=13,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()

# button /,%,=
f1 = Frame(root,bg="grey")
b = Button(f1,text="/",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="%",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="=",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()


# button c
f1 = Frame(root,bg="grey")
b = Button(f1,text="c",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text=".",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

b = Button(f1,text="00",padx=10,pady=8, font="lucida 25 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f1.pack()

root.mainloop()


