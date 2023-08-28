# kopier denne teksten og lag en python fil i Pycharm eller en annen editor. 

# Finn feilene !! 
 
# Leser inn to heltall fra brukeren 

number1 = int(input("Skriv inn det første tallet: ")) 

number2 = int(input("Skriv inn det andre tallet: ")) 

# Leser inn en desimaltall fra brukeren 

float_number = float(input("Skriv inn et desimaltall: ")) 

# Utfører enkel matematikk 

sum_numbers = number1 + number2 

product = number1 * number2 

quotient = number1 / number2 

# Printer resultatene 

print("Summen av tallene er: ", sum_numbers) 

print("Produktet av tallene er: ", product) 

print("Kvotienten av tallene er: ", quotient) 
 
# Leser inn en streng og en boolsk verdi fra brukeren 

user_string = input("Skriv inn en streng: ") 

user_bool = input("Skriv inn True eller False: ").lower()

if user_bool == "true":
    user_bool = True
    print(f"verdien av user_bool={user_bool}") 
elif user_bool == "false":
    user_bool = False
    print(f"verdien av user_bool={user_bool}") 
else:
    print("Kjenner ikke igjen verdi.")

# Konverterer float til int og utfører en operasjon 

float_as_int = int(float_number) 

result = float_as_int * number1 

# Printer det endelige resultatet 

print("Resultatet av operasjonen er: ", result) 