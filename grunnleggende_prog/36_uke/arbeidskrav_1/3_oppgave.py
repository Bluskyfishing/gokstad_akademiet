#Lag en liste som innholder fem valgfrie dyr (tekststrenger). Skriv så ut alle elementene på hver sin linje. 
dyr = ["hund", "katt", "fisk", "ape", "fugl"]

#Deretter skal du gi dyrene navn. Navnene skal du legge i en ny liste. Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Ola er en hund»  
navn_dyr =["Kåre","Karl","Bob","Per","Espen"]

for antall in dyr:
    print(antall)

for individ in range(0,5):
    print(f"{navn_dyr[individ]} er en {dyr[individ]}.")
    
#Skriv ut det første og siste elementet i listen med dyr.  
print(f"\nFørste element i dyr: {dyr[0]}\nSiste element i dyr: {dyr[-1]}\n")

#Skriv ut listen med dyr i reversert alfabetisk rekkefølge.  
dyr.sort()
dyr.reverse()

print(dyr)

#Du skal nå lage en dictionary med disse fem dyrene med navn. 
dyr_dict = {"hund": "Kåre",
            "katt": "Karl",
            "fisk": "Bob",
            "ape": "Per",
            "fugl": "Espen"}

#Du kan bruke navn som key og hvilken type dyr som value. Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Siri er en katt» 
for i in dyr_dict:
    print(f"{dyr_dict[i]} er en {i}.")



input()