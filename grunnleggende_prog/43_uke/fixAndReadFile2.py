import os 
import sys
from functools import reduce

FILENAME = "differentValues.txt"

if not os.path.exists(FILENAME):
    print(f"Couldn't find the file: {FILENAME}")
    sys.exit()

def letterFinder(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

with open(FILENAME, "r") as fNumbers:
    line = fNumbers.readline().rstrip("\n")
    
    while line:
        
        lineSum = 0
        arrNumbers = line.split(",")
        letterRemover = filter(letterFinder,arrNumbers)
        letterRemover = list(letterRemover)
        nums = map(float, letterRemover)
    
        result = reduce(lambda x,y: x + y, nums) 

        line = fNumbers.readline().rstrip("\n")
        print(" + ".join(letterRemover), "=", result)