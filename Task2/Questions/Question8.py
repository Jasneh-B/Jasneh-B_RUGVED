# Calculate mean, median and standard deviation of ‘win_by_runs’ 

import pandas as pd

matches = pd.read_csv('matches.csv')


mean_all, median_all, std_all = matches['win_by_runs'].mean(), matches['win_by_runs'].median(), matches['win_by_runs'].std()


print(f"Mean: {mean_all:.2f}")
print(f"Median: {median_all:.2f}")
print(f"Standard Deviation: {std_all:.2f}\n")



print("For matches where win_by_runs > 0")
runs_gt_zero = matches[matches['win_by_runs'] > 0]
mean_gt0, median_gt0, std_gt0 = runs_gt_zero['win_by_runs'].mean(), runs_gt_zero['win_by_runs'].median(), runs_gt_zero['win_by_runs'].std()

print(f"Mean: {mean_gt0:.2f}")
print(f"Median: {median_gt0:.2f}")
print(f"Standard Deviation: {std_gt0:.2f}")