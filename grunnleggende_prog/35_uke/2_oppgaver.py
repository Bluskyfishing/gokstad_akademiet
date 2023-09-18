# 1.Spill: Gjett et tall 

import random
def gjettespill():
    tall = random.randint(1, 100)

    teller = 0


    print(tall)

    while True: 
        svar = input(f"Gjett tallet! (1 - 100):\n")
        if not svar.isdigit():
            print("Skriv inn et tall!")
            continue
        svar = int(svar)
        teller += 1
        if svar > tall:
            print("Svaret er for stort!")
        if svar < tall: 
            print("Svaret er for lite!")
        if svar == tall:
            print(f"Du klarte det med {teller} forsøk!")
            break
gjettespill()

# 2.Kalkulator med meny 
def kalkulator():
    valg = float(input(f"Velg et av følgene valg:\n1.Addisjon\n2.Subtraksjon\n3.Multiplikasjon\n4.Divisjon\n5.Avslutt\nSkriv her: "))

    if valg == 1:
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 + tall2
        print(f"{tall1} + {tall2} = {resultat}")
    elif valg == 2:
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 - tall2
        print(f"{tall1} - {tall2} = {resultat}")
    elif valg == 3:
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 * tall2
        print(f"{tall1} * {tall2} = {resultat}")
    elif valg == 4:
        tall1 = float(input("Skriv inn et tall: "))
        tall2 = float(input("Skriv inn et tall til: "))
        resultat = tall1 / tall2
        print(f"{tall1} / {tall2} = {resultat}")
    else:
        pass

# 3.Gangetabell spillet 
import random

def ganngetabellen():
    while True:
        tall1 = random.randint(-10,10) #Random tall
        tall2 = random.randint(-10,10)
        regneoperator = random.randint(0,3) 
        valg_regneopetraor = ["addisjon","subtraksjon","divisjon","multiplikasjon"] #Liste med regneoperatorer
        final_valg = valg_regneopetraor[regneoperator] #Velger hvilken operator string 

        print(final_valg)

        if final_valg == "addisjon":
            resultat = tall1 + tall2
            svar = int(input(f"Hva er {tall1} + {tall2}\nSkriv her: "))
        elif final_valg == "subtraksjon":
            resultat = tall1 - tall2
            svar = int(input(f"Hva er {tall1} - {tall2}\nSkriv her: "))
        elif final_valg == "divisjon":
            resultat = tall1 / tall2
            svar = int(input(f"Hva er {tall1} / {tall2}\nSkriv her: "))
        elif final_valg == "multiplikasjon":
            resultat = tall1 * tall2
            svar = int(input(f"Hva er {tall1} * {tall2}\nSkriv her: "))

        if svar == resultat: #Hvis riktig svar skipper iterasjon.
            continue
        elif svar == "avslutt":
            print("Programmet avsluttes!")
            break
        else: 
            while svar != resultat: #Hvis svar ikke er resultatet, går i loop.
                svar = int(input("Try again!: "))

# 4.Løs førstegradslikning (heltallsløsning) -------------------

#def venstre():
#    for x in range(-100,100):
#        pass
#
#
#def hoyre():
#    for x in range(-100,100):
#        pass

# 5. Stein, saks, papir med tkinter. se 35_uke/test.py  ------------------

#import random
#from tkinter import *
#
#spiller_score = 0 
#pc_score = 0 
#runder = 0
#valg_navn = ["stein", "saks", "papir"]
#
#
#while runder < 2:
#    pc_valg = random.randint(0,2)
#    spiller_valg = int(input(f"Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))
#
#    print(f"Spiller valgte: {valg_navn[spiller_valg]}")
#    print(f"PC valgte: {valg_navn[pc_valg]}")
#
#    if spiller_valg == pc_valg:
#        print(f"Uavgjort!\nScore: Spiller:{spiller_score} PC:{pc_score} ")
#    elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
#        spiller_score += 1
#        print(f"Spiller vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
#    else:
#        pc_score += 1
#        print(f"PC vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
#
#    runder += 1
#
#    if runder == 2:
#        if spiller_score > pc_score:
#            print("Spiller vinner vant med:",spiller_score,"poeng!")
#        elif pc_score > spiller_score:
#            print("PC vinner vant med:",pc_score,"poeng!")
#        else:
#            print("SUDDEN DEATH!!!")
#            while spiller_score == pc_score:
#                pc_valg = random.randint(0,2)
#                spiller_valg = int(input(f"Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))
#                
#                if spiller_valg == pc_valg:
#                    print(f"Uavgjort!\nScore: Spiller:{spiller_score} PC:{pc_score} ")
#                    print("SUDDEN DEATH!!!")
#                elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
#                    spiller_score += 1
#                    print(f"Spiller vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
#                else:
#                    pc_score += 1
#                    print(f"PC vinner!\nScore: Spiller:{spiller_score} PC:{pc_score}")
#    
#print(f"Spillet er ferdig!")


# 6.Black jack
#------------------------

# 7.Færrest terningkast for å oppnå 50 poeng     
#import random 

def terning():
    poeng = 0 
    antall_kast = 0

    while True:
        antall_kast += 1 
        terning = random.randint(1,6)
        terning2 = random.randint(1,6)
        print("terning: ",terning,"terning-2: ",terning2)
        poeng += terning
        poeng += terning2
        if terning == terning2:
            poeng += terning
            print("Dobbelt! poeng!")
        resultat = poeng
        print("poeng:", resultat,"antall kast:",antall_kast)
        if resultat > 50:
            break

# 8. Lag et program som løser pytagoras 
import math


def pytagoras():
    vinkel1 = int(input("Skriv in vinkel A: "))
    vinkel2 = int(input("Skriv in vinkel B: "))
    vinkel_ekpo = pow(vinkel1,2) + pow(vinkel2,2)
    vinkel3 = math.sqrt(vinkel_ekpo)
    print(f"A:{vinkel1} B:{vinkel2} = C: {vinkel3}")




# 9. Lage eget matematisk bibliotek ( egen .py fil som kan brukes fra andre program, interaktivt shell) 