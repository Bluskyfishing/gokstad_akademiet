#Skriv et program som leser inn et navn og skriver ut en hilsen til brukeren.Eks «Hei, Ola»  
navn = input("Skriv navnet ditt: ")

print("Hei", navn)

#Skriv et program som leser inn et tall og skriver ut om tallet er positivt, negativt eller null  
tall = int(input("Skriv et tall: "))

if tall < 0:
    print("Tallet er negativt!")
elif tall > 0: 
    print("Tallet er positivt!") 
elif tall == 0:
    print("Tallet er 0!")

#Skriv et program som leser inn et tall og skriver ut det dobbelte.
tall = int(input("Skriv inn et tall: "))

print(f"Det dobbelte av {tall} er {tall * 2}.")

#Skriv et program som leser inn en tekst og skriver ut teksten baklengs. 
tekst = input("Skriv inn et ord: ")

baklengs = tekst[::-1]

print(f"{tekst} baklengs er {baklengs}.")


input()