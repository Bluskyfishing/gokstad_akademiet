#-Enkel Quiz-
poeng = 0 

svar1 = input(f"Hva er hovedstaden i Norge?:\n1.Stockholm \n2.Oslo \n3.Kobenhavn\nSvar: ").lower()

if svar1 == "oslo" or svar1 == "2":
    poeng += 1
    print("riktig svar!")
else:
    print("feil svar!")
print(svar1)

svar2 = input(f"Hva er hovedstaden i Sverige?:\n1.Stockholm \n2.Oslo \n3.Kobenhavn\nSvar: ").lower()

if svar2 == "stockholm" or svar2 == "1":
    poeng += 1
    print("riktig svar!")
else:
    print("feil svar!")

svar3 = input(f"Hva er hovedstaden i Danmark?:\n1.Stockholm \n2.Oslo \n3.Kobenhavn\nSvar: ").lower()

if svar3 == "kobenhavn" or svar3 == "3":
    poeng += 1 
    print("riktig svar!")
else:
    print("feil svar!")

print(f"Du svarte {poeng} riktig!")