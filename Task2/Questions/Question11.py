# Find all deliveries where the batsman scored a six.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv')

sixes = deliveries[deliveries['batsman_runs'] == 6]
sixes_count = len(sixes)

print(f"Total number of deliveries where the batsman scored a six: {sixes_count}\n")
  
