numlist = [3,5,9,10,11]

for i in numlist:
    print(i)
    if i >= 10:
        print("Number is higher then 10.")
    elif i <= 5:
        print("Number is lower than 5.")
    else:
        print("Number is inbetween 5 and 10.")

for i in range(len(numlist)):
    print(f"index={i}, value={numlist[i]}")

index = 0
while True:
   print(f"index={index}, value={numlist[index]}")
   index += 1
   if index == len(numlist):
       break

total = 0
for i in numlist:
    total += i
print("total sum is:",total)