import matplotlib.pyplot as plt
import numpy as np
means_men = np.array([22, 30, 35, 35, 26])
means_women = np.array([25, 32, 30, 35, 29])
std_men = np.array([4, 3, 4, 1, 5])
std_women = np.array([3, 5, 2, 3, 3])
groups = np.arange(5)
width = 0.5
plt.bar(
    groups,
    means_men,
    width,
    yerr=std_men,
    capsize=5,
    label="Men"
)
plt.bar(
    groups,
    means_women,
    width,
    bottom=means_men,
    yerr=std_women,
    capsize=5,
    label="Women"
)
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Stacked Bar Plot with Error Bars")
plt.xticks(
    groups,
    ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5"]
)
plt.legend()
plt.show()