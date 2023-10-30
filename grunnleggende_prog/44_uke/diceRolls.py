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
        index = idx = roll - 1
        DICESTAT[index] += 1
        

def viewStats(amountRolls):
    xValues = [f"One: ({DICESTAT[0]})\n{(DICESTAT[0]/amountRolls)*100:.1f} %",
               "Two",
               "Three",
               "Four",
               "Five",
               "Six"]

    plt.xlabel("Dicerolls")
    plt.ylabel("Amount of rolls")
    plt.bar(xValues, DICESTAT)
    plt.show()


def main():
    AmountOfSimulations = readPositiveNumber()
    runSimulation(AmountOfSimulations)
    viewStats(AmountOfSimulations)

if __name__ == "__main__":
    main()