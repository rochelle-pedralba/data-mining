import pandas as pd

# Paths to your CSV files
csv_file_path1 = 'data-mining\dataset\csv\international_top_terms_000000000290.csv'
csv_file_path2 = 'data-mining\dataset\csv\international_top_terms_000000000192.csv'
csv_file_path3 = 'data-mining\dataset\csv\international_top_terms_000000000290.csv'

# Read each CSV file
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)
df3 = pd.read_csv(csv_file_path3)

# Concatenate all DataFrames into one
combined_df = pd.concat([df1, df2, df3])

# Save the concatenated DataFrame to a new CSV file
combined_csv_path = 'data-mining\dataset\csv\international_top_terms_combined.csv'
combined_df.to_csv(combined_csv_path, index=False)