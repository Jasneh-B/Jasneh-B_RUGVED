# Tally the toss decisions each team has taken. 

import pandas as pd

matches = pd.read_csv('matches.csv')

toss_tally = matches.groupby(['toss_winner', 'toss_decision']).size()

print(f"Toss Decisions Tally: \n{toss_tally}")