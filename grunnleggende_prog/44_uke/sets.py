a = {1,2,3,4,5}
b = {1,3,5,7}

c = a.union(b)
print("Union", c)

d = a.intersection(b)
print("Intersection", d)

e = a.difference(b)
print("Difference", e)

f = a.symmetric_difference(b)
print("Symmetric differece", f)
