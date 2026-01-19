import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]   # X-axis
y = [2, 4, 6, 8, 10]  # Y-axis

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("My First Simple Graph")

# Show the graph
plt.show()