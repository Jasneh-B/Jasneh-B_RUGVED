# Count the total number of normal and tied matches. 

import pandas as pd

matches = pd.read_csv('matches.csv')


match_results = matches['result'].value_counts()
normal_matches = match_results.get('normal', 0)
tied_matches = match_results.get('tie', 0)

print(f"Total number of normal matches: {normal_matches}")
print(f"Total number of tied matches: {tied_matches}")