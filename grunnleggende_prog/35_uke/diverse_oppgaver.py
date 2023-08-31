from matplotlib import pyplot
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

#c)

#Oppgave 2


#Oppgave 3 
#a 
karakter_liste = []
teller = 0

karakterer = None

while karakterer != "stop":
    karakterer = str(input(f"Skriv 'stop' når alle karaterene er lagt inn. \nSkriv inn karakter: "))
    if karakterer == "stop":
        int_liste = list(map(int,karakter_liste)) #???? 
        print(int_liste)
        break
    else:
        karakter_liste.append(karakterer)
        
