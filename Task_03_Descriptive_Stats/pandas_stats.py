import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) > 1 else '/workspaces/codespaces-blank/2024_fb_ads_president_scored_anon.csv'

df = pd.read_csv(filename)

print(f"\nLoaded {filename} with shape {df.shape}\n")
print("General stats:\n", df.describe(include='all'))
print("\nUnique counts:\n", df.nunique())
print("\nMost frequent values:\n", df.mode().iloc[0])

# Aggregation by page_id
if 'page_id' in df.columns:
    print("\nStats by page_id (mean of numeric):")
    print(df.groupby('page_id')[['estimated_audience_size','estimated_impressions','estimated_spend']].mean().head())

# Aggregation by (page_id, ad_id)
if 'ad_id' in df.columns:
    print("\nStats by (page_id, ad_id) (mean of numeric):")
    print(df.groupby(['page_id','ad_id'])[['estimated_audience_size','estimated_impressions','estimated_spend']].mean().head())
