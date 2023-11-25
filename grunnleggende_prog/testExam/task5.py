import math 

def celciusToFarenheit(temp):
    try:
        conversion = (int(temp) * 9/5) + 32
    except UnboundLocalError as unBoundLocalErr:
        return unBoundLocalErr
    except ValueError as valErr:
        return valErr
    return conversion

temprature = input("Write temp in celcius: ")
print(celciusToFarenheit(temprature))

def divide(a, b):
    try:
        result = a/b
    except Exception as e:
        return None
    return result

print(divide(10,2))
print(divide(10,0))

def volume_sphere(radius):
    return (4/3) * math.pi * radius**3
print(volume_sphere(10))