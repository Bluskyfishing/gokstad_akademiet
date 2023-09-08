# 1.Spill: Gjett et tall 

#import random
#
#tall = random.randint(1, 100)
#
#teller = 0
#svar = None
#
#print(tall)
#
#while svar != tall: 
#    svar = int(input(f"Gjett tallet! (1 - 100):\n"))
#    teller += 1
#    if svar > tall:
#        print("Svaret er for stort!")
#    if svar < tall: 
#        print("Svaret er for lite!")
#    if svar == tall:
#        print(f"Du klarte det med {teller} forsøk!")
#        break

# 2.Kalkulator med meny 
#valg = float(input(f"Velg et av følgene valg:\n1.Addisjon\n2.Subtraksjon\n3.Multiplikasjon\n4.Divisjon\n5.Avslutt\nSkriv her: "))
#
#if valg == 1:
#    tall1 = float(input("Skriv inn et tall: "))
#    tall2 = float(input("Skriv inn et tall til: "))
#    resultat = tall1 + tall2
#    print(f"{tall1} + {tall2} = {resultat}")
#elif valg == 2:
#    tall1 = float(input("Skriv inn et tall: "))
#    tall2 = float(input("Skriv inn et tall til: "))
#    resultat = tall1 - tall2
#    print(f"{tall1} - {tall2} = {resultat}")
#elif valg == 3:
#    tall1 = float(input("Skriv inn et tall: "))
#    tall2 = float(input("Skriv inn et tall til: "))
#    resultat = tall1 * tall2
#    print(f"{tall1} * {tall2} = {resultat}")
#elif valg == 4:
#    tall1 = float(input("Skriv inn et tall: "))
#    tall2 = float(input("Skriv inn et tall til: "))
#    resultat = tall1 / tall2
#    print(f"{tall1} / {tall2} = {resultat}")
#else:
#    pass

# 3.Gangetabell spillet 
#import random
#
#while True:
#    tall1 = random.randint(-10,10) #Random tall
#    tall2 = random.randint(-10,10)
#    regneoperator = random.randint(0,3) 
#    valg_regneopetraor = ["addisjon","subtraksjon","divisjon","multiplikasjon"] #Liste med regneoperatorer
#    final_valg = valg_regneopetraor[regneoperator] #Velger hvilken operator string 
#
#    print(final_valg)
#
#    if final_valg == "addisjon":
#        resultat = tall1 + tall2
#        svar = int(input(f"Hva er {tall1} + {tall2}\nSkriv her: "))
#    elif final_valg == "subtraksjon":
#        resultat = tall1 - tall2
#        svar = int(input(f"Hva er {tall1} - {tall2}\nSkriv her: "))
#    elif final_valg == "divisjon":
#        resultat = tall1 / tall2
#        svar = int(input(f"Hva er {tall1} / {tall2}\nSkriv her: "))
#    elif final_valg == "multiplikasjon":
#        resultat = tall1 * tall2
#        svar = int(input(f"Hva er {tall1} * {tall2}\nSkriv her: "))
#
#    if svar == resultat: #Hvis riktig svar skipper iterasjon.
#        continue
#    elif svar == "avslutt":
#        print("Programmet avsluttes!")
#        break
#    else: 
#        while svar != resultat: #Hvis svar ikke er resultatet, går i loop.
#            svar = int(input("Try again!: "))


# 4.Løs førstegradslikning (heltallsløsning) 

import random
from tkinter import *

spiller_score = 0 
pc_score = 0 
runder = 0
valg_navn = ["stein", "saks", "papir"]


while runder < 2:
    pc_valg = random.randint(0,2)
    spiller_valg = int(input(f"Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))

    print(f"Spiller valgte: {valg_navn[spiller_valg]}")
    print(f"PC valgte: {valg_navn[pc_valg]}")

    if spiller_valg == pc_valg:
        print(f"Uavgjort!\nScore: Spiller:{spiller_score} PC:{pc_score} ")
    elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
        spiller_score += 1
        print(f"Spiller vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
    else:
        pc_score += 1
        print(f"PC vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")

    runder += 1

    if runder == 2:
        if spiller_score > pc_score:
            print("Spiller vinner vant med:",spiller_score,"poeng!")
        elif pc_score > spiller_score:
            print("PC vinner vant med:",pc_score,"poeng!")
        else:
            print("SUDDEN DEATH!!!")
            while spiller_score == pc_score:
                pc_valg = random.randint(0,2)
                spiller_valg = int(input(f"Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))
                
                if spiller_valg == pc_valg:
                    print(f"Uavgjort!\nScore: Spiller:{spiller_score} PC:{pc_score} ")
                    print("SUDDEN DEATH!!!")
                elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
                    spiller_score += 1
                    print(f"Spiller vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
                else:
                    pc_score += 1
                    print(f"PC vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
    

print(f"Spillet er ferdig!")