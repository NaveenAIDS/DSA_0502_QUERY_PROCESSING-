import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(20, 500, 50)
plt.scatter(x, y, s=sizes, alpha=0.6)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot with Balls of Different Sizes")
plt.show()