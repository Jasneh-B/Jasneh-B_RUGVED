# Find total runs scored in each season.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

deliv_matches = pd.merge(deliveries, matches[['id', 'season']], left_on='match_id', right_on='id')
runs_per_season = deliv_matches.groupby('season')['total_runs'].sum().sort_index()

print("Total runs scored in each season:\n")
for season, total_runs in runs_per_season.items():
    print(f"Season: {season}, Total Runs: {total_runs}")

