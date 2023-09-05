def lengde_konverterer(lengde):
    fot = lengde * 3.28084
    return fot

lengde = float(input("Skriv inn lengde i Meter: "))

print(f"{lengde}m er {lengde_konverterer(lengde)}fot.\n")


def temp_konverterer(temp):
    farenheit = temp * (9/5) + 32
    return farenheit

temp = float(input("Skriv inn temperatur i Celcius: "))
print(f"{temp}°C er {temp_konverterer(temp)}°F\n")


input()