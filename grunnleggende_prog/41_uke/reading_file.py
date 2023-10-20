import os 
import sys

def lineCounterInFile():
    FILENAME = "numbers.csv"

    readFile = open(FILENAME, "r")

    counter = 0 
    for i in readFile:
        counter += 1 
    print("Amount of lines in file:",counter)

def reversedFileFix():
    FILENAME2 = "reversed_numbers.csv"

    with open(FILENAME2, "r") as readFile:
        data = readFile.read()
    
    reversedData = data[::-1]

    with open(FILENAME2, "w") as writeFile:
        writeFile.write(reversedData)
        writeFile.close()


def findAge(gender):

    FILENAME = "persons.csv"

    with open(FILENAME, "r") as readFile:
        line = readFile.readline().rstrip("\n")
        age = 0
        while line:
            elementList = line.split(",")
            for element in elementList:
                if gender in elementList:
                    try:
                        num = int(element)
                        age += num
                    except ValueError:
                        continue
            line = readFile.readline().rstrip("\n")
        return age

ageWomen = findAge("Female")
ageMen = findAge("Male")
print("The total age of Women is:",ageWomen)
print("The total age of Men is:",ageMen)

def findgender(gender):
    FILENAME = "persons.csv"

    with open(FILENAME, "r") as readFile:
        line = readFile.readline().rstrip("\n")
        counter = 0
        while line:
            elementList = line.split(",")
            for element in elementList:
                if gender == element:
                    counter += 1
            line = readFile.readline().rstrip("\n")
        return counter
    
totalWomen = findgender("Female")
totalMen = findgender("Male")
print("The total amount of females:",totalWomen)
print("The total amount of males:",totalMen)