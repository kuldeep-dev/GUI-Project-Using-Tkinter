from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

# myslider = Scale(root,from_=0,to=100)
# myslider.pack()

def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited",f"we have credited {myslider2.get()} dollars to your bank account")

Label(root,text="How many dollars do you want").pack()
myslider2 = Scale(root,from_=0,to=100 , orient=HORIZONTAL,tickinterval=50)
myslider2.set(20)
myslider2.pack()
Button(root,text="Get Dollars", pady=10, command=getdollar).pack()

# GUI logic
root.mainloop()


