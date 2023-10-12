def addData(date,temprature,stateOfWeather):
    newdata = {"Date": date,"Temperature": temprature, "State:": stateOfWeather}
    listOfDict.append(newdata)
    return listOfDict

def devideList(list,n=6):
    for i in range(0, len(list), n):
        yield list[i:i + n]
    
def prettyPrintOfDict(dict):
    for index in range(0,3):
        keypairs = []
        for i in dict:
            Key, Value = list(i.items())[index]
            keypairs.append(Key)
            keypairs.append(Value)
        for i in range(0, len(keypairs), 2):
                print(str(keypairs[i]).center(10), ":" ,str(keypairs[i+1]).center(10), "|" ,end="")
        print()

def mainMenu():
    global listOfDict 
    listOfDict = [{"Date": "12/12/2012","Temprature": 12, "State:": "sunny"},
                  {"Date": "13/12/2013","Temprature": 13, "State:": "rainy"},
                  {"Date": "14/12/2022","Temprature": 14, "State:": "cloudy"},
                  {"Date": "15/12/2023","Temprature": 15, "State:": "sunny"}]

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

            addData(date,temp,state)
        if inp == "b":
            if len(listOfDict) > 6:
                for part in devideList(listOfDict, 6):
                    print()
                    prettyPrintOfDict(part)
            else:
                prettyPrintOfDict(listOfDict)
            print(listOfDict)
        if inp == "c":
            averageTempList = []
            total = 0

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
        if inp == "d":
            print("\nQuitting program!")
            break

mainMenu()


{'Date': '12/12/2001', 'Temperature': 12, 'State:': 'sunny'}
{'Date': '15/12/2023', 'Temprature': 15, 'State:': 'sunny'}