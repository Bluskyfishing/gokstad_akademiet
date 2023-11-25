import random as rnd 


def main():
    questionAmount = int(input("How many questions do you need?: "))
    FILENAME = input("Write the name of the file: ")
    #file = open(FILENAME, "w")
    with open(FILENAME, "w") as readFile:
        for i in range(questionAmount):
                firstInt = rnd.randint(1,100)
                secondInt = rnd.randint(1,100)
                operatorList = ["-","+"]
                operatorInt = rnd.randint(0,1)
                readFile.write(f"{firstInt} {operatorList[operatorInt]} {secondInt} =\n")
    
    with open(FILENAME, "r") as readFile:
        data = readFile.read()

    solved = input("What name should the solution be?: ")

    with open(solved, "w") as writeFile:
        writeFile.write(data)
        
        writeFile.close()
    
   
            

if __name__ == "__main__":
    main()
