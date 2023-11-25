animalList = ["Dog","Cat","Capybara","Shark","Whale"]

for animal in animalList:
    print(animal)

animalNames = ["Petter","Ola","Satoru","Steinar","Mordi"]

for animal in range(len(animalList)):
    print(animalNames[animal],"is a",animalList[animal])

print("First element:", animalList[0],
      "Last element:", animalList[-1])

print(list(reversed(animalList)))

namesAndAnimals = zip(animalList,animalNames)
animalDict = dict(namesAndAnimals)

for animal, name in animalDict.items():
    print(name,"is a",animal)