from tkinter import *
# install pillow modile means python image librarry
from PIL import Image, ImageTk

root = Tk()
# width x height "500x500"
root.geometry("500x500")
# max size and min size arugment is weight , height
# root.minsize(300,100) #min size 
# root.maxsize(800,700)  #max size
# label = Label(text="This is kuldeep and this is a GUI") 

# for png image 
# photo = PhotoImage(file="test.png")
# label_image = Label(image=photo) 
# label_image.pack()

# for jpg images
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)
# label_image.pack()

# Label title
root.title("my GUI with kuldeep")


# Important label attributes
"""
text = adds the text
bg = background
fg = foreground
font = sets the fonts   1. font=("arial",15,"bold")   2. font="arial 15 bold"
padx = padding in x
pady = padding in Y
relief = border styling = SUNKEN,RAISED,GROOVE,RIDGE

"""

title_label = Label(text = "sadfsdfasdfasdfasdfasdfasdfhasjkdfh",bg="red",fg="white",padx=25,pady=60,font="arial 15 bold",borderwidth=10,relief=SUNKEN)

# Important pack attributes
""" 
anchor="nw" side nw means north west
side = top(by default),bottom,left,right
fill = X is capital , same as Y is capital
padx = padding in x
pady = padding in y

"""

title_label.pack(side=BOTTOM,anchor="nw",fill=X)

# GUI logic
root.mainloop()


