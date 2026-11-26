import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot of Random Distribution")
plt.show()