# Find the total number of matches played in each season.

import pandas as pd

matches = pd.read_csv('matches.csv')

matches_per_season = matches['season'].value_counts().sort_index()

print("Total number of matches played in each season:\n")
for season, count in matches_per_season.items():
    print(f"Season: {season}, Matches Played: {count}")
    
