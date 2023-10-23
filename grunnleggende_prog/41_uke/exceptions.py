try:
    str_nr = input("Write a number: ")
    nr = int(str_nr)
    print(f"The double of the number is {nr*2}")
except ValueError as valErr:
    print(f"Got a problem with input as a number: {valErr}")

try: 
    a = int(input("read number a: "))
    b = int(input("read number b: "))

    print(f"{a}/{b}={a/b}")
except ValueError as valErr:
    print(f"Got a problem with input as a number: {valErr}")
except ZeroDivisionError as zeroDivErr:
    print(f"Can't devide by 0: {zeroDivErr}")
except Exception as ex:
    print(ex)


FILENAMEDummy = "test.txt"

try:
    with open(FILENAMEDummy, "r", encoding="utf-8") as fileRead:
        for line in fileRead:
            print(line)
except FileNotFoundError as fileNotFoundErr:
    print(f"Couldnt find file: {fileNotFoundErr}")
except IOError as ioErr:
    print(f"Couldnt read file: {ioErr}")
except Exception as ex:
    print(ex)