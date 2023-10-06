
mylist1 = ["a","b","c"]
mylist2 = [1,2,3]
newdict = {}

#for i in mylist1:
#    for j in mylist2:
#        newdict[i] = j
#        mylist2.remove(j)
#        break



x = zip(mylist1,mylist2)
mydict = dict(x)


for i in mydict:
    print(mydict[i],i)