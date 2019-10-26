# TEST 3
from tkinter import *
import time

root = Tk()

message = StringVar()
quote = "To be, or not to be--that is the question"
quote_array = quote.split(" ")
current_split_quote = quote_array[0]
message.set(current_split_quote)
Instruction = Label(root, textvariable=message,  font='size, 20').pack()

textBox=Text(root, height=2, width=100)
textBox.pack()

# This function is called whenever a key is released
split_counter = 1
def typing(event):
    global split_counter, current_split_quote
    curr_input = textBox.get("1.0", "end-1c") 
    # print(curr_input + " = " + current_split_quote + "?")
    if (current_split_quote in curr_input):
        if (split_counter < len(quote_array)):
            current_split_quote += " " + quote_array[split_counter]
            message.set(current_split_quote)
            split_counter += 1
        else: print("COMPLETE!!!")

textBox.bind('<KeyRelease>', typing) # bind responseEntry to keyboard keys being released, and have it execute the function typing when this occurs


# WINDOW
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()








# TEST 1

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

# TEST 2

# import tkinter as tk
# from tkinter import ttk


# LARGE_FONT= ("Verdana", 12)
# NORM_FONT= ("Verdana", 10)
# SMALL_FONT= ("Verdana", 8)

# def popupmsg(msg):
#     popup = tk.Tk()
#     popup.wm_title("!")
#     label = ttk.Label(popup, text=msg, font=NORM_FONT)
#     label.pack(side="top", fill="x", pady=10)
#     B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
#     B1.pack()
#     popup.mainloop()

# # for i in range(3):  
# #     popupmsg("popup message here!")

# import tkinter as tk
# from overlay import Window

# win = Window()
# label = tk.Label(win.root, text="Window_0")
# label.pack()
# Window.launch()