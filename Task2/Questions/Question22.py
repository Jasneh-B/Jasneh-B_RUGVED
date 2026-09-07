# Visualize the toss outcomes of all teams.

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
toss_winners = matches['toss_winner'].value_counts()
toss_winners.plot(kind='bar', color='green')
plt.title('Toss Outcomes of All Teams')
plt.xlabel('Teams')
plt.ylabel('Tosses Won')
plt.show()
print("Here are the toss outcomes for all teams:")
print(toss_winners)