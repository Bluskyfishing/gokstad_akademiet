import random as rnd 

myList = []

for i in range(10):
    myList.append(rnd.randint(0,10))

print(myList)


total = 0 
for i in myList:
    total += i 
print(total)
print(sum(myList))


if 6 in myList:
    print(6, "in list")


for num in myList[::-1]:
    if num %2 == 0:
        myList.remove(num)
print(myList)