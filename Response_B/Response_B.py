import numpy as np
import matplotlib.pyplot as plt

# Create a NumPy array
x = np.arange(10)
y = x**2

# Plot the line plot
plt.plot(x, y, color="red", linewidth=2)
plt.show()
print(x)