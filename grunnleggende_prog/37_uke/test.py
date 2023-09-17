#Ig

import re

gjetteOrd = input('Skriv inn et ord som skal gjettes: ')
antallLiv = int(input('Velg antall liv spilleren skal ha: '))

secretString = list(re.sub(r"[^\s]", "_", gjetteOrd))
playerHP = antallLiv

while playerHP != 0:
    print(f"HP: {playerHP}")
    print("".join(secretString))
    guessLetter = input('Gjett en bokstav: ')
    matches = False
    for match in re.finditer(guessLetter, gjetteOrd):
        matches = True
        secretString[match.start() : match.end()] = guessLetter
    if not matches: playerHP -= 1
    if playerHP == 0: print("You lost!")
    if list(gjetteOrd) == secretString:
        playerHP = 0
        print("You won!")


#Ar
guessPhrase = input("Guess word: ").lower()
hp = 3

letters = {}
hiddenString = ""
numSpaces = 0
for i, letter in enumerate(guessPhrase):
    if letter == " ":
        hiddenString += " "
        numSpaces += 1
        continue 
    try:
        letters[letter].add(i)
    except KeyError:
        letters[letter] = set()
        letters[letter].add(i)
    hiddenString += "_"
print(letters)
lettersGuessed = 0
print(hiddenString)
while hp > 0 and lettersGuessed < len(guessPhrase) - numSpaces:
    guessLetter = input("Guess a letter: ").lower()
    if len(guessLetter) > 1:
        print("Please input one letter")
        continue
    if guessLetter in letters:
        for i in letters[guessLetter]:
            hiddenString = hiddenString[:i] + guessLetter + hiddenString[i + 1:]
            lettersGuessed += 1
    else:
        hp -= 1
    #print(f"letters: {numLetters} lettersGuessed: {lettersGuessed}")
    print(f"HP: {hp}")
    print(hiddenString)