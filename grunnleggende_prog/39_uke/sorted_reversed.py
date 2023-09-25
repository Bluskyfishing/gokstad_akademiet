#Sort

def num_liste():
    num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    num_list.sort()
    print(num_list)
   

def case_insensitive():
    fruit_list =  ['apple', 'Banana', 'Cherry'] 
    fruit_list.sort(key=str.casefold)
    print(fruit_list)


def tuple_list():
    mytuple = (6, 2, 9, 1, 5, 3)
    reversed_tuple = sorted(mytuple,reverse=True)
    print(tuple(reversed_tuple))


def length(x):
    return len(x)

def len_sort():
    fruit_list = ['apple', 'banana', 'cherry']
    fruit_list.sort(key=length)
    print(fruit_list)


#Reversed

def reversed_list():
    numlist = [1, 2, 3, 4, 5]
    print(list(reversed(numlist)))


def str_reversed():
    txt = "Hello"
    x = list(reversed(txt))
    print(" ".join(x))


def reversed_tuple():
    mytuple = (1, 2, 3, 4, 5)
    print(tuple(reversed(mytuple)))


def reversed_dict(): #lol?
    mydict = {"Isak":"Kul","Brian":"Giga kul","Youko":"Japansk"}
    mydict_reverse = list(reversed(mydict.keys()))

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