print("\nOppgave A\n")

frukter = ["eple", "Dragefrukt", "Drue", "Appelsin", "Kiwi"]

print("\nOppgave A.1\n")
for frukt in frukter:
    print(frukt)


print("\nOppgave A.2\n")
index= 0

while index < len(frukter):
    print(frukter[index])
    index += 1


print("\nOppgave B\n")

farger = ["Rød", "Rosa", "Lilla", "Orange", "Brun"]

for index in range(len(frukter)):
    print(f"{frukter[index]} er {farger[index]}.")


print("\nOppgave C\n")

print(f"Andre elementet i listen: {frukter[1]} \nFjerde element i listen: {frukter[-2]}")


print("\nOppgave D\n") #Her antar jeg at jeg må skrive ut hvert element og ikke bare hele listen.

for frukt in sorted(frukter): 
    print(frukt)

print("\nOppgave E\n")

fruktDict = dict(zip(frukter, farger))

for frukt, farge in fruktDict.items():
    print(f"{frukt}: {farge}")  


print("\nOppgave F\n")

list_dicts = [{"name": "Vegard", "age": 50},
            {"name": "Tor", "age": 22},
            {"name": "Siv", "age": 30},
            {"name": "Anne", "age": 30},
            {"name": "Beate", "age": 66}]

#Sorterer listed basert på alder paramenteren. Hvis alder er lik brukes navn som et paramenter.
sortertListe = sorted(list_dicts, key=lambda x: (x["age"], x["name"])) 

for element in sortertListe:
    print(element)