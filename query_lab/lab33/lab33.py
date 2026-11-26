import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(
    x, y,
    marker='o',
    facecolors='none',
    edgecolors='black'
)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot with Empty Circles")
plt.show()