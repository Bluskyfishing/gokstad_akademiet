myList = [2, 3, 4, 6, 7, 8]

with open("liste_med_tall.txt", "w") as readFile:
    for num in myList:    
        readFile.write(f"{num}\n")

with open("liste_med_tall.txt", "r") as readFile:
    data = readFile.read()
    readFile.close()


print("Numbers in file: ")
for i in data:
    if i == "\n":
        continue
    print(i,end=" ")
print()


numbers = list(data)
for i in numbers[::-1]:
    if i == "\n":
        numbers.remove(i)
numbers = map(int, numbers)
numbersList = list(numbers)

for i in range(1,10):
    if i not in numbersList:
        print(i)