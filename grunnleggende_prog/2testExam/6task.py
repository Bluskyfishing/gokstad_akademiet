names = "Ina, Phillip, Jo, Aleksandria og Anna" 
names = ["Ina","Phillip","Jo","Aleksandria","Anna"]

with open("names.txt", "w") as writeFile: #Make file 
    for name in names:   
        writeFile.write(f"{name}")
        if name != names[-1]:
            writeFile.write("\n")

with open("names.txt", "r") as readFile: #Read and print names to console
    lines = readFile.readlines()
    for line in lines:
        print(line.rstrip())


with open("names.txt", "r") as readFile: #Copy names 
    lines = readFile.readlines()
    names1 = []
    for line in lines:
        names1.append(line)

with open("names2.txt", "w") as writeFile: # Make new file without Jo
    for name in names1:
        if name == "Jo\n":
            continue
        writeFile.write(name)

with open("names2.txt", "r") as readFile: #Get data from 2 file
    lines = readFile.readlines()
    names2 = []
    for line in lines:
        names2.append(line)


for name in names1: #Find difference between file1 and file2
    if name not in names2:
        print("\nName not in file2:",name)