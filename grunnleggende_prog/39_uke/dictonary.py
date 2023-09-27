#Opprett en dictionary med 5 nøkkel-verdi par, der nøklene er frukt og verdiene er deres farger.
 
fruits = {"apple":"red","pear":"green","grape":"purple","banana":"yellow","watermelon":"green"}

#Legg til et nytt nøkkel-verdi par til den eksisterende dictionaryen. 
#Slett et nøkkel-verdi par fra dictionaryen ved hjelp av nøkkelen. 

def firstList():
    fruits["citron"] = "yellow"
    fruits.pop("banana")
    print(fruits)

#Bruk en for-løkke for å skrive ut alle nøklene i dictionaryen.
 
def allKeys():
    for i in fruits:
        print(i)

#Bruk en for-løkke for å skrive ut alle verdiene i dictionaryen. 

def allValues():
    for i in range(len(fruits)):
        x = fruits.values()
        y = list(x) 
        print(y[i])

#Fra to lister: Gitt to lister keys = ['a', 'b', 'c'] og values = [1, 2, 3], lag en dictionary ved å koble sammen elementene fra begge listene. 

def twoLists():
    keys = ["a","b","c"]
    values = [1,2,3]

    x = zip(keys,values)
    mydict = dict(x)
    print(mydict)

#Fra liste med tupler: Gitt en liste med tupler items = [('a', 1), ('b', 2), ('c', 3)], konverter den til en dictionary. 

def tupleDict():
    tupleritems = [('a', 1), ('b', 2), ('c', 3)]
    tuplerdict = dict(tupleritems)
    print(tuplerdict)

#Nøkler fra liste, fast verdi: Gitt en liste ['apple', 'banana', 'cherry'], lag en dictionary hvor hvert element i listen er en nøkkel, og verdien for hver nøkkel er 'fruit'. 

def sameValueDict():
    mylist1 = ['apple', 'banana', 'cherry']
    mylist2 = ["fruit"]
    newdict = {}

    for i in mylist1:
        for j in mylist2:
            newdict[i] = j
    print(newdict)

#Fra liste, bruk indeks: Gitt en liste ['zero', 'one', 'two', 'three'], lag en dictionary hvor nøklene er indeksene (0, 1, 2, osv.) og verdiene er elementene fra listen. 

def indexDict():
    values = ['zero', 'one', 'two', 'three']
    newdict = {}
    index = 0

    for i in values:
        newdict[i] = index
        index += 1 
    print(newdict)

#Opprett nested dictionary: Gitt to lister students = ['Anna', 'Bob', 'Charlie'] og grades = [85, 90, 78], 
#lag en dictionary hvor hver student er en nøkkel, og verdien er en annen dictionary med nøkkel-verdi par for fag (f.eks. 'math') og karakter. 

def nestedDict():
    students = ['Anna', 'Bob', 'Charlie'] 
    subjects = ["math","science","english"]
    grades = [85, 90, 78]
    mydict = {}

    for i in range(len(students)):
        student_name = students[i]
        student_grades = {subjects[i]: grades[i]}
        mydict[student_name] = student_grades

    print(mydict) 