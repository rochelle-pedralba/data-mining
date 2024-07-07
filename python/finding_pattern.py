import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 2: Load the CSV file
csv_file_path = r'C:\Users\roche\Desktop\SUBJECT FOLDERS\3rd Year\2nd Semester\Data Mining\Apriori Algorithm in Jupyter\data-mining\dataset\csv\international_top_terms_cleaned.csv'  # Update this path
df = pd.read_csv(csv_file_path)

# Step 3: Sort the DataFrame
sorted_df = df.sort_values(by='country_name')  # Assuming the column name is 'countries'

# Create a dictionary to hold each country's data
country_data = {}

# Separate each country's data and store it in the dictionary
for country in sorted_df['country_name'].unique():
    country_data[country] = sorted_df[sorted_df['country_name'] == country]

# Example usage: Print the DataFrame for a specific country
print(country_data['Australia'])