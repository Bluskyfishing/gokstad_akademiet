names = ["ina","phillip","jo","aleksandria","anna"] 

for name in names:
    print("first letter=", name[0], "length=",len(name))


longestName = names[0]
shortestName = names[0]
for name in names:
    if len(name) > len(longestName):
        longestName = name
    elif len(name) < len(shortestName):
        shortestName = name

print(longestName, shortestName)


for name in names:
    if name == name[::-1]:
        print(name)


