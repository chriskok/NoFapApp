from tkinter import *

root = Tk()

v = StringVar()

hello = Label(text=v)
hello.grid(sticky=W)

mynameisLabel = Label(text="My name is:")
mynameisLabel.grid(row=1, sticky=W)

responseEntry = Text(width=40, height=1)
responseEntry.grid(row=2, sticky=E)

conclusionText = Text(width=40, height=5)
conclusionText.insert(END, "Ah, so your name is ?")
conclusionText.grid(row=3, columnspan=2)

# This function is called whenever a key is released
def typing(event):
    name = responseEntry.get("1.0",END) # Get string of our name
    conclusionText.delete("1.0", END)   # delete the text in our conclusion text widget
    conclusionText.insert(END, "Ah, so your name is " + name[:-1] + "?") # Update text in conclusion text widget. NOTE: name ends with a new line
    v.set(name[:-1])

responseEntry.bind('<KeyRelease>', typing) # bind responseEntry to keyboard keys being released, and have it execute the function typing when this occurs

root.mainloop()