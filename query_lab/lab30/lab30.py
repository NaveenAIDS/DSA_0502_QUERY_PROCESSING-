import matplotlib.pyplot as plt
import numpy as np
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
groups = np.arange(5)
width = 0.35
plt.bar(groups - width/2, means_men, width, label="Men")
plt.bar(groups + width/2, means_women, width, label="Women")
plt.xticks(groups, ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5"])
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.legend()
plt.show()