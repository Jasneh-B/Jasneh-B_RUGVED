# Count the total number of matches conducted in 2008. 

import pandas as pd


matches = pd.read_csv('matches.csv')


matches_2008 = matches[matches['season'] == 2008].shape[0]

print(f"Total number of matches conducted in 2008: {matches_2008}")