import sys
import csv
from collections import Counter, defaultdict
from statistics import mean, stdev

filename = sys.argv[1] if len(sys.argv) > 1 else '/workspaces/codespaces-blank/2024_fb_ads_president_scored_anon.csv'

# Read data
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

columns = reader.fieldnames
num_rows = len(data)
print(f"\nRows: {num_rows}, Columns: {len(columns)}\n")

for col in columns:
    values = [row[col] for row in data if row[col] != '']
    print(f"\nColumn: {col}")
    # Numeric fields
    if col in ['estimated_audience_size', 'estimated_impressions', 'estimated_spend']:
        nums = [float(v) for v in values if v.replace('.', '', 1).isdigit()]
        if nums:
            print(f"  Count: {len(nums)}")
            print(f"  Mean: {mean(nums):.2f}")
            print(f"  Min: {min(nums)}")
            print(f"  Max: {max(nums)}")
            if len(nums) > 1:
                print(f"  Stddev: {stdev(nums):.2f}")
    # Binary flags
    elif col.endswith('_illuminating') or col.endswith('_topic_illuminating'):
        print("  Unique values:", set(values))
        ones = values.count('1')
        zeros = values.count('0')
        print(f"  Count of 1: {ones}, Count of 0: {zeros}")
    # Date
    elif col == 'ad_creation_time':
        print(f"  Earliest: {min(values)}")
        print(f"  Latest: {max(values)}")
    # List/dict string fields
    elif col in ['delivery_by_region', 'demographic_distribution', 'publisher_platforms', 'illuminating_mentions']:
        print(f"  Example value: {values[0]}")
        print(f"  Unique value count: {len(set(values))}")
    # Other text/categorical
    else:
        counts = Counter(values)
        print(f"  Unique values: {len(counts)}")
        print(f"  Most common: {counts.most_common(1)}")
