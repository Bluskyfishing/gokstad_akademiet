import os 
import sys

FILENAME = "differentValues.txt"

if not os.path.exists(FILENAME):
    print(f"Couldn't find the file: {FILENAME}")
    sys.exit()

with open(FILENAME, "r") as fNumbers:
    line = fNumbers.readline().rstrip("\n")
    
    while line:
       
        lineSum = 0
        arrNumbers = line.split(",")
        for i in range(len(arrNumbers)): 
            numberStr = arrNumbers[i]
            try:
                nr = float(numberStr)
                lineSum += nr
            except ValueError:
                arrNumbers[i] = "0"

        line = fNumbers.readline().rstrip("\n")
        print(" + ".join(arrNumbers), "=", lineSum)