#1
def counter():
    for i in range(1,101):
        print(i)

#2
def evenNumbers():
    for i in range(1,101):
        if i % 2 == 0:
            print(i)
        else:
            continue

#3
def oddNumbers():
    for i in range(1,100):
        if i % 2 != 0:
            print(i)
        else:
            continue

#4
def multiplicationTable():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j)

#5 
def sumofNumbers(num): 
    sumnum = 0
    for i in range(1,num):
        print(i)
        sumnum += i
    return sumnum  
#res = sumofNumbers(4)
#print(res)

#6
def multiplicationNumbers(num):
    total = 1 
    for i in range(1,num):
        total *= i
        print(total)
    return total

#7 
def average(list):
    sumnum = 0
    for i in list:
        sumnum += i
    return sumnum / len(list)

listofNumbers = [1,2,3,4,5]
#res = average(listofNumbers)
#print(res)

#8
def biggestNumber(list):
    biggest = list[0]
    for i in list:
        print(i)
        if i > biggest:
            biggest = i
    return biggest

#res = biggestNumber(listofNumbers)
#print(res)

#9
def smallestNumber(list):
    smallest = list[0]
    for i in list:
        print(i)
        if i < smallest:
            smallest = i
    return smallest

#res = smallestNumber(listofNumbers)
#print(res)

#10
def squared(num):
    for i in range(1,num):
        print(i*i)
    return num*num

#res = squared(5)
#print(res)