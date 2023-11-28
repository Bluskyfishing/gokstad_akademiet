name = input("Write your name: ")
print("Hello,",name)


num = int(input("Write a number: "))
if num > 0:
    print(num,"is possitve!")
elif num < 0:
    print(num,"is negative!")
else:
    print("num is 0")


num = int(input("Write a number: "))
print(num*2)


txt = input("Write some text: ")
print(txt[::-1])