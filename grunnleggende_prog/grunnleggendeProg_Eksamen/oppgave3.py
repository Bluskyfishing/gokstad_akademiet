import math
 
print("\nOppgave A\n")
def førsteBokstavStor(string):
    setningListe = string.split()
    index = 0 

    for element in setningListe:                                   #velger første bokstav og gjør det til en storbokstav.
        setningListe[index] = f"{element[0].upper()}{element[1:]}" #starter fra andrebokstav og går gjennom stringen og slår det sammen.
        index += 1
    setning = " ".join(setningListe)
    return setning

print(førsteBokstavStor("ingen capslock karakterer her nei."))

print("\nOppgave B\n")
def meterTilKilometer(meter):
    try:
        if meter < 0: #Sjekker at tallet er positivt.
            return "Nummer må være positivt"  
        return meter / 1000 #formel for meter til km.
    except TypeError: #Sjekker at tallet er en int.
        return "Nummer må være en int!"

print(meterTilKilometer(500),"km")
print(meterTilKilometer(-500))
print(meterTilKilometer("Hello"))

print("\nOppgave C\n")
def arealAvSirkel(radius):
    try:
        if radius < 0:
            return "Nummer må være positive" 
        areal = math.pi * radius**2 #Formel for areal av sirkel.
        return areal
    except TypeError:
        return "Nummer må være en int!"

print(arealAvSirkel(10),"cm*2")
print(arealAvSirkel(-10))
print(arealAvSirkel("10"))

print("\nOppgave D\n")
def oftestForekomstBokstav(tekst):
    tekstListe = tekst.lower().split() #Fjerner mellomrom, gjør til små bokstaver og legger til i en liste.
    foreKomst = {}

    for element in tekstListe: #Går gjennom hvert ord i listen.
        for bokstav in element: #Går gjennom hver bokstav i ord.
            if bokstav in foreKomst: #Legger til 1 hvis bokstaven allerede er i ordbok.
                foreKomst[bokstav] += 1
            else:
                foreKomst[bokstav] = 1 #Hvis den ikke er i ordboken, blir den lagt inn.
    alleNokklene = max(foreKomst.items(), key=lambda k: k[1]) #Finner høyeste tall i ordbok-verdien nøkkelen er bokstaven.
    return (alleNokklene)                                     #lambda funksjonen sorterer på verdien i ordbok-verdien.                
#                                                              hvis verdien er høyere enn forrige, blir den byttet ut.
print(oftestForekomstBokstav("Ha en fin dag!"))