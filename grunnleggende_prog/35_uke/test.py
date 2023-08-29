#x = bool(input("True eller False"))
#
#print(x) 


#user_bool = None
#
#while user_bool != "true" or user_bool != "false":
#    user_bool = input("Skriv inn True eller False: ").lower()
#    print(user_bool)
#if user_bool == "true":
#    user_bool = True
#    print(f"verdien av user_bool={user_bool}") 
#elif user_bool == "false":
#    user_bool = False
#    print(f"verdien av user_bool={user_bool}") 

#if user_bool == "true":
#    user_bool = True
#    print(f"verdien av user_bool={user_bool}") 
#elif user_bool == "false":
#    user_bool = False
#    print(f"verdien av user_bool={user_bool}") 
#else:
#    print("Kjenner ikke igjen verdi.")


import random

spiller_score = 0
pc_score = 0
runder = 0

valg_navn = ["stein", "saks", "papir"]

while runder < 10:
    pc_valg = random.randint(0, 2)
    spiller_valg = int(input("Skriv inn et tall (0-2)\n0 = Stein\n1 = Saks\n2 = Papir\nSkriv her: "))

    print(f"Spiller valgte: {valg_navn[spiller_valg]}")
    print(f"PC valgte: {valg_navn[pc_valg]}")

    if spiller_valg == pc_valg:
        print("Uavgjort!")
    elif (spiller_valg == 0 and pc_valg == 1) or (spiller_valg == 1 and pc_valg == 2) or (spiller_valg == 2 and pc_valg == 0):
        spiller_score += 1
        print(f"Spiller vinner!\nScore: Spiller: {spiller_score} PC: {pc_score}")
    else:
        pc_score += 1
        print(f"PC vinner!\nScore: Spiller: {spiller_score} PC: {pc_score}")

    runder += 1

print("Spillet er ferdig!")
