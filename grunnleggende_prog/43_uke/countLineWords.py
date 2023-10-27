import os 

FILENAME = "ensolskinnsdag.txt"

def lineCounterInFile(fileName: list):
    readFile = open(fileName, "r")
    counter = 0 

    for i in readFile:
        counter += 1 
    return counter

def wordCounterInFile(fileName: list):
    with open(fileName, "r") as readFile:
        lines = readFile.readlines()
        counter = 0

        for line in lines:
            lineList = line.split()
            for word in lineList:
                if word.startswith("[") or word.endswith("]"):
                    continue
                counter += 1
        return counter

print("Amount of lines in file:",lineCounterInFile(FILENAME))
print("Amount of words in file:", wordCounterInFile(FILENAME))