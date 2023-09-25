#Filter

def oddnumberFinder(x):
    if (x % 2) != 0:
        return True
    else:
        return False

#num = [1, 2, 3, 4, 5, 6]
#oddnumbers = filter(oddnumberFinder,num)
#for i in oddnumbers:
#    print(i)


def wordLength(x):
    if len(x) <= 5:
        return True
    else:
        return False

#fruit = ['apple', 'banana', 'cherry', 'date']
#longwords = filter(wordLength,fruit)
#print(list(longwords))


def negativeBeGone(x):
    if x > 0:
        return True
    else:
        return False

#mytuple = (-5, -3, 2, 4, -1, 6)
#positivenNum = filter(negativeBeGone,mytuple)
#print(tuple(positivenNum))

# Bruk en kombinasjon av filter og map for å finne alle kvadrater av tallene i listen [1, 2, 3, 4, 5] som er større enn 10. 
#def greaterThan10(x):
#    if x * x > 10:
#        return True
#    else:
#        return False
#
#num = [1, 2, 3, 4, 5]
#
#bignum = filter(greaterThan10,num)
#print(list(bignum))

#Med filter og map:

#def squared(x):
#    return x * x
#def greatherThan10(x):
#    if x > 10:
#        return True
#    else:
#        return False
#    
#squaredList = list(map(squared,num))
#numgreaterThan10 = list(filter(greatherThan10,squaredList))
#print(numgreaterThan10)


#Bruk filter for å hente ut alle par-tall fra en dictionary med tall som nøkler. 

def partall(x):
    if (x % 2) == 0:
        return True
    else:
        return False

partalldic = {"Isak":2,"Per":1,"Thorfinn":4}
x = filter(partall,partalldic)

