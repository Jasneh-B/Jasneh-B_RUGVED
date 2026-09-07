# Compute the total number of wickets taken by each bowler.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv')

bowler_dismissals = ['caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket']

bowler_wickets_df = deliveries[deliveries['dismissal_kind'].isin(bowler_dismissals)]
top_bowlers = bowler_wickets_df.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False)

print("\nTotal Wickets Taken by Each Bowler:\n")
for bowler, total_wickets in top_bowlers.items():
    print(f"Bowler: {bowler}, Total Wickets: {total_wickets}")