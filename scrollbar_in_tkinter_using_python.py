from tkinter import *

root = Tk()
# width x height "500x500"
root.geometry("500x500") #default window

# Label title
root.title("my GUI with kuldeep")

# for connect scrollbar to a widget
"""
1. widget (y scroll command = scrollbar.set)
2. scrollbar.config(commandwidget.yview) 
"""

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root,yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"item {i}")

# listbox.pack(fill=BOTH,padx=22)
text = Text(root,yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
# scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview)
# GUI logic
root.mainloop()


