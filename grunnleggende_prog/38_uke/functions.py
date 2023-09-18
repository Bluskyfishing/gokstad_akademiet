#def add(x,y):
#    return x + y
#
#x = 23 
#y = 56 
#
#
#print(f"sum = {add(x,y)}")

#x = 43 
#y = 0

#print(f"sum = {add(x,y)}")

#global variabel 

_sum = 0

def add(a:float,b:float):
    summen = a + b 
    return summen

def sub(a:float, b:float):
    return a - b 

def div(a:float,b:float):
    try:
        return a / b
    except ZeroDivisionError:
        return("Dette går ikke!")

print(div(20,0))