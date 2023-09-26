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

dyr = ["hund", "katt", "fisk", "ape", "fugl"]
navn_dyr =["Kåre","Karl","Bob","Per","Espen"]

dyr_dict = {}
for i in range(0,len(dyr)):
    dyr_dict[dyr[i]] = navn_dyr[i]

for i in dyr_dict:
    print(f"{dyr_dict[i]} er en {i}.")


input()