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

svar = 1 

#while svar != "avslutt":
tall1 = random.randint(1,10)
tall2 = random.randint(1,10)
regneoperator = random.randint(0,3)
valg_regneopetraor = ["addisjon","subtraksjon","divisjon","multiplikasjon"]
final_valg = valg_regneopetraor[regneoperator]

print(final_valg)

if final_valg == "addisjon":
    svar = int(input(f"Hva er {tall1} + {tall2}\nSkriv her: "))
elif final_valg == "subtraksjon":
    svar = int(input(f"Hva er {tall1} - {tall2}\nSkriv her: "))
elif final_valg == "divisjon":
    svar = int(input(f"Hva er {tall1} / {tall2}\nSkriv her: "))
elif final_valg == "multiplikasjon":
    svar = int(input(f"Hva er {tall1} * {tall2}\nSkriv her: "))

 if svar == resultat:
     tall1 = random.randint(1,10)
     tall2 = random.randint(1,10)
     resultat = tall1 * tall2
 
   # if svar == "avslutt":
   #     print("Programmet avsluttes!")
   #     break
    