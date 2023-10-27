import os
import sys

FILENAME = "persons.csv"
WRITE_FILENAME = "age.txt"

with open(FILENAME, "r", encoding="utf-8") as readFile:
    unsortedList = []
    for line in readFile:
        personArr = line.rstrip('\n').split(',')
        firstName, lastName, age, gender = personArr
        unsortedList.append([age,firstName,lastName,gender])
    unsortedList[1:] = sorted(unsortedList[1:])

with open(WRITE_FILENAME, "w", encoding="utf-8") as writeFile:
    for i in unsortedList:
        writeFile.write(str(i))
        writeFile.write("\n")