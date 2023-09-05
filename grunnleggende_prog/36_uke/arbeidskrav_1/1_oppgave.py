navn = input("Skriv navnet ditt: ")

print(f"Hei {navn}\n")

tall = int(input(f"Skriv et tall: \n"))

if tall < 0:
    print(f"Tallet er negativt!\n")
elif tall > 0: 
    print(f"Tallet er positivt!\n") 
elif tall == 0:
    print(f"Tallet er 0!\n")

tall = int(input(f"Skriv inn et tall: \n"))

print(f"Det dobbelte av {tall} er {tall * 2}.\n")

tekst = input(f"Skriv inn et ord: \n")

baklengs = tekst[::-1]

print(f"\n{tekst} baklengs er {baklengs}.\n")


input()