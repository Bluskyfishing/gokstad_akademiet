print("\nOppgave A\n")

alder = int(input("Skriv alderen din: "))
print("Du er", alder, "år gammel!")

print("\nOppgave B\n")
inputTall = input("Skriv inn et tall: ")

try:
    tall = int(inputTall)
except ValueError as valErr: 
    print("Feil! Må være et heltall!", valErr)

print("\nOppgave C\n")

tall1 = int(input("Skriv inn et tall: "))
tall2 = int(input("Skriv inn det andre tallet: "))
print("Summen av dem blir:", tall1 + tall2)

print("\nOppgave D\n")

setning = input("Skriv inn en setning: ")
lengde = len(setning.split())
print("Det er", lengde, "ord i setningen.")

print("\nOppgave E\n")

setning = input("Skriv inn en setning: ")
lengde = setning.split() #Lager en liste fra stringen splittet på mellomrom.
lengsteOrd = lengde[0]

for element in lengde:
    if len(element) > len(lengsteOrd): #Hvis elementet i listen er større enn "lengsteOrd" variablen.
        lengsteOrd = element           #redefinerer til variabel. 

print("Det lengste ordet i setningen er:", lengsteOrd)

print("\nOppgave F\n")

setning = input("Skriv inn en setning: ")
lengde = setning.split()

for element in lengde[::-1]:  #Går baklengs gjennom "lengde"-listen.
    print(element, end = " ") #Printer ut hvert element på samme linje.
print()