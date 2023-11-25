import random as rnd 

randomList = []

for i in range(5):
    randomNum = rnd.randint(1,101)
    randomList.append(randomNum)
print(randomList)

randomList.sort()
print(randomList)

random100List = []
for i in range(1,101):
    randomNum = rnd.randint(1,201)
    random100List.append(randomNum)

print(random100List)

for i in random100List[::-1]:
    if i > 100 or i %3 == 0:
        random100List.remove(i)
print(random100List)