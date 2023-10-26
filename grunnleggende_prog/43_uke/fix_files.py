import os 

FILENAME = "reversedFile.txt"

with open(FILENAME, "r") as readFile:
    lines = readFile.readlines()

reversed_lines = []
for line in lines:
    words = line.split()
    reversed_words = words[::-1]  
    reversed_line = " ".join(reversed_words)
    reversed_lines.append(reversed_line)
    reversed_lines.append("\n")
    
with open(FILENAME, "w") as writeFile:
    writeFile.writelines(reversed_lines)

FILENAME2 = "stutter_file.txt"

with open(FILENAME2, "r") as readFile:
    lines = readFile.readlines()
    outputLines = []
    for line in lines:
        lineList = line.split()
        prevValue = None
        newLine = []  
        for word in lineList:
            if word != prevValue:
                newLine.append(word)
                prevValue = word
            print(word)
        outputLines.append(" ".join(newLine))
        outputLines.append("\n")

with open(FILENAME2, "w") as writeFile:
    writeFile.writelines(outputLines)