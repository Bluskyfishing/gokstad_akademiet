import os 
#import sys 
#from context import uke
#print("test")
#from 41_uke import lineCounterInFile
#sys.path.insert(0, '/home/amninder/Desktop/Folder_2')

FILENAME = "ensolskinnsdag.txt"

def lineCounterInFile(fileName: list):
    readFile = open(fileName, "r")

    counter = 0 
    for i in readFile:
        counter += 1 
    print("Amount of lines in file:",counter)

lineCounterInFile(FILENAME)

def wordCounterInFile(fileName: list):
    with open(FILENAME, "r") as readFile:
        lines = readFile.readlines()
        counter = 0

        for line in lines:
            lineList = line.split()
            for word in lineList:
                print(word)
                for letter in word:
                    if letter.isdigit() or letter == "[" or letter == "]":
                        continue
                counter += 1
        print("Amount of words in file:", counter)

wordCounterInFile(FILENAME)