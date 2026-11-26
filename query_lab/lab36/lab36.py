import matplotlib.pyplot as plt
height1 = [150, 155, 160, 165, 170]
weight1 = [50, 52, 55, 58, 60]
height2 = [155, 160, 165, 170, 175]
weight2 = [55, 58, 62, 65, 70]
height3 = [160, 165, 170, 175, 180]
weight3 = [60, 63, 67, 72, 75]
plt.scatter(height1, weight1, label="Group 1")
plt.scatter(height2, weight2, label="Group 2")
plt.scatter(height3, weight3, label="Group 3")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight for Three Groups")
plt.legend()
plt.grid(True)
plt.show()