#Kode fra tavla: 
#print(f'{2} + {3} = {2+3}')
#enere = 3 
#toere = 6 
#summen = enere + toere
#print(f"Summen av enere og toere er {summen}.")

#Oppgaver:
#1 Be brukeren om sitt navn og skriv ut en hilsen med navnet. 
#navn = input(str("Hei! Hva er navnet ditt?: "))
#print(f"Hei {navn} hvordan går det?")

#2 Be brukeren om to tall, legg dem sammen, og skriv ut resultatet. 
#svar1 = input("Skriv inn et tall: ")
#svar2 = input("Skriv inn et tall till: ")
#summen = int(svar1) + int(svar2) 
#print(f"Summen er {summen}.")

#3 Be brukeren om to tall og finn gjennomsnittet av dem. Skriv ut resultatet. 
#tall1 = int(input("Skriv inn tall: "))
#tall2 = int(input("Skriv inn et annent tall: "))
#sum1 = tall1 + tall2
#print(f"gjennomsnittet mellom tallene er: {sum1/2}")

#4 Konverter en temperatur fra Celsius til Fahrenheit og skriv ut resultatet. 
#temp = float(input("Skriv inn temperatur i celcius: "))
#farenheit = temp * (9/5) + 32 
#print(f"Temperaturen er °{farenheit}.")

#5 La brukeren gi inn et antall minutter og konverter dette til timer og minutter.
#antall= int(input("Angi antall minutter: "))
#timer = antall // 60 
#minutter = antall % 60 
#print(f" {timer} timer og {minutter} minutter.")

#6 Be brukeren om en tekst og tell antall tegn i teksten. Skriv ut resultatet. 
#teller = len(input("Skriv et ord: "))
#print(f"Ordet har {teller} bokstaver i seg.")

#7 Spør brukeren om sin fødselsdato og beregn deres alder. 
#bursdag= int(input("Hva er fødselsdatoen din? "))
#alder = 2023 - bursdag 
#print(f"Du er {alder} år gammel.")

#8 La brukeren gi inn en pris, beregn 15% tips og skriv ut både tips og totalprisen. 
#pris = int(input("Skriv inn pris på vare: "))
#total = pris * 1.15 
#tips = total * 0.15
#print(f"Tips:{tips} Total: {total}")

#9 Be brukeren om et ord, og skriv ut ordet baklengs. 
#ord = input("Skriv inn et ord: ")
#print(ord[::-1])

#10 Spør brukeren om en hel streng, og finn ut om strengen er et palindrom.
#ord = input("Skriv inn et ord: ")
#reverseord = ord[::-1]
#if ord == reverseord:
#    print("Ordet er palindrom!")
#else:
#    print("Ordet er ikke palindrom!")

#11 Be brukeren om deres vekt i kilo og høyde i meter, og beregn deres BMI. 
#vekt = int(input("Vekt i Kg: "))
#hoyde = float(input("Høyde i M: "))
#hoyde2 = hoyde*hoyde
#bmi = vekt/hoyde2 
#print(f"Bmi-en din er: {bmi}.")

#12 Konverter en temperatur fra Fahrenheit til Celsius og skriv ut resultatet. 
#temp = float(input("Skriv inn temperatur i farenheit: "))
#celsius = (temp - 32)*5/9
#print(f"Temperaturen i celsius er °{celsius}")

#14 Be brukeren om radiusen på en sirkel og beregn sirkelens omkrets. 
#i = 3.14
#adius = float(input("Radius på sirkel: "))
#mkrets = (pi*2)*radius
#rint(f"Omkretsen er {omkrets} cm.")

#15 Be brukeren om radiusen på en sirkel og beregn sirkelens areal. 
#i = 3.14
#radius = float(input("Hva er radiusen på sirkelen?: "))
#real = pi*radius**2
#rint(f"Arealet på sirkelen er {areal}.")

#21 Spør brukeren om et heltall og skriv ut om tallet er oddetall eller partall.  ----------------------
#svar = int(input("Skriv inn tall: ")) inrange?

#22 chatgpt hjalp litt. 
#svar = input("Skriv inn et ord: ")
#vokalliste = "aeiouæøåAEIOUÆØÅ"
#teller = 0 
#for vokal in svar:
#    if vokal in vokalliste:
#        teller += 1 
#print(f"Det er {teller} vokaler i ordet ditt.")

#25 Be brukeren om to ord og sjekk om de er anagrammer av hverandre.
#ord1 = input("Skriv inn ord1: ") 
#ord2 = input("Skriv inn ord2: ")
#
#liste1 = []
#liste2 = []
#
#for bokstav in ord1: 
#    liste1.append(bokstav)
#for bokstav2 in ord2:    
#    liste2.append(bokstav2)
#
#liste1.sort()
#liste2.sort()
#
#if liste1== liste2:
#    print("Disse ordene er anagrammer!")
#else:
#    print("Disse ordene er ikke anagramemr!")

#29 Spør brukeren om et ord og skriv ut det tredje og det nest siste tegnet i ordet. 
#ord = (input("Skriv inn et ord. "))
#print(ord[2], ord[len(ord)-2])

#30 Be brukeren om en setning og skriv ut hvert ord i setningen på en ny linje.
#setning = input("Skriv inn en setning: ")
#ord_liste = setning.split()
#for ord in ord_liste:
#    print(ord)

#31 Be brukeren om en tekst og skriv ut om teksten inneholder bokstaven 'a'.
#tekst = input("Skriv inn en tekst: ").lower()
#liste = []
#for bokstav in tekst:
#    liste.append(bokstav)    
#if "a" in liste:
#    print("Teksten inneholder A!")
#else:
#    print("Teksten inneholder ikke A!")

#32 Be brukeren om et tall og skriv ut tallets faktorielle. -----------------

#33 Spør brukeren om en setning og skriv ut antall ord i setningen.
#setning = input("Skriv en setning: ")
#deltsetning = setning.split()
#print(f"Det er {len(deltsetning)} ord i setningen.")

#34 Be brukeren om et ord og skriv ut ordet med store bokstaver.
#ord = input("Skriv ett ord: ")
#print(ord.upper())

#35 La brukeren gi inn et tall og avgjøre om tallet er positivt, negativt, eller null. -----------

#36 Spør brukeren om tre tall og skriv ut det største tallet.
#tall1 = int(input("Skriv inn første tall: "))
#tall2 = int(input("Skriv inn andre tall: "))
#tall3 = int(input("Skriv inn tredje tall: "))
#
#tall_liste = []
#
#tall_liste.append(tall1)
#tall_liste.append(tall2)
#tall_liste.append(tall3)
#tall_liste.sort()
#
#print(tall_liste[2])

#37 Be brukeren om en tekst og skriv ut antall mellomrom i teksten.
#tekst = input("Skriv en tekst: ")
#mellomrom = tekst.count(" ")
#print(f"Det er {mellomrom} mellomrom i denne teksten.")

#38 Be brukeren om et ord, bytt ut alle vokalene med bokstaven 'x', og skriv ut det nye ordet. -----------------

#39 Spør brukeren om et tall og skriv ut alle heltall opp til det tallet. -----------------------

#40 La brukeren gi inn en setning og skriv ut setningen i omvendt rekkefølge. ---------------------------
#setning = input("Skriv setning: ")
#
#deltopp = setning.split()
#reverse_setning = []
#for x in deltopp:
#    reverse_setning.append(x)
#    reverse_setning.append(" ")
#print(reverse_setning)