dyr = ["hund", "katt", "fisk", "ape", "fugl"]
navn_dyr =["Kåre","Karl","Bob","Per","Espen"]

for antall in dyr:
    print(antall)

print(" ")

for individ in range(0,5):
    print(f"{navn_dyr[individ]} er en {dyr[individ]}.")
    
print(f"\nFørste element i dyr: {dyr[0]}\nSiste element i dyr: {dyr[-1]}\n")

dyr.sort()
dyr.reverse()

print(dyr)

print(" ")

dyr_dict = {"hund": "Kåre",
            "katt": "Karl",
            "fisk": "Bob",
            "ape": "Per",
            "fugl": "Espen"}
for i in dyr_dict:
    print(f"{dyr_dict[i]} er en {i}.")


input()