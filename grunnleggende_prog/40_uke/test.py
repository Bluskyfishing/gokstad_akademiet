listOfDict = [{"date": "12/12/2012","Temprature": 12, "State:": "sunny"},
                  {"date": "13/12/2013","Temprature": 13, "State:": "rainy"},
                  {"date": "14/12/2022","Temprature": 14, "State:": "cloudy"},
                  {"date": "15/12/2023","Temprature": 15, "State:": "sunny"}]


#x = listOfDict[0]
#y = list(x.values())
#z= y[1]
#print(z)

#   for i in listOfDict:
            #    print(" ")
            #    for key, value in i.items():
            #        print(key, ":", value)


#secondKeyPairs = []
#thirdKeypairs = []

def prettyPrintOfDict(row,dict):
    KeyPairs = []

    for i in dict:
        Key, Value = list(i.items())[row]
        KeyPairs.append(Key)
        KeyPairs.append(Value)
    for i in range(0, len(KeyPairs), 2):
        print(str(KeyPairs[i]).center(10), ":" ,str(KeyPairs[i+1]).center(10), "| " ,end="")

prettyPrintOfDict(0,listOfDict)
print()
prettyPrintOfDict(1,listOfDict)
print()
prettyPrintOfDict(2,listOfDict)
print()


def del_liste(liste, n=6):
    for i in range(0, len(liste), n):
        yield liste[i:i + n]

# Eksempel på bruk:
min_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for delen in del_liste(min_liste, 6):
    print(delen)


#for i in listOfDict:
#    for key, value in i.items():
#        pairList = [key,value]
#        pairtuple = tuple(pairList)
#        firstKeyPairs.append(pairtuple)
#        break
#print(firstKeyPairs)