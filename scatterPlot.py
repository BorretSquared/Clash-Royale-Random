import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

trophies = []
levels = []

with open('data/playerInfo.txt') as file:
    for line in file:
        line = line.strip()  # remove leading/trailing whitespace
        if line:  # check if line is not empty
            trophies.append(int(line.split(" ")[0]))
            levels.append(int(line.split(" ")[1]))

# Use scatter plot with transparency for better readability
plt.scatter(trophies, levels, alpha=0.5, c='blue', edgecolors='w', s=50)

# Add horizontal lines for king tower level up with corrected labels
kingTowerLevels = [1, 2, 3, 5, 7, 10, 14, 18, 22, 26, 30, 34, 38, 42, 54]
kingTowerLabels = {1: 1, 2: 2, 3: 3, 5: 4, 7: 5, 10: 6, 14: 7, 18: 8, 22: 9, 26: 10, 30: 11, 34: 12, 38: 13, 42: 14, 54: 15} # terrible but works
for level in kingTowerLevels:
    plt.axhline(y=level, color='#000000', linestyle='-')
    plt.text(0, level, f'Level {kingTowerLabels[level]}', color='#000000', fontsize=12, verticalalignment='bottom')
    

plt.xlabel('Trophies', fontsize=30)
plt.ylabel('Levels', fontsize=30)
plt.title('TROPHIES VS LEVELS', fontsize=40)

# Add a custom legend
redLine = mlines.Line2D([], [], color='#000000', linestyle='-', label='King Tower Levels')
plt.legend(handles=[redLine], loc='upper left')

# Set x-axis limits
plt.xlim(0, 9000)
plt.ylim(0, 70)

plt.show()
