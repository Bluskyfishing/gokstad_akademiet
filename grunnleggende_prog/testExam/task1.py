name = input("Write your name: ")
print("Hello",name)

while True:
    num = input("Write a number: ")
    try:
        convertion = int(num)
        break
    except ValueError:
        print("Input has to be a number!")

num = int(input("Choose a number: "))

if num %2 == 0:
    print(num,"Is an even number")
else: 
    print(num, "Is an odd number!")