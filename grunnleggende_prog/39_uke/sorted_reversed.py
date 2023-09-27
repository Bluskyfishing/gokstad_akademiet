#####Sort#####

#Sorter listen [3, 1, 4, 1, 5, 9, 2, 6, 5] i stigende rekkefølge. 

def num_liste():
    num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    num_list.sort()
    print(num_list)
   
#Sorter listen ['apple', 'Banana', 'Cherry'] alfabetisk, uavhengig av store/små bokstaver. 

def case_insensitive():
    fruit_list =  ['apple', 'Banana', 'Cherry'] 
    fruit_list.sort(key=str.casefold)
    print(fruit_list)

#Sorter tuplet (6, 2, 9, 1, 5, 3) i synkende rekkefølge. 

def tuple_list():
    mytuple = (6, 2, 9, 1, 5, 3)
    reversed_tuple = sorted(mytuple,reverse=True)
    print(tuple(reversed_tuple))

#Sorter listen med ord ['apple', 'banana', 'cherry'] basert på lengden av hvert ord. 

def length(x):
    return len(x)

#Sorter en liste med dictionaries basert på en bestemt nøkkel.
 
def len_sort():
    fruit_list = ['apple', 'banana', 'cherry']
    fruit_list.sort(key=length)
    print(fruit_list)


#####Reversed#####

#Reverser listen [1, 2, 3, 4, 5]. 

def reversed_list():
    numlist = [1, 2, 3, 4, 5]
    print(list(reversed(numlist)))

#Konverter en streng 'hello' til en liste og reverser den ved hjelp av reversed. 

def str_reversed():
    txt = "Hello"
    x = list(reversed(txt))
    print(" ".join(x))

#Reverser tuplet (1, 2, 3, 4, 5). 

def reversed_tuple():
    mytuple = (1, 2, 3, 4, 5)
    print(tuple(reversed(mytuple)))

#Hvordan ville du brukt reversed for å reversere nøklene i en dictionary? 

def reversed_dict(): #lol?
    mydict = {"Isak":"Kul","Brian":"Giga kul","Youko":"Japansk"}
    mydict_reverse = list(reversed(mydict.keys()))

#Reverser rekkefølgen av ord i strengen 'Python er gøy' ved hjelp av reversed.
 
def reverseKeys(dictionary):
    for key in list(dictionary.keys()):
        reverseKey = key[::-1]
        value = dictionary.pop(key)
        dictionary[reverseKey] = value
dic = {"isak": 1, "arnas": 2}
reverseKeys(dic)
print(dic)


def reversed_string():
    txt = "Python is fun"
    rtxt = list(reversed(txt))
    print("".join(rtxt))