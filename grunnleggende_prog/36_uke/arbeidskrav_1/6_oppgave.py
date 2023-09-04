#Målet med denne oppgaven er å lage en enkel kalkulator som bruker alt du har lært om variabler, datatyper, operatorer, og kontrollstrukturer. 
#Beskrivelse: 

#Lag en Meny:
 
#Programmet skal starte med å vise en meny med følgende valgmuligheter: 
#Addisjon (Pluss) 
#Subtraksjon (Minus) 
#Multiplikasjon 
#Divisjon 
#Avslutt 

#Brukerinput for Valg:  
#Etter at menyen er vist, skal programmet vente på at brukeren gjør et valg. 

valg = float(input(f"Velg et av følgene valg:\n1.Addisjon\n2.Subtraksjon\n3.Multiplikasjon\n4.Divisjon\n5.Avslutt\nSkriv her: "))

if valg == 1:
    tall1 = float(input("Skriv inn et tall: "))
    print("+")
    tall2 = float(input("Skriv inn et tall til: "))
    resultat = tall1 + tall2
    print(f"{tall1} + {tall2} = {resultat}")
elif valg == 2:
    tall1 = float(input("Skriv inn et tall: "))
    print("-")
    tall2 = float(input("Skriv inn et tall til: "))
    resultat = tall1 - tall2
    print(f"{tall1} - {tall2} = {resultat}")
elif valg == 3:
    tall1 = float(input("Skriv inn et tall: "))
    print("*")
    tall2 = float(input("Skriv inn et tall til: "))
    resultat = tall1 * tall2
    print(f"{tall1} * {tall2} = {resultat}")
elif valg == 4:
    tall1 = float(input("Skriv inn et tall: "))
    print("/")
    tall2 = float(input("Skriv inn et tall til: "))
    resultat = tall1 / tall2
    print(f"{tall1} / {tall2} = {resultat}")
else:
    pass


input()