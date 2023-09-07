# Spill: Gjett et tall 

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

# Kalkulator med meny 
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

import random

tall1 = random.randint(1,10)
tall2 = random.randint(1,10)
resultat = tall1 * tall2

svar = int(input(f"Hva er produktet mellom {tall1} og {tall2}\nSkriv her: "))

if svar == resultat:
    print("Riktig! Neste spørsmål!")
    tall1 = random.randint(1,10)
    tall2 = random.randint(1,10)
    resultat = tall1 * tall2
    while svar != resultat:
        svar = int(input(f"Hva er produktet mellom {tall1} og {tall2}\nSkriv her: "))
elif svar == 0:
    pass