import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]  # 5 elements
y = [2, 3, 5, 7]     # 4 elements

# Adjust y to match the length of x
y.append(11)  # Now y has 5 elements

# Now you can plot
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.legend()
plt.show()