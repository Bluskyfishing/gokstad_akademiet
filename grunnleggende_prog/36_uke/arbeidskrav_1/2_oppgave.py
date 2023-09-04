#Opprett og skriv ut en liste med 5 tilfeldig heltall mellom 1 og 100  
import random

tall_liste = []
tall2_liste = []

for i in range(0,5):
    tall = random.randint(0,100)
    tall_liste.append(tall)

#Sorter og skriv ut den samme listen med tallene i stigende rekkefølge.
tall_liste.sort()

print("5 tilfeldig heltall mellom 1 og 100:",tall_liste)

#Opprett og skriv ut en liste med 100 tilfeldige heltall mellom 1 og 200  
for i in range(0,100):
    tall2 = random.randint(0,200)

#I listen med 100 tilfeldig tall skal du nå fjerne alle tall som er større en 100 
#I listen med tilfeldig tall skal du nå også fjerne alle tall som er delelig med tre, altså tall som er i 3 gangeren. 
    if tall2 >= 100:
        pass
    elif tall2 % 3 != 0:
        tall2_liste.append(tall2)

print(tall2_liste)    


input()