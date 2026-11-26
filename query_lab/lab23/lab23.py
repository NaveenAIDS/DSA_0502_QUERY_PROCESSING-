import matplotlib.pyplot as plt
import os

x = []
y = []

file_path = os.path.join(os.path.dirname(__file__), "test.txt")

with open(file_path, "r") as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

plt.plot(x, y, marker='o')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph")

plt.show()