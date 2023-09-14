# 1.Lag for løkker som skriver ut disse mønstrene: 

#for i in range(0,10):
#    for j in range(0,i+1):
#        print("*",end=" ")
#    print("\r")

#Reverse?

# 2.Lister: 
#1

#liste = []
#summen = 0 
#
#while True:
#    tall = input("Skriv inn tall: ")
#    if tall == "quit":
#        break
#    else:
#        int_tall = int(tall)
#        summen += int_tall
#        liste.append(int_tall)
#
#print(liste)
#print("Summen av listen:",summen)
#print("Gjennomsnitt:",summen/len(liste))

# 2.Finn største og minste tall: 

#liste = []
#
#
#while True:
#    tall = input("Skriv inn tall: ")
#    if tall == "quit":
#        break
#    else:
#        int_tall = int(tall)
#        liste.append(int_tall)
#        liste.sort()
#
#
#print(liste[0],liste[-1])

# 3.Gjennomsnitt av oddetall:

#liste = []
#summen = 0 
#
#while True:
#    tall = input("Skriv inn tall: ")
#    if tall == "quit":
#        break
#    else:
#        int_tall = int(tall)
#        liste.append(int_tall)
#
#oddetall = []
#
#for x in liste:
#    if x %2 == 1:
#        oddetall.append(x)
#        summen += x
#
#print(oddetall)
#print("Gjennomsnitt:",summen/len(oddetall))

# 4.Liste med unike elementer: 

#liste = []

#while True:
#    tall = input("Skriv inn tall: ")
#    if tall == "quit":
#        break
#    else:
#        int_tall = int(tall)
#        liste.append(int_tall)
#        set_liste = set(liste)
#        liste_organisert = list(set_liste)
#
#print(liste_organisert)

#Ordentilig: 
#
#liste = []
#ingendup = []
#
#while True:
#    tall = input("Skriv inn tall: ")
#    if tall == "quit":
#        break
#    else:
#        int_tall = int(tall)
#        liste.append(int_tall)
#
#for tall in liste:
#    if tall in ingendup:
#        continue
#    ingendup.append(tall)
#
#print(liste)
#print(ingendup)

# 5. Listeomvendt:
def omvendt_liste():
    liste = []

    while True:
        tekst = input("Skriv tekst inn her: ")
        if tekst == "stop":
            break
        liste.append(tekst)
    liste.reverse()
    print(liste)

# 6. Liste av partall

def partall_liste():
    liste = []

    while True:
        tall = input("Skriv tall inn her: ")

        if tall == "stop":
            break
        tall_int = int(tall)
        if tall_int%2 == 0:
            liste.append(tall_int)

    
    print(liste)

# 7. Slett elementer

def sletting_liste():
    liste = []

    while True:
        tekst = input("Skriv tall inn her: ")

        if tekst == "0":
            break
        liste.append(tekst)

    print(liste)
    
    for element in liste:
        if len(element) > 5:
            liste.pop()
    
    print(liste)

# 8. Tallrekkefølge 

def tallrekkefolge():
    liste = []
    stigende = 0


    while True:
        tall = input("Skriv tall inn her: ")

        if tall == "stop":
            break
        tall_int = int(tall)

        liste.append(tall_int) 

    for i in range(1,len(liste)):
        if liste[i - 1 ] < liste[i]:
            stigende = True
        else:
            stigende = False
        
    if stigende == True:
        print("Listen er i stigende rekkefølge!")
    else: 
        print("Listen er ikke i stigende rekkeføgle!")

# 9. Finn felles elementer

def felles_elementer():
    liste = []
    liste2 = []
    felles = []

    while True:
        tall = input("Skriv tall for liste1: ")
        tall2 = input("Skriv tall for liste2: ") 
        if tall == "stop" or tall2 == "stop":
            break
        tall_int = int(tall)
        tall2_int = int(tall2)

        liste.append(tall_int) 
        liste2.append(tall2_int)
        liste.sort()
        liste2.sort()

    for i in range(len(liste)):
        if liste[i] == liste2[i]:
            felles.append(liste[i])


        
    print(liste,liste2,felles)

# 10. Palindrom-identifikasjon

def palindrom():
    liste = []
    palindrom_ord = []

    while True:
        tekst = input("Skriv tall inn her: ")

        if tekst == "stop":
            break
        liste.append(tekst)

    for i in liste:
        if i == i[::-1]:
            palindrom_ord.append(i)
    
    print(liste,palindrom_ord)

palindrom()