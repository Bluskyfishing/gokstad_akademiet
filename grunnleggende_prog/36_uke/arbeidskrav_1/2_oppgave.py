import random

tall_liste = []

for i in range(0,5):
    tall = random.randint(0,100)
    tall_liste.append(tall)

print(tall_liste)

print(" ")

tall_liste.sort()

print("5 tilfeldig heltall mellom 1 og 100 organisert:",tall_liste)

print(" ")

tall2_liste = []

for i in range(0,100):
    tall2 = random.randint(0,200)
    if tall2 >= 100:
        pass
    elif tall2 % 3 != 0:
        tall2_liste.append(tall2)

print(tall2_liste)    


input()