def addData(list,date,temp,stateOfWeather):
    newdata = {"Date":date,"Temp":temp, "State":stateOfWeather}
    list.append(newdata)

def devideList(list,n=3):
    for i in range(0, len(list), n):
        yield list[i:i + n]
    
def prettyPrintOfDict(dict):
    for index in range(0,3):
        keypairs = []
        for i in dict:
            key, value = list(i.items())[index]
            keypairs.append(key)
            keypairs.append(value)
        for i in range(0, len(keypairs), 2):
                key = str(keypairs[i]).center(10)
                value = str(keypairs[i+1]).center(10)
                print(key, ":", value, "|",end="")
        print()

def mainMenu():
    listOfDict = []

    while True:
        inp = input("\na. Add weather data.\nb. Show saved information.\nc. Analyze data.\nd. Quit.\nInput: ").lower()
        
        if inp == "a":
            try:
                date = (input("\nEnter date (d/m/y): "))
                temp = int(input("Enter temperature (in Celcius): "))
                state = input("Enter state of weather (sunny/rainy/cloudy): ")
            except ValueError:
                print("Invalid type! Temperature must be a number. Please try again!")
                continue

            addData(listOfDict,date,temp,state)

        if inp == "b":
            if len(listOfDict) > 3:
                for part in devideList(listOfDict, 3):
                    print()
                    prettyPrintOfDict(part)
            else:
                prettyPrintOfDict(listOfDict)

        if inp == "c":
            averageTempList = []
            total = 0
            try: 
                for i in range(len(listOfDict)):
                    elementInList = listOfDict[i]
                    valuesFromList = list(elementInList.values())
                    averageTempList.append(valuesFromList[1])
                for i in averageTempList:
                    total += i

                averageTemp = total/len(averageTempList)
                highestTemp = max(averageTempList)
                lowestTemp = min(averageTempList)
                print(f"\n---Statistics from data collected---\nAverage Temperature:{averageTemp}")
                print(f"Highest Temperature:{highestTemp}\nLowest Temperature:{lowestTemp}")
            except ZeroDivisionError:
                print("No data is stored! Add some data to be analysed!")

        if inp == "d":
            print("\nQuitting program!")
            break

mainMenu()