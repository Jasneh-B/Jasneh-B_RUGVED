# Find the umpires who umpired the maximum number of times.

import pandas as pd

matches = pd.read_csv('matches.csv')

all_umpires = pd.concat([matches['umpire1'], matches['umpire2'], matches['umpire3']])

umpire_counts = all_umpires.value_counts()

max_matches = umpire_counts.max()
most_frequent_umpires = umpire_counts[umpire_counts == max_matches]

print(f"Maximum Matches Umpired: {max_matches}")
print(most_frequent_umpires.to_string(header=False))