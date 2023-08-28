import random

tall = random.randint(1, 100)

teller = 0
svar = None

print(tall)

while svar != tall: 
    svar = int(input(f"Gjett tallet! (1 - 100):\n"))
    teller += 1
    if svar > tall:
        print("Svaret er for stort!")
    if svar < tall: 
        print("Svaret er for lite!")
    if svar == tall: #Funker ikke med else? 
        print(f"Du klarte det med {teller} forsøk!")
        break