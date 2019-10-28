import csv
import random 
content = []

with open('t_asv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    firstline = True
    for row in readCSV:
        if (firstline): 
            firstline = False
            continue
        if (int(row[1])==1):
            content.append(row[4])

    print(len(content))

def getRandomVerse():
    return random.choice(content)

for i in range(10):
    print(getRandomVerse())