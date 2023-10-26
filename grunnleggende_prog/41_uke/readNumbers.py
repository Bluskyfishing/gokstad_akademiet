import os 
import sys

FILENAME = "numbers.csv"

if not os.path.exists(FILENAME):
    print(f"Couldn't find the file: {FILENAME}")
    sys.exit()

with open(FILENAME, "r") as fNumbers:
    line = fNumbers.readline().rstrip("\n")
    while line:
        lineSum = 0
        arrNumbers = line.split(",")
        for numberStr in arrNumbers:
            if numberStr.isdigit():
                nr = int(numberStr)
                lineSum += nr

        line = fNumbers.readline().rstrip("\n")
        print(" + ".join(arrNumbers), "=", lineSum)