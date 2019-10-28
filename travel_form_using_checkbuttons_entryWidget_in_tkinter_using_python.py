from tkinter import *

root = Tk()

def getvals():
    print("sumitting form")
    print(f"{namevalue.get(),phonevalue.get() ,gendervalue.get(),emergencyvalue.get(), paymentmodevalue.get() ,foodservicevalue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get() ,gendervalue.get(),emergencyvalue.get(), paymentmodevalue.get() ,foodservicevalue.get()}\n")

# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

Label(root,text="welcome to kuldeep Travels",font="comicsansms 13 bold",pady=5).grid(row=0,column=3)

# Text for our Form
name = Label(root,text="Name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
emergency = Label(root,text="Emergency Contact")
paymentmode = Label(root,text="Payment Mode")

# Pack form using grid method
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

# Tkinter variables for string entries 
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#  Entries for a form
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)

# packing the entry
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# checkbox and packing
foodservice = Checkbutton(text="want to prebook your meal", variable=foodservicevalue)
foodservice.grid(row=6,column=3)

# button nad packing and assign a command
Button(text="Submit",command=getvals).grid(row=7,column=3)

# GUI logic
root.mainloop()


