import math 

def meterToFoot(length):
    return length * 3.28084

print(meterToFoot(10))

def volumeCylinder(radius, height):
    return math.pi*radius**2*height

print(f"Radius={4}, height={10}, Volum={volumeCylinder(4,10)}")