def table():
    for i in range(1,11):
        for j in range(1,11):
            if j == 10:
                print(f"{i}*{j}={i * j}")
            else:
                print(f"{i}*{j}={i * j}", end="\t") #Needed \t instead of " " in end=
#idk
table()