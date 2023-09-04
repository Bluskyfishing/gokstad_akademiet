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
valg = 0

while valg != "stop":
    valg = str(input(f"Velg et av følgene valg:\n1.Addisjon\n2.Subtraksjon\n3.Multiplikasjon\n4.Divisjon\n5.Avslutt\nSkriv her: ")).lower()
    if valg == "1" or valg == "addisjon":
        tall1 = float(input("Skriv inn et tall: "))
        print("Operator valgt: +")
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 + tall2
        print(f"{tall1} + {tall2} = {resultat}")

    elif valg == "2" or valg == "subtraksjon":
        tall1 = float(input("Skriv inn et tall: "))
        print("Operator valgt: -")
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 - tall2
        print(f"{tall1} - {tall2} = {resultat}")

    elif valg == "3" or valg == "multiplikasjon":
        tall1 = float(input("Skriv inn et tall: "))
        print("Operator valgt: *")
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 * tall2
        print(f"{tall1} * {tall2} = {resultat}")

    elif valg == "4" or valg == "divisjon":
        tall1 = float(input("Skriv inn et tall: "))
        print("Operator valgt: /")
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 / tall2
        print(f"{tall1} / {tall2} = {resultat}")

    elif valg == "avslutt":
        print("Programmet avsluttes!")
        break
    
    else:
        print(f"Gjenskjenner ikke valg prøv på nytt!\n")


input()