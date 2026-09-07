# Find the venue where the team won by the highest and lowest number of runs. 

import pandas as pd

matches = pd.read_csv('matches.csv')

max_run_win = matches.loc[matches['win_by_runs'].idxmax()]
run_wins = matches[matches['win_by_runs'] > 0]
min_run_wins = run_wins[run_wins['win_by_runs'] == run_wins['win_by_runs'].min()]

venue_max = max_run_win['venue']
venues_min = min_run_wins['venue'].unique().tolist()

print(f"\nVenue where the team won by the highest number of runs: {venue_max}\n")
print("Venues where the team won by the lowest number of runs:")
for venue in venues_min:
    print(venue)