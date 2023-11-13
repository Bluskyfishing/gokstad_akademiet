import os 
import sys

def read_persons(filename: str, includeHeader=False) -> list | str:
    # sjekk at filen finnes
    if not os.path.exists(filename):
        return f"Finner ikke filen: '{filename}'"

    person_data_list = []
    with open(filename, 'r', encoding='utf-8') as file_read:
        for idx, line in enumerate(file_read):
            if idx == 0 and not includeHeader:
                continue
            person_arr = line.rstrip('\n').split(',')
            
            if idx == 0 and includeHeader:
                person_data_list.append(person_arr)
                continue

            # 1. Validering, sjekke at vi har 4 felter
            if not len(person_arr) == 4:
                print(f"Feil format på filen: linenr {idx} -> {line}")
                continue

            # person_arr = ['Ole', 'Johansen', '44', 'Mann']
            first_name, last_name, age, gender = person_arr

            # 2. Validering, sjekker at vi har verdier i alle felt
            if not all([first_name, last_name, age, gender]):
                print(f"Feil i data, mangler felter: linenr: {idx} -> {line}")
                continue

            # 3. Validering, sjekker at age er en int !!
            if not age.isdigit():
                print(f"Feil i data, age er ikke et tall: linenr: {idx} -> {line}")
                continue

            # 4. Validering, sjekker at kjønn er 'kvinne' eller 'mann'
            if not gender.lower() in ['kvinne', 'mann']:
                print(f"Feil i data, kjønn stemmer ikke: linenr: {idx} -> {line}")

            # Nå har vi gyldig data på denne linjen
            # passe på å legge inn riktig datatype på alder
            person_data_list.append((first_name, last_name, int(age), gender))

    return person_data_list


# tester
#FILENAME = "persons.csv"
#results = read_persons(FILENAME)
#if isinstance(results, str):
#    print(f"Avslutter, årsak: {results} ")
#    sys.exit()

#for r in results:
#    print(r)

def lineCounterInFile(fileName: list):
    readFile = open(fileName, "r")

    counter = 0 
    for i in readFile:
        counter += 1 
    print("Amount of lines in file:",counter)


def reversedFileFix(fileName: list):
    with open(fileName, "r") as readFile:
        data = readFile.read()
    
    reversedData = data[::-1]

    with open(fileName, "w") as writeFile:
        writeFile.write(reversedData)
        writeFile.close()


def findAgeOfGender(fileName: list, gender: str):
    with open(fileName, "r") as readFile:
        line = readFile.readline().rstrip("\n")
        age = 0
        while line:
            elementList = line.split(",")
            for element in elementList:
                if gender in elementList:
                    try:
                        num = int(element)
                        age += num
                    except ValueError:
                        continue
            line = readFile.readline().rstrip("\n")
        return age

#ageWomen = findAgeOfGender(FILENAME, "Female")
#ageMen = findAgeOfGender(FILENAME, "Male")
#print("The total age of Women is:",ageWomen)
#print("The total age of Men is:",ageMen)

def findgender(fileName: list, gender: str):
    with open(fileName, "r") as readFile:
        line = readFile.readline().rstrip("\n")
        counter = 0
        while line:
            elementList = line.split(",")
            for element in elementList:
                if gender == element:
                    counter += 1
            line = readFile.readline().rstrip("\n")
        return counter
    
#totalWomen = findgender(FILENAME, "Female")
#totalMen = findgender(FILENAME, "Male")
#print("The total amount of females:",totalWomen)
#print("The total amount of males:",totalMen)