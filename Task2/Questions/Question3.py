# Find total count of matches city-wise. 

import pandas as pd


matches = pd.read_csv('matches.csv')

city_total = matches['city'].value_counts().to_dict()

for city, count in city_total.items():
    print(f"{city}: {count} matches")
    