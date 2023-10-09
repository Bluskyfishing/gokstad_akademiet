#1
def primeNumbers():
    newlist = []
    for i in range(1,11):
        newlist.append(i)
    return newlist

#2 
def tupleEvenNumbers():
    newlist = []
    for i in range(1,21):
        if i % 2 == 0:
            newlist.append(i)
    evenNumbers = tuple(newlist)
    return evenNumbers

#3 
def numbersSquared():
    newdict = {}
    for i in range(1,11):
        newdict[i] = i*i
    return newdict

#4
def listSorted(list):
    list.sort()
    return list

#5
def myfunc(e):
    return len(e)

def lengthSortList(list):
    list.sort(key=myfunc)
    return list

#6
def sortedKeys(dict):
    mylist = list(dict.keys())
    mylist.sort()
    return mylist

#mydict = {10:"Jula",8:"Kåre",1:"Petter"}
#x = sortedKeys(mydict)
#print(x)

#7
def uniqueNumbers(list):
    newlist = []
    for i in list:
        if i in newlist:
            continue
        else:
            newlist.append(i)
    return newlist

#x = uniqueNumbers([1,1,2,2,3])
#print(x)

#8
def smallestAndBiggest(list):
    smallest = list[0]
    biggest = list[0]
    newlist = []
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = i
        if list[i] > biggest:
            biggest = i

    newlist.append(smallest)
    newlist.append(biggest)

    return tuple(newlist)

#x = smallestAndBiggest([1,2,3])
#print(x)

#9
def recurringInList(list1,list2):
    newlist = []
    for i in list1:
        if i in list1 and i in list2 :
            newlist.append(i)
    return(newlist)

#x = [1,2,3,4,5]
#y = [3,4,5,6,7]
#z = recurringInList(x,y)
#print(z)

#10
def numberFrequency(list):
    newdict = {}
    for i in list:
        if i in newdict:
            newdict[i] = newdict.get(i) + 1 
        else:
            newdict[i] = 1  

    return newdict

#x = [1,1,1,2,2,3]
#y = numberFrequency(x)
#print(y)