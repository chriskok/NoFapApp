# from tkinter import *

# for i in range(3):
#     root = Tk()

#     w = Label(root, text="Right-click to display menu", width=40, height=20)
#     w.pack()

#     # create a menu
#     popup = Menu(root, tearoff=0)
#     popup.add_command(label="Next") # , command=next) etc...
#     popup.add_command(label="Previous")
#     popup.add_separator()
#     popup.add_command(label="Home")

#     def do_popup(event):
#         # display the popup menu
#         try:
#             popup.tk_popup(event.x_root, event.y_root, 0)
#         finally:
#             # make sure to release the grab (Tk 8.0a1 only)
#             popup.grab_release()

#     w.bind("<Button-3>", do_popup)

#     b = Button(root, text="Quit", command=root.destroy)
#     b.pack()

#     mainloop()

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

for i in range(3):  
    popupmsg("popup message here!")