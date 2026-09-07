# Find the cities where the maximum and minimum number of matches were conducted. 


import pandas as pd


matches = pd.read_csv('matches.csv')

city_count = matches['city'].value_counts()
max, max_count = city_count.idxmax(), city_count.max()
min, min_count = city_count.idxmin(), city_count.min()

print(f"City with maximum matches: {max} ({max_count} matches)")
print(f"City with minimum matches: {min} ({min_count} matches)")