cloths = ["pants","tshirt","sweater","hoody","hat"]

colors = ["blue","red","yellow","green","purple"]

print(colors[0], cloths[0])

print(cloths[0], cloths[-1])

print(list(reversed(sorted((cloths)))))

names = ("ole","kåre","per","john","mordi")
ages = (22,32,22,13,80)

dictPersons = dict(zip(names,ages))

for name, age in dictPersons.items():
    print(name,"is", age)