import random as rnd 

def questionMaker(fileName, questionAmount):
    with open(fileName, "w") as writeFile:
        for i in range(questionAmount):
                mathLength = rnd.randint(2,7)
                for itere in range(mathLength):
                    num = rnd.randint(1,101)
                    operatorInt = rnd.randint(0,1)
                    operatorList = ["-","+"]
                    writeFile.write(f"{num} ")
                    if itere == mathLength -1:
                        continue
                    writeFile.write(f"{operatorList[operatorInt]} ")
                writeFile.write("=")
                writeFile.write("\n") #Vil remove siste newLine

def copyFile(inputFile, outputFile):
    with open(inputFile, "r") as readFile:
        data = readFile.read()

    with open(outputFile, "w") as writeFile:
        writeFile.write(data)
        writeFile.close()

def mathSolver(fileName):
    with open(fileName, "r") as readFile:
        expressions = []
        results = []
        for line in readFile.readlines():
            lineList = line.split()
            expressions.append(lineList)
            total = int(lineList[0])
            previousValue = None
            for strNum in lineList[1:]:
                intNum = 0
                if strNum == "=":
                    continue
                try:
                    intNum = int(strNum)
                except ValueError:
                    previousValue = strNum
                    continue
                if previousValue == "+":
                    total += intNum
                elif previousValue == "-":
                    total -= intNum
            results.append(total)
        readFile.close()

    return expressions, results


FILENAME = "regnestykker.txt"
questionAmount = rnd.randint(1,10) # 10 HUSK! endre tilbake 
SOLVEDFILE = "regnestykker_løsning.txt"

questionMaker(FILENAME, questionAmount)
copyFile(FILENAME, SOLVEDFILE)
mathSolver(SOLVEDFILE)

solverExpressions, solverResults = mathSolver(SOLVEDFILE) #Få det siste i en func? Lage en stor func?
for i in range(len(solverExpressions)):
    solverExpressions[i].append(solverResults[i])

with open(SOLVEDFILE, "w") as writeFile:
    for itemList in solverExpressions:
        for item in itemList:
            writeFile.writelines(str(item))
            writeFile.writelines(" ")
        writeFile.writelines(" \n")
    writeFile.close() 



#def mathQuestionBuilder(inputFile, outputFile, questionAmount):
#    questionMaker(inputFile, questionAmount)
#    copyFile(inputFile, outputFile)
#    mathSolver(outputFile)