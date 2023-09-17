def hengman(ord,liv):
    hemmlig_ord = []
    husket_ord = []

    for bokstav in ord:
        husket_ord.append(bokstav)
        if bokstav == " ":
            hemmlig_ord.append(bokstav) 
        else:
            hemmlig_ord.append(bokstav.replace(bokstav,"_"))

    while True:
        print("\nLengde på ordet:","".join(hemmlig_ord))
        svar = input("Gjett en bokstav!: ")

        if svar in husket_ord:
            for index in range(len(husket_ord)):
                if svar == husket_ord[index]:
                    hemmlig_ord[index] = svar
                    continue
        if svar not in husket_ord:
            liv -= 1
            if liv == 0:
                print("Du tapte! Svaret var:","".join(husket_ord))
                break
            print("Du mistet et liv! Du har:",liv,"igjen!")
        if hemmlig_ord == husket_ord:
            print("Du vinner! Svaret var:","".join(husket_ord))
            break


ord = input("Skriv inn ordet som skal gjettes: ")
liv = int(input("Antall liv: "))

hengman(ord,liv)