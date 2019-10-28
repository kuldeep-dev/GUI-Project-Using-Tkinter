from tkinter import *

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set("Ready now")

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN ,anchor="w")
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="upload",command=upload).pack()

# GUI logic
root.mainloop()


