#1 Lag en forløkke som skriver ut tallene 0-9 
#for x in range(10):
#    print(x)

#2 Lag en forløkke som skriver ut tallene 5 - 15 
#for x in range(5,15):
#    print(x)

#3 Lag en forløkke som skriver ut alle partallene opp til 20. 
#for x in range(2,20,2):
#    print(x)

#eller

#for x in range(1,20):
#    if x %2 == 0:
#        print(x)

#4 Lag en forøkke som skriver ut alle oddetallene opp til 20 
#for x in range(1,20):
#    if x %2 == 1:
#        print(x)

#5 Lag en forløkke som skriver ut alle tallene fra 30 og ned til 10 
#for x in reversed(range(10,31)):
#    print(x)

#6 Lag en forløkke som skriver alle oddetallen fra 30 - 10 
#for x in reversed(range(10,31)):
#    if x %2== 1:
#        print(x)

#7 Lag en forløkke som summerer alle tallen fra 1 til 10. Skriv ut ny sum for hver iterasjon (runde i løkken) 
#sum = 0
#for x in range(1,11):
#    sum += x
#    print("Summen etter", x, "iterasjoner:", sum)

#8 Lag en forløkke som summerer alle partallene opp til 20 
#sum = 0 
#for x in range(1,21):
#    if x %2 == 0:
#        sum += x
#        print("Partall:", x ,"Iterasjon:" ,sum)

#9 Lag en forløkke som summerer alle oddetallene opp til 20  
#sum = 0
#for x in range(1,21):
#    if x %2 == 1:
#        sum += x
#        print("Oddetall:",x,"Iterasjon:",sum)

#10 Lag et program som leser inn et tall for deretter å skrive ut gangetabellen for dette tallet. Bruk for løkke.
#tall = int(input("Skriv inn et tall som skal ganges: "))
#
#for x in range(0,11):
#    print(tall * x)

#11 Lag en while løkke som skrive ut tallene 1 - 10 
#tall = 0
#while tall < 10:
#    tall += 1 
#    print(tall)

#12 Lag en while løkke som skriver ut tallene 5 -15 
#tall = 4
#while tall < 15:
#    tall += 1 
#    print(tall)

#13 Lag en while løkke som skriver ut tallene fra 30 - 10 
#tall = 31
#
#while tall > 10:
#    tall -= 1
#    print(tall)

#14 While løkke som skriver ut partallene opptil 20  
#tall = 0
#while tall < 20:
#    tall += 1
#    if tall %2 == 0:
#        print(tall)

#15 Lag en while løkke som skriver alle kvadrattallene opptil 100 
#tall = 1
#while tall < 11:
#    summen = tall * tall
#    tall += 1  
#    print(summen)

#16 Lag en while løkke som skriver alle kvadrattallene som er mindre enn oppgitt innput. Les denne verdien inn fra tastaturet. 
#tall = int(input("Skriv inn et tall: "))
#while tall < 11:
#    summen = tall * tall
#    tall += 1
#    print(summen)

#17 Les inn et tall fra tastaturet.  
#tall = int(input("Skriv inn et tall: "))
#
#if tall > 10:
#    print("Tallet er større enn 10.")
#elif tall < 10:
#    print("Tallet mindre enn 10.")
#else:
#    print("Tallene er like.")

#18 Lag et program som skriver ut denne tallfølgen på skjermen (Fibonaccitall).
#n = int(input("Hvor mange Fibonacci-tall vil du generere? "))
#
#fib_sequence = [0, 1]
#for _ in range(2, n):
#    next_fib = fib_sequence[-1] + fib_sequence[-2]
#    fib_sequence.append(next_fib)
#
#print("Fibonacci-tallene:")
#for fib in fib_sequence:
#    if fib == 0:
#        pass
#    else:
#        print(fib)

#19 Lag et program som for hver iterasjon dobler tallet som skrives ut på skjerm. Start med tallet 1 og gjør dette for de 10 første tallene. 
#tall = int(input("Skriv inn et tall: "))
#
#print(tall)
#
#for x in range(1,11):
#    tall *= 2
#    print(tall)

#20 Lag et program som skriver ut gangetabellen slik som du ser under.


for x in range(1,11):
    print(f"1*{x}={1 * x} 2*{x}={2 * x} 3*{x}={3 * x} 4*{x}={4 * x} 5*{x}={5 * x} 6*{x}={6 * x} 7*{x}={7 * x} 8*{x}={8 * x} 9*{x}={9 * x} 10*{x}={10 * x}")

