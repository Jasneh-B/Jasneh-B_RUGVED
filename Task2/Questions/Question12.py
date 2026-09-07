# Compute the average runs scored in matches in all the venues.

import pandas as pd

deliveries = pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

match_runs = deliveries.groupby('match_id')['total_runs'].sum().reset_index()

match_venue = pd.merge(match_runs, matches[['id', 'venue']], left_on='match_id', right_on='id')

venue_stats = match_venue.groupby('venue')['total_runs'].agg(
    avg_runs_per_match='mean',
    matches_count='count',
    total_runs='sum'
).sort_values(by='avg_runs_per_match', ascending=False)

print("Average runs scored in matches in all the venues:\n")
for venue, stats in venue_stats.iterrows():
    print(f"Venue: {venue}")
    print(f"Average Runs per Match: {stats['avg_runs_per_match']:.2f}")
    print(f"Total Matches: {stats['matches_count']}")
    print(f"Total Runs: {stats['total_runs']}\n")