valg = 0

while valg != "stop":
    valg = str(input(f"Velg et av følgene valg:\n1.Addisjon\n2.Subtraksjon\n3.Multiplikasjon\n4.Divisjon\n5.Avslutt\nSkriv her: ")).lower()

    if valg == "1" or valg == "addisjon":
        print("Operator valgt: +")
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 + tall2
        print(f"{tall1} + {tall2} = {resultat}\n")

    elif valg == "2" or valg == "subtraksjon":
        print("Operator valgt: -")
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 - tall2
        print(f"{tall1} - {tall2} = {resultat}\n")

    elif valg == "3" or valg == "multiplikasjon":
        print("Operator valgt: *")
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 * tall2
        print(f"{tall1} * {tall2} = {resultat}\n")

    elif valg == "4" or valg == "divisjon":
        print("Operator valgt: /")
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 / tall2
        print(f"{tall1} / {tall2} = {resultat}\n")

    elif valg == "0" or valg == "avslutt":
        print("Programmet avsluttes!")
        break
    
    else:
        print(f"Gjenskjenner ikke valg prøv på nytt!\n")


input()