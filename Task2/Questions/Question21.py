# Find the distribution of the teams who won the matches.

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
winner_distribution = matches['winner'].value_counts()
winner_distribution.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 10))
plt.title('Distribution of Winning Teams')
plt.ylabel('')
plt.show()
print("Distribution of match winners:")
print(winner_distribution)
