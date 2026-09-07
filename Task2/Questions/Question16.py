# Calculate total number of runs scored by each batsman and display top 10.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv')

top_batsmen = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

print("Top 10 Batsmen by Total Runs Scored:\n")
for batsman, total_runs in top_batsmen.items():
    print(f"Batsman: {batsman}, Total Runs: {total_runs}")
