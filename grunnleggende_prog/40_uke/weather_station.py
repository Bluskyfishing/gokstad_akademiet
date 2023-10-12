def addData(date,temprature,stateOfWeather):
    newdata = {"date": date,"Temprature": temprature, "State:": stateOfWeather}
    listOfDict.append(newdata)
    return listOfDict
        
def mainMenu():
    global listOfDict 
    listOfDict = [{"date": "12/12/2012","Temprature": 12, "State:": "sunny"},
                  {"date": "13/12/2013","Temprature": 13, "State:": "rainy"},
                  {"date": "14/12/2022","Temprature": 14, "State:": "cloudy"},
                  {"date": "15/12/2023","Temprature": 15, "State:": "sunny"}]

    while True:
        inp = input("a. Add weather data\nb. Show saved information.\nc. Analyze data\nd. Quit\nInput: ").lower()
        print(" ")

        if inp == "a":

            try:
                date = (input("Enter date (d/m/y: )"))
                temp = int(input("Enter tempratrue (in Celcius): "))
                state = input("Enter state of weather (sunny/rainy/cloudy): ")
            except ValueError:
                print("Invalid type please try again!")
                continue

            addData(date,temp,state)
            print(listOfDict)
        if inp == "b":
            for i in listOfDict:
                print(i)
        if inp == "c":
            x = listOfDict[0]
            y = list(x.values())
            z= y[1]
        if inp == "d":
            print("Quitting program!")
            break

mainMenu()