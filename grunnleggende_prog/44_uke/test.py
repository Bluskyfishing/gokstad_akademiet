import matplotlib.pyplot as plt

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
plt.show()
