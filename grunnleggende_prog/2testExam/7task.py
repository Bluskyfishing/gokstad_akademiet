with open("payments.csv", "r") as readFile:
    lines = readFile.readlines()
    readFile.close()

listofOrders = []

for line in lines:
    listofOrders.append(line.rstrip("\n").split(","))
    dictOfOrders = [dict(zip(listofOrders[0], order)) for order in listofOrders[1:]]


mostExpensive = 0
date = None

for mydict in dictOfOrders:
    if float(mydict["amount"]) > mostExpensive:
        mostExpensive = float(mydict["amount"])
        date = mydict["paymentDate"]

print("Most expensive order:", mostExpensive, date)


customerSums = {}

for mydict in dictOfOrders:
    customerName = mydict['customerName']
    amount = float(mydict['amount'])
    customerSums[customerName] = customerSums.get(customerName, 0) + amount
for customer, totalAmount in customerSums.items():
    print(f"Customer: {customer}, Total Amount: {totalAmount}")