with open("secretText.txt", "r", encoding="iso-8859-1") as rfile:
    for line in rfile:
        for word in line.split("|"):
            for c in word.split(","):
                if c.isdigit():
                    print(chr(int(c)), end="")
            print(" ", end="")
        print("")