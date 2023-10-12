#1
def stop():
    while True:
        inp = input("Write something! (Write 'stop' to stop.)\n")
        if inp == "stop":
            break

#2
def countertoTen():
    counter = 1
    while True:
        print(counter)
        if counter == 10:
            break
        counter += 1

#3
def sumofNum():
    num = int(input("Write a number: "))
    counter = 1
    result = 0
    while True:
        print(counter)
        result += counter
        if counter == num:
            break
        counter += 1
    print(result)

#4 
def productofNum(num):  # Huh?
    product = 1
    iteration = 1
    while iteration <= num:
        product *= iteration
        iteration += 1
    return product
res = productofNum(4)
print(res)

#5
def divisibleby17():
    counter = 1000
    while True:
        counter += 1
        if counter%17 == 0:
            print(counter)
            break

#6
def averageinList(list):
    total = 0
    index = 0
    while index < len(list):
        total += list[index]
        index += 1
    return total/len(list)

listnumbers = [1,2,3,4,5]
#res = averageinList(listnumbers)
#print("The average of the list is :",res)

#7
def biggestNumber(list):
    index = 0
    biggest = list[0]
    while index != len(list):
        if list[index] > biggest:
            biggest = list[index]
        index += 1
    return(biggest)
    
#res = biggestNumber(listnumbers)
#print("The biggest number in the list is:",res)

#8
def smallestNumber(list):
    index = 0 
    smallest = list[index]
    while index != len(list):
        if smallest > list[index]:
            smallest = list[index]
        index += 1
    return(smallest)

#res = smallestNumber(listnumbers)
#print("The smallest number in the list is:",res)

#9
import random as r

def guessRandomNum():
    number = r.randint(0,10)
    guess = 0
    print("The number to guess is: ",number)
    while number != guess:
        print("PC guess:",guess)
        guess += 1
    print("The number was",guess)

#10
def squared(num):
    counter = 1
    while True:
        print(counter * counter)
        counter += 1
        if counter == num:
            break