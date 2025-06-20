import sys
import polars as pl

# Use file path from command line or default to one of your files
filename = sys.argv[1] if len(sys.argv) > 1 else '/workspaces/codespaces-blank/2024_fb_ads_president_scored_anon.csv'

# Load CSV (automatically detects column types)
df = pl.read_csv(filename)

print(f"\nLoaded {filename} with shape {df.shape}\n")

# General descriptive statistics
print("General stats:\n", df.describe())

# Unique value counts (for each column)
print("\nUnique counts:")
for col in df.columns:
    print(f"{col:40s}: {df[col].n_unique()}")

# Most common value for each column (mode)
print("\nMost frequent values (mode):")
for col in df.columns:
    mode = df[col].mode()
    modes = mode.to_list()
    print(f"{col:40s}: {modes[0] if modes else 'N/A'}")


# Aggregation by page_id (mean of selected numerics)
if {'page_id', 'estimated_audience_size', 'estimated_impressions', 'estimated_spend'}.issubset(df.columns):
    grouped = (
        df.group_by('page_id')
        .agg([
            pl.col('estimated_audience_size').mean().alias('audience_size_mean'),
            pl.col('estimated_impressions').mean().alias('impressions_mean'),
            pl.col('estimated_spend').mean().alias('spend_mean')
        ])
    )
    print("\nStats by page_id (mean of numerics):")
    print(grouped.head())

# Aggregation by (page_id, ad_id)
if {'page_id', 'ad_id', 'estimated_audience_size', 'estimated_impressions', 'estimated_spend'}.issubset(df.columns):
    grouped = (
        df.group_by(['page_id', 'ad_id'])
        .agg([
            pl.col('estimated_audience_size').mean().alias('audience_size_mean'),
            pl.col('estimated_impressions').mean().alias('impressions_mean'),
            pl.col('estimated_spend').mean().alias('spend_mean')
        ])
    )
    print("\nStats by (page_id, ad_id) (mean of numerics):")
    print(grouped.head())
