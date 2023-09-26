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


#Bruk filter for å hente ut alle par-tall fra en dictionary med tall som nøkler. -----------

def partall(x):
    if (x % 2) == 0:
        return True
    else:
        return False

#partalldic = {"Isak":2,"Per":1,"Thorfinn":4}
#x = filter(partall,partalldic)
#
#for i in partalldic:
#    print(i)    


#Zip

#Bruk zip for å kombinere listen ['a', 'b', 'c'] med listen [1, 2, 3] til en liste av tupler

def ziplist():
    mylist = ["a","b","c"]
    mylist2 = [1,2,3,]
    x = list(zip(mylist,mylist2))
    print(x)


#Kombiner to lister av tall der den ene er [1, 2, 3] og den andre er [4, 5, 6] 
#til en ny liste med summer av parrede elementer ved hjelp av zip og map. 

def zippedlist(list1):
    return sum(list1)

mylist = [1,2,3]
mylist2 = [4,5,6]

mycombinedlist = list(zip(mylist,mylist2))
print(mycombinedlist)

sum_list = map(zippedlist,mycombinedlist)
for i in sum_list:
    print(i)