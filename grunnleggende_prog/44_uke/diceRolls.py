import random as rnd
import matplotlib.pyplot as plt

DICESTAT = [0] * 6

def readPositiveNumber():
    rollDecide = 0 

    while rollDecide <= 0:
        try:
            rollDecide = int(input("How many times do you want to throw the dice?: "))
            if rollDecide <= 0:
                print("Number has to be positive! Try again!")
                continue
            
        except ValueError as valErr:
            print("Not a valid format, input a positive number!", valErr)
    return rollDecide

    
def runSimulation(amountRolls):
    for i in range(amountRolls):
        roll = rnd.randint(1,6)
        print("Rolled a:",roll)
        index = roll - 1
        DICESTAT[index] += 1
        print("All dice rolls:",DICESTAT)
        

def viewStats(amountRolls): #missing amount, % for loop 
    labelList = ["One","Two","Three","Four","Five","Six"]
    #xValues = []
    #for i in range(len(labelList)):
    #    x = f"{labelList[i]}:({(DICESTAT[i])})\n{(DICESTAT[i]/amountRolls)*100:.1f} %"
    #    xValues.append(x)
    
    xValues = [f"{labelList[index]}:({(DICESTAT[index])})\n{(DICESTAT[index]/amountRolls)*100:.1f} %" for index in range(len(labelList))]
    
    plt.xlabel("Dicerolls distribution")
    plt.ylabel(f"Amount of rolls: {amountRolls}")
    plt.bar(xValues, DICESTAT)
    plt.show()


def main():
    AmountOfSimulations = readPositiveNumber()
    runSimulation(AmountOfSimulations)
    viewStats(AmountOfSimulations)

if __name__ == "__main__":
    main()