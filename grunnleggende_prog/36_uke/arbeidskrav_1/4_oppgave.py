#For hver av verdiene i listen [3, 5, 9, 10, 11], skriv ut om verdien er: 
#større eller lik 10  
#mindre eller lik 5  
#mellom 5 og 10  
liste = [3, 5, 9, 10, 11]

for tall in liste:
    if tall >= 10 or tall <= 5:
        print(tall)
print("")

for tall in liste:
    if tall >= 5 and tall <= 10:
        print(tall)
print("")

#Lag en for-løkke hvor du skriver ut både index og verdi for denne listen på en egen linje. 
#Eks: «Index=0, Verdi=3»  
index_teller = 0

for tall in liste:
    print(f"Index:{index_teller} Verdi:{tall}")
    index_teller += 1
print("")

#Gjør det samme som i oppgave B. men nå gjør med en while-løkke.   
index_teller = 0

while index_teller < 5:
    print(f"Index:{index_teller} Verdi:{liste[index_teller]}")
    index_teller += 1
print("")

#Lag et program som regner ut summen av alle tallene i listen.  
total = 0

for tall in liste:
    total += tall
print(total)

#print(sum(liste))


input()