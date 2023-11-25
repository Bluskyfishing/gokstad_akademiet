import random as rnd 

def questionMaker(fileName, questionAmount):
    with open(fileName, "w") as writeFile:
        for i in range(questionAmount):
            mathLength = rnd.randint(2,7)
            for number in range(mathLength):
                num = rnd.randint(1,101)
                operatorInt = rnd.randint(0,1)
                operatorList = ["-","+"]
                writeFile.write(f"{num} ")
                if number == mathLength -1:
                    continue
                writeFile.write(f"{operatorList[operatorInt]} ")
            writeFile.write("=")
            if i == questionAmount -1:
                continue
            writeFile.write("\n")

def copyFile(file, outputFile):
    with open(file, "r") as readFile:
        data = readFile.read()

    with open(outputFile, "w") as writeFile:
        writeFile.write(data)
        writeFile.close()

def mathSolver(file):
    with open(file, "r") as readFile:
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

def solutionPrint(file):
    solverExpressions, solverResults = mathSolver(file)

    for i in range(len(solverExpressions)):
        solverExpressions[i].append(solverResults[i])

    with open(file, "w") as writeFile:
        for itemList in solverExpressions:
            for item in itemList:
                writeFile.writelines(str(item) )
                writeFile.writelines(" ")
            if itemList == solverExpressions[-1]:
                continue
            writeFile.writelines("\n")
        writeFile.close() 

def mathQuestionBuilder(file, questionAmount, outputFile, ):
    questionMaker(file, questionAmount)
    copyFile(file, outputFile)
    mathSolver(file)
    solutionPrint(outputFile)

FILENAME = "regnestykker.txt"
questionAmount = rnd.randint(1,10) 
SOLVEDFILE = "regnestykker_løsning.txt"
mathQuestionBuilder(FILENAME, questionAmount, SOLVEDFILE)