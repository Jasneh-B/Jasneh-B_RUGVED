# Find the players who have won ‘Player of the Match’ more than 3 times.

import pandas as pd

matches = pd.read_csv('matches.csv')

potm_counts = matches['player_of_match'].value_counts()
potm_gt_3 = potm_counts[potm_counts > 3]

print("Players who have won 'Player of the Match' more than 3 times:")
for player, count in potm_gt_3.items():
    print(f"{player}: {count} times")

