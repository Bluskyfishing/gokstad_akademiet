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


my_dict = dict(zip(dyr,navn_dyr))
print(my_dict)

my_dict2 = {}
for i in range(0,len(dyr)):
    my_dict2[dyr[i]] = navn_dyr[i]
print(my_dict2)


dyr_dict = {"hund": "Kåre",
            "katt": "Karl",
            "fisk": "Bob",
            "ape": "Per",
            "fugl": "Espen"}
for i in dyr_dict:
    print(f"{dyr_dict[i]} er en {i}.")


input()