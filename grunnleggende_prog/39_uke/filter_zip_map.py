#####Filter#####

def oddnumberFinder(x):
    if (x % 2) != 0:
        return True
    else:
        return False

#num = [1, 2, 3, 4, 5, 6]
#oddnumbers = filter(oddnumberFinder,num)
#for i in oddnumbers:
#    print(i)


def lengthfinder(x):
    if len(x) <= 5:
        return True
    else:
        return False

#fruit = ['apple', 'banana', 'cherry', 'date']
#longwords = filter(lengthfinder,fruit)
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


#####Zip#####

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

#mylist = [1,2,3]
#mylist2 = [4,5,6]
#
#mycombinedlist = list(zip(mylist,mylist2))
#print(mycombinedlist)
#
#sum_list = map(zippedlist,mycombinedlist)
#print(list(sum_list))


#Lag en dictionary der nøklene er fra listen ['Anna', 'Bob', 'Charlie'] og verdiene er fra listen [25, 30, 35] ved hjelp av zip. 

def dictZip():
    mykeys = ["Anna","Bob","Charlie"]
    myvalues = [25,30,35]
    x = zip(mykeys,myvalues)
    print(dict(x))


#Kombiner tre lister ved hjelp av zip: ['a', 'b', 'c'], [1, 2, 3], og ['apple', 'banana', 'cherry']. 

def ziplists():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    list3 = ['apple', 'banana', 'cherry']
    x = zip(list1,list2,list3)
    print(list(x))

#Hvordan ville du brukt zip for å splitte en liste av tupler (f.eks. [('a', 1), ('b', 2), ('c', 3)]) i to separate lister? 
#?????????????????


#####Map#####

#Bruk map for å øke alle verdier i listen [1, 2, 3, 4] med 1. 

def increment(num):
    return num + 1

#mylist = [1,2,3,4]
#x = map(increment,mylist)
#print(list(x))


#Konverter alle strengene i listen ['1', '2', '3'] til heltall. 

def strConverter(string):
    return int(string)

#mylist = ["1","2","3"]
#x = map(strConverter,mylist)
#print(list(x))


#Skriv en funksjon som returnerer første bokstav i hvert ord fra listen ['apple', 'banana', 'cherry'] ved hjelp av map. 

def firstletter(letter):
    return letter[0]

#mylist = ["apple","banana","cherry"]
#x = map(firstletter,mylist)
#print(list(x))


#Bruk map for å lage en ny liste der hvert element er lengden av ord fra listen ['apple', 'banana', 'cherry']. 

def wordlength(word):
    return len(word)

#mylist = ["apple","banana","cherry"]
#x = map(wordlength,mylist)
#print(list(x))


#Bruk map for å lage en ny dictionary fra to lister, der den første listen ['a', 'b', 'c'] er nøkler og den andre [1, 2, 3] er verdiene. 

def dictmaker(key, value):
    mydict = {key: value}
    return mydict

mylist1 = ["a", "b", "c"]
mylist2 = [1, 2, 3]

x = map(dictmaker, mylist1, mylist2)
print(list(x))