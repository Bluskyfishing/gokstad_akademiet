#Skriv en funksjon som tar en lengde i meter som input og returnerer lengden i fot. 
#Tallet som skal testes skal leses inn fra tastaturet. Eksempler på konverteringer: 
#7 meter[Equation]22,97 fot 17 meter[Equation]55,77 fot 



#Lag en funksjon som og konverterer temperatur i Celsius til Fahrenheit. Tallet skal testes skal leses inn fra tastaturet. Eksempler på konverteringer:  

#-20 grader celsius → -4.0 Fahrenheit 6 grader celsius →42.8 Fahrenheit 17 grader celsius → 62.6 Fahrenheit 

temp = float(input("Skriv inn temperatur i Celcius: "))
farenheit = temp * (9/5) + 32 
print(f"Temperaturen er °{farenheit}.")