liste = [3, 5, 9, 10, 11]

for tall in liste:
    if tall >= 10 or tall <= 5:
        print(tall)
print("")

for tall in liste:
    if tall >= 5 and tall <= 10:
        print(tall)
print("")


index_teller = 0

for tall in liste:
    print(f"Index:{index_teller} Verdi:{tall}")
    index_teller += 1
print("")

index_teller = 0

while index_teller < len(liste):
    print(f"Index:{index_teller} Verdi:{liste[index_teller]}")
    index_teller += 1
print("")


total = 0

for tall in liste:
    total += tall
print(f"Total er alle elementene i listen: {total}")

#print(sum(liste))


input()