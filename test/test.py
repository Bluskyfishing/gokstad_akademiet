def getpow(num, pownum):
    for i in range(pownum):
        num *= num
    return num

cardNum = "53420582349058903488" # - checknumber
total = []

if len(cardNum) > 12:
    for index, strnum in enumerate(cardNum, start = 1):
        num = int(strnum)
        if index % 2 != 0:
            result = num * 2
            if len(str(result)) == 2:
                strResult = str(result)
                result = int(strResult[0]) + int(strResult[1])
            total.append(result)
        else:
            total.append(num)
    if sum(total) % 10 == 0:
        print(sum(total), "Valid")
    else:
        print(sum(total), "Not Valid")
else:
    print(cardNum, "is not 12 numbers!")