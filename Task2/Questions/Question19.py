# Visualize toss decisions across all seasons.

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
toss_data = matches.groupby(['season', 'toss_decision']).size().unstack()
toss_data.plot(kind='bar')
plt.title('Toss Decisions Across All Seasons')
plt.xlabel('Season')
plt.ylabel('Number of Tosses')
plt.show()
print("Showing the chart for toss decisions now.")