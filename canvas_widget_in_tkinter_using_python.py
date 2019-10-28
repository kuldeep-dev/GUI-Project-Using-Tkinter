from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas")
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# the line goes from the point X1,Y1 to X2,Y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="green")

#  to create a rectangle specify parameters in this order cordinates of top left and cordinates of bottom right
can_widget.create_rectangle(3,5,700,300,fill="blue")

can_widget.create_text(200,200,text="kuldeep")

can_widget.create_oval(344,233,244,355)

# GUI logic
root.mainloop()


