import os
import sys

FILENAME = "test.txt"
WRITE_FILENAME = "test.log"

if not os.path.exists(FILENAME) and not os.path.isfile(FILENAME):
    print(f"Finner ikke filen {FILENAME} -avslutter")
    sys.exit()

with open(FILENAME, "r", encoding="utf-8") as readFile:
    for line in readFile:
        print(line)

with open(WRITE_FILENAME, "w", encoding="utf-8") as writeFile:
    for n in range(1,101):
        writeFile.write(f"Number is {n}\n")