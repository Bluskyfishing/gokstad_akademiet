listNum = []

for n in range(1,21):
    listNum.append(n)

print(*listNum) # to get out of list in print

listNumComp = [n for n in range(1, 21)]
print(*listNumComp)

evenNum = [n for n in range(0, 21) if n % 2 == 0]
print(*evenNum)

squaredNum = [n*n for n in range(0, 21)]
print(*squaredNum)

