# Visualize Total Matches vs Winning Matches vs Win Rate for all teams.

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
team1_count = matches['team1'].value_counts()
team2_count = matches['team2'].value_counts()
total_matches = team1_count + team2_count
winning_matches = matches['winner'].value_counts()
win_rate = (winning_matches / total_matches) * 100

data = pd.DataFrame({'Total Matches': total_matches, 'Winning Matches': winning_matches, 'Win Rate %': win_rate})
data.plot(kind='bar', y=['Total Matches', 'Winning Matches'])
plt.title('Total Matches vs Winning Matches')
plt.show()

data.plot(kind='bar', y='Win Rate %', color='red')
plt.title('Win Rate For All Teams')
plt.show()
print(data)
