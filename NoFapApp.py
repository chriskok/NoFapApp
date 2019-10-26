import pyautogui
# from nudenet import NudeClassifier
import time
# classifier = NudeClassifier('models/classifier_model')

from tkinter import *
import time

def main():
    filepath = 'imgs/test.png'

    # while True:
    for i in range (10):
        print("taking screenshot")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(filepath)

        print("starting classification")
        classified_dict = classifier.classify(filepath)
        print(classified_dict[filepath]['unsafe'])

def fullscreen_popup():
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
        nonlocal split_counter, current_split_quote
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


if __name__ == "__main__":
    # main()
    fullscreen_popup()