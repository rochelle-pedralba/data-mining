import pandas as pd

csv_file_path = 'data-mining\dataset\csv\international_top_terms_combined.csv'
df = pd.read_csv(csv_file_path)

# Filter out rows where either "score" or "rank" column is empty
filtered_df = df[df['score'].notna() & df['rank'].notna()]

# Filter out rows where "rank" is greater than 50 or "score" is less than 50
filtered_df = df[(df['rank'] <= 50) & (df['score'] >= 50)]

# Save the filtered DataFrame to a new CSV file
filtered_csv_path = 'data-mining\dataset\csv\international_top_terms_cleaned.csv'
filtered_df.to_csv(filtered_csv_path, index=False)




