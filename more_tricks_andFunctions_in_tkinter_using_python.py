from tkinter import *

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

# change GUI icon must have ico extention image
root.wm_iconbitmap("1.ico")

# change background color
root.configure(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="close",command=root.destroy).pack()

# GUI logic
root.mainloop()


