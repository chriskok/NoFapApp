import time
import pyautogui
import tkinter as tk
import time
import csv
import random 
from nudenet import NudeClassifier

BIBLE_CONTENT = []

def main():
    readBible()

    filepath = 'imgs/test.png'
    classifier = NudeClassifier('models/classifier_model')

    # while True:
    for i in range (10):
        print("taking screenshot")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(filepath)

        print("starting classification")
        classified_dict = classifier.classify(filepath)
        print(classified_dict[filepath]['unsafe'])
        if (classified_dict[filepath]['unsafe'] > 0.5):
            fullscreen_popup()
        
        time.sleep(3)

def readBible():
    global BIBLE_CONTENT
    with open('t_asv.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        firstline = True
        for row in readCSV:
            if (firstline): 
                firstline = False
                continue
            if (int(row[1])==1):
                BIBLE_CONTENT.append(row[4])

        print("Bible Content: {}".format(len(BIBLE_CONTENT)))

def getRandomVerse():
    global BIBLE_CONTENT
    return random.choice(BIBLE_CONTENT)

def fullscreen_popup():

    BG_COLOR = "#cc3300"
    LABEL_COLOR = "#ff9966"

    # WINDOW
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.bind("<Escape>", lambda e: root.destroy())
    root.config(bg=BG_COLOR)

    # LABEL
    titleLabel = tk.Label(root, text="THE NO FAP APP", bg=BG_COLOR, fg=LABEL_COLOR,  font=("Ubuntu", 40))
    titleLabel.pack(fill=tk.BOTH, side=tk.TOP, pady=15, padx=60)
    titleLabel2 = tk.Label(root, text="Type out the following as punishment:", bg=BG_COLOR, fg=LABEL_COLOR,  font=("Ubuntu", 20), anchor="n")
    titleLabel2.pack(fill=tk.BOTH, side=tk.TOP, pady=10, padx=60)

    # CANVAS (currently placeholder just for space)
    # TODO: add images that would turn people off?
    canvas = tk.Canvas(root, height=10,bg=BG_COLOR, highlightthickness=0)
    canvas.pack(fill=tk.X, side=tk.TOP, pady=30)

    # MESSAGE TEXT
    message = tk.StringVar()
    quote = getRandomVerse()
    # quote = """Scientists have finally been able to read the oldest biblical text ever found. The 2,000-year-old scroll has been in the hands of archaeologists for decades. But it hasn’t been possible to read it, since it was too dangerous to open the charred and brittle scroll. Scientists have now been able to read it, using special imaging technology that can look into what’s inside. And it has found what was in there: the earliest evidence of a biblical text in its standardised form."""
    quote_array = quote.split(" ")
    current_split_quote = quote_array[0]
    message.set(current_split_quote)
    Instruction = tk.Message(root, textvariable=message,  font=("Helvetica", 32), fg="#fff", bg=BG_COLOR, width=int(root.winfo_screenwidth()) - 100,  anchor="nw", pady=30, padx=60)
    Instruction.pack(fill=tk.X, side=tk.TOP)

    # INPUT TEXT
    textBox=tk.Text(root, height= 5, width=1, font=("Helvetica", 20))
    textBox.pack(fill=tk.X, side=tk.BOTTOM, pady=30, padx=60)

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
            else: 
                print("COMPLETE!!!")
                root.destroy()

    textBox.bind('<KeyRelease>', typing) # bind responseEntry to keyboard keys being released, and have it execute the function typing when this occurs
    textBox.focus_set()  # <-- move focus to this widget

    root.mainloop()


if __name__ == "__main__":
    main()

    # readBible()
    # for i in range(5):
    #     print(i)
    #     fullscreen_popup()