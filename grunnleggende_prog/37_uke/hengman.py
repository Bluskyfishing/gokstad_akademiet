
ord = input("Skriv inn ordet som skal gjettes: ")
#liv = int(input("Antall liv: "))

hemmlig_ord = []
husket_ord = []

for bokstav in ord:
    husket_ord.append(bokstav)
    hemmlig_ord.append(bokstav.replace(bokstav,"_"))

while True:
    print("\nLengde på ordet: ",hemmlig_ord)
    svar = input("Gjett en bokstav!: ")
    if svar in husket_ord:
        for i in range(len(husket_ord)):
            pass            

    print(hemmlig_ord)
 
    if svar == husket_ord:
        print("Du vinner! Svaret var: ",husket_ord)
        break


# Må nok bruke dette for å sammenligne listene.
#     for i in range(len(liste)):
#        if liste[i] == liste2[i]:
#            felles.append(liste[i])