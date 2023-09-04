#from matplotlib import pyplot
#a)
#x =["Volvo", "BMW", "Opel", "Ford", "Tesla","Nissan","Hyundai"]
#y = [1,3,6,7,6,9,4]
#pyplot.bar(x,y)
#pyplot.xlabel("Merke")
#pyplot.ylabel("Antall")
#pyplot.show()

#b)
#x =["6","5","4","3","2","1"]
#y = [1,3,7,6,4,0]
#pyplot.bar(x,y)
#pyplot.xlabel("Karakter")
#pyplot.ylabel("Antall")
#pyplot.show()

#c) finne på en tabell av karakterer og anntall 

#Oppgave 2 vneter på publisering av oppgave i teskst.


#Oppgave 3 
karakter_liste = []
teller = 0

karakterer = None

while karakterer != "stop":
    karakterer = str(input(f"Skriv 'stop' når alle karaterene er lagt inn. \nSkriv inn karakter: "))
    if karakterer == "stop":
        int_liste = list(map(int,karakter_liste))
        int_liste.sort() 

        gjennomsnitt = sum(int_liste) / len(int_liste)

        median = len(int_liste)/2
        median2 = int_liste[int(median)]

        print(f"\nDet ble lagt inn {teller} karakterer.")
        print(f"Den laveste karakteren:{int_liste[0]}\nDen høyeste karakteren:{int_liste[-1]}\nGjennomsnitt karakteren:{gjennomsnitt}")
        print(f"Median karakter:{median2}")
        break
    else:
        teller += 1
        karakter_liste.append(karakterer)