import os 
import random as rnd 

currentDir = os.getcwd()

newFolder = os.path.join(currentDir, "Test")
if not os.path.exists("Test"):
    os.mkdir("Test")
    print("Made new folder:",newFolder)

for _ in range(100):
    year = rnd.randint(2015, 2023)
    month = rnd.randint(1,12)
    fileName = f"{year}--{month:0>2}.txt"
    with open(os.path.join(newFolder,fileName), "w"):
        print(f"Created file {fileName}")
