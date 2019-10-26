import pyautogui
from nudenet import NudeClassifier
import time
classifier = NudeClassifier('models/classifier_model')

def main():
    # while True:
    # for i in range (10):
    #     print("taking screenshot")
    #     myScreenshot = pyautogui.screenshot()
    #     myScreenshot.save('imgs/test.png')

    #     print("starting classification")
    #     classifier = NudeClassifier('models/classifier_model')
    #     print(classifier.classify('imgs/test.png'))

    filepath = 'imgs/test.png'
    print("starting classification")
    classified_dict = classifier.classify('imgs/test.png')
    print(classified_dict)
    print(classified_dict[filepath]['unsafe'])

if __name__ == "__main__":
    main()