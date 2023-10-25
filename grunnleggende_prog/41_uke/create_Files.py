import os 
import random as rnd 

currentDir = os.getcwd()
newFolder = os.path.join(currentDir, "Files_Created")

if not os.path.exists("Files_Created"):
    os.mkdir("Files_Created")
    print("Made new folder:",newFolder)

for _ in range(100):
    year = rnd.randint(2015, 2023)
    month = rnd.randint(1,12)
    fileName = f"{year}-{month:0>2}.txt"

    yearDirectory = str(year)
    parentDir = "/home/fish_fast/Documents/gokstad_akademiet/grunnleggende_prog/41_uke/Files_Created"
    yearPath = os.path.join(parentDir,yearDirectory)
    
    if not os.path.isdir(yearPath):
        os.mkdir(yearPath)
        print("Created folder:", str(year))

    monthDirectory = str(month)
    monthPath = os.path.join(parentDir, yearDirectory, monthDirectory)

    if not os.path.isdir(monthPath):
        os.mkdir(monthPath)
        print("Created folder:", str(month))
        
        with open(os.path.join(monthPath,fileName), "w"):
            print(f"Created file {fileName}")
            continue