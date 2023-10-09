#1
def sumOfNumbers(num1,num2):
    return num1 + num2

#2 
def productOfNumbers(num1,num2):
    return num1 * num2

#3
def quotientOfNumbers(num1,num2):
    return num1/num2

#4 
def sumOfList(list):
    total = 0 
    for i in list:
        total += i
    return total

#5 
def productInList(list):
    total= 1 
    for i in list:
        total *= i
    return total
    
#6
def biggestNumber(list):
    biggest = list[0]
    for i in list:
        if i > biggest:
            biggest = i 
    return biggest

#7 
def smallestNumber(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i 
    return smallest

#8
def average(list):
    total = 0 
    for i in list:
        total += i 
    return total/len(list)

#9
def addingInList(list,num):
    newlist = []
    for i in list:
        newlist.append(i * num)
    return newlist

#10
def reverseString(txt):
    return txt[:: -1]