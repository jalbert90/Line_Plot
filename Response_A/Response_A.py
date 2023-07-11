import numpy as np
import matplotlib.pyplot as plt

# Create a NumPy array
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Plot the array
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()