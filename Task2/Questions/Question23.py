# Visualize the top 5 teams with the most wins across all seasons.

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
team_wins = matches['winner'].value_counts()
top_5_teams = team_wins.head(5)
top_5_teams.plot(kind='bar', color='purple')
plt.title('Top 5 Teams With Most Wins')
plt.xlabel('Team Name')
plt.ylabel('Total Wins')
plt.show()
print("Top 5 teams list:")
print(top_5_teams)