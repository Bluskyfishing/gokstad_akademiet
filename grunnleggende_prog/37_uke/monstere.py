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

