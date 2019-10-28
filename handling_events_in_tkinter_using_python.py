from tkinter import *

def kuldeep(event):
    print(f"you clicked on the button at {event.x} , {event.y}")

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Handling Events in kinter")

widget = Button(root,text="click me please")
widget.pack()

widget.bind('<Button-1>',kuldeep)
widget.bind('<Double-1>',quit)

# GUI logic
root.mainloop()


