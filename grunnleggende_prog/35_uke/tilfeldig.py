#oppgaver for Random lib
#1
import random 

#tall = random.randint(1, 100)
#print(tall)

#2
#tall = random.random()
#print(tall * 100)

#3
#tall = random.randint(5, 15)
#
#forsok = int(input("Gjett tallet: "))
#
#if forsok == tall: 
#    print("Riktig!")
#else:
#    print("Feil!")

#4
#tall1 = random.randint(1,100)
#tall2 = random.randint(1,100)
#tall3 = tall1 + tall2 
#
#svar = int(input(f"Hva er summen av {tall1} + {tall2}?\n"))
#
#if svar == tall3:
#    print("Riktig!")
#else:
#    print("Feil!")

#5
#tall = random.randint(1,2)
#
#if tall == 1:
#    tall = True
#else:
#    tall = False
#
#print(tall)

#6
#tall1 = random.randint(1,10)
#tall2 = random.randint(1,10)
#tall3 = random.randint(1,10)
#
#tall_liste = []
#
#tall_liste.append(tall1)
#tall_liste.append(tall2)
#tall_liste.append(tall3)
#
#tall_liste.sort()
#
#print(tall_liste)
#print(f"Størst: {tall_liste[0]} Minst: {tall_liste[2]}")

#7
#tall = random.randint(1, 10) 
#
#dobbel = tall * 2
#
#print("Dette var tallet",tall,"Dette er det nye tallet",dobbel)

#8
#tall = random.uniform(10,20)
#
#rundet_tall = round(tall)
#
#print(f"Tallet var: {tall} rundet av er det: {rundet_tall}.")

#9
#tall = random.randint(1,100)
#
#delt_tall = tall/2
#
#print(f"Tallet var {tall} ,delt på 2 blir det {delt_tall}")

#10
#tall = random.randint(50,100)
#
#trekk_tall = tall - 25
#
#print(f"Tallet var {tall} ,-25 blir det {trekk_tall}")

#Stein, saks, papir

spiller_score = 0 
pc_score = 0 
runder = 0
valg_navn = ["stein", "saks", "papir"]


def gamemaster(spiller_score, pc_score, runder):
    while runder < 10:
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

        if runder == 10:
            if spiller_score > pc_score:
                print("Spiller vinner vant med:",spiller_score,"poeng!")
            elif pc_score > spiller_score:
                print("PC vinner vant med:",pc_score,"poeng!")
            else:
                print("SUDDEN DEATH!!!")
                while spiller_score == pc_score:
                    pc_valg = 1 #random.randint(0,2)
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
        
gamemaster(spiller_score, pc_score, runder) 

print(f"Spillet er ferdig!")