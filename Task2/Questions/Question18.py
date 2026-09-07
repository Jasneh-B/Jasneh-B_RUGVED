# Compute batting averages and display top 10.

import pandas as pd

deliveries = pd.read_csv("deliveries.csv")


total_runs = deliveries.groupby('batsman')['batsman_runs'].sum()
dismissals = deliveries[deliveries['player_dismissed'].notna()]
total_outs = dismissals.groupby('player_dismissed').size()
batting_average = total_runs / total_outs
batting_average = batting_average
top_10_average = batting_average.sort_values(ascending=False).head(10)

print(f"Top 10 Batting Averages:")
for batsman, average in top_10_average.items():
    print(f"Batsman: {batsman}, Batting Average: {average:.2f}")
