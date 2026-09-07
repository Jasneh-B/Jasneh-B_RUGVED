#Find the teams where the result was a tie.

import pandas as pd

matches = pd.read_csv('matches.csv')

tied_matches = matches[matches['result'] == 'tie']
tied_teams = sorted(list(set(tied_matches['team1']).union(set(tied_matches['team2']))))

print(f"Teams where the result was a tie: {', '.join(tied_teams)}")