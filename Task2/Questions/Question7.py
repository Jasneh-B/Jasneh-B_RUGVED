# Find the team which won the match by the highest and lowest number of runs.

import pandas as pd

matches = pd.read_csv('matches.csv')


max_run_win = matches.loc[matches['win_by_runs'].idxmax()]

runs_gt_zero = matches[matches['win_by_runs'] > 0]
min_run_wins = runs_gt_zero[runs_gt_zero['win_by_runs'] == runs_gt_zero['win_by_runs'].min()]

print(f"\nMatch with the highest run win: {max_run_win['team1']} vs {max_run_win['team2']} - Winner: {max_run_win['winner']} by {max_run_win['win_by_runs']} runs\n")
print("Matches with the lowest run win:")
print(min_run_wins[['team1', 'team2', 'winner', 'win_by_runs']].to_string(index=False))
