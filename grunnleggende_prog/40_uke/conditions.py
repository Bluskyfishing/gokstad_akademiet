#1
def numberAttribute(num):
    if int(num) > 0:
        print("Number is positive!")
    elif int(num) < 0:
        print("Number is negative!")
    else:
        print("Number is 0!")

#2
def oddorEven(num):
    if num % 2 == 0:
        print("Number is even!")
    else: 
        print("Number is odd!")

#3
def biggestNumber(num1,num2,num3):
    numbers = (num1,num2,num3)
    return print(max(numbers))

#4
def sameornot(num1,num2):
    if num1 > num2:
        print("First number is bigger!")
    elif num1 < num2:
        print("Second number is bigger!")
    else:
        print("The numbers are equal!")

#5
def grades(char):
    gradesdict = {"A":"Outstanding","B":"Very good","C":"Good","D":"Well","F":"Failed"}
    return print(gradesdict[char])