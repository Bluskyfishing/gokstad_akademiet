import matplotlib.pyplot as plt
from deep_translator import GoogleTranslator

# Create some example data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

# Create a plot
plt.plot(x, y)

# Get the current axis
ax = plt.gca()

# Add an x-axis label
ax.set_xlabel("X-axis Label")

# Show the plot
#plt.show()

DICESTAT = [0] * 6
amountRolls = 10

DICESTAT[5] += 3

labelList = ["One","Two","Three","Four","Five","Six"]
myList = []
for i in range(len(labelList)):
    x = f"{labelList[i]}:({(DICESTAT[i])}) \n{(DICESTAT[i]/amountRolls)*100:.1f} %"
    myList.append(x)

print(myList)

tall = "1"
translated = GoogleTranslator(source="en", target="no").translate(tall)
print(tall)