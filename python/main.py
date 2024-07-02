
# May separate files for each step kasi ang dami

# Dito muna yung temporary na code sa gagamitin natin sa pag analyze ng data
# Tsaka nalang ilipat sa jupyter notebook ulit para mapakita step by step

#step 1: import libraries

import numpy as np 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules

#step 2: import data

data = pd.read_excel(r"C:\Users\roche\Desktop\SUBJECT FOLDERS\3rd Year\2nd Semester\Data Mining\Apriori Algorithm in Jupyter\Online Retail.xlsx") 
data.head() 

data.columns

Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
       'UnitPrice', 'CustomerID', 'Country'],
      dtype='object')

#step 3: Cleaning the data - disregarded code
#this will be executed in BigQuery MySQL

#same procedure, dropping rows without scores and ranks

# Stripping extra spaces in the description 
data['Description'] = data['Description'].str.strip() 
  
# Dropping the rows without any invoice number 
data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True) 
data['InvoiceNo'] = data['InvoiceNo'].astype('str') 
  
# Dropping all transactions which were done on credit 
data = data[~data['InvoiceNo'].str.contains('C')]

# Transactions done in France 
basket_France = (data[data['Country'] =="France"] 
          .groupby(['InvoiceNo', 'Description'])['Quantity'] 
          .sum().unstack().reset_index().fillna(0) 
          .set_index('InvoiceNo')) 
  
# Transactions done in the United Kingdom 
basket_UK = (data[data['Country'] =="United Kingdom"] 
          .groupby(['InvoiceNo', 'Description'])['Quantity'] 
          .sum().unstack().reset_index().fillna(0) 
          .set_index('InvoiceNo')) 
  
# Transactions done in Portugal 
basket_Por = (data[data['Country'] =="Portugal"] 
          .groupby(['InvoiceNo', 'Description'])['Quantity'] 
          .sum().unstack().reset_index().fillna(0) 
          .set_index('InvoiceNo')) 
  
basket_Sweden = (data[data['Country'] =="Sweden"] 
          .groupby(['InvoiceNo', 'Description'])['Quantity'] 
          .sum().unstack().reset_index().fillna(0) 
          .set_index('InvoiceNo'))

#step 5: Hot coding of data

# Defining the hot encoding function to make the data suitable  
# for the concerned libraries 
def hot_encode(x): 
    if(x<= 0): 
        return 0
    if(x>= 1): 
        return 1
  
# Encoding the datasets 
basket_encoded = basket_France.map(hot_encode) 
basket_France = basket_encoded 
  
basket_encoded = basket_UK.map(hot_encode) 
basket_UK = basket_encoded 
  
basket_encoded = basket_Por.map(hot_encode) 
basket_Por = basket_encoded 
  
basket_encoded = basket_Sweden.map(hot_encode) 
basket_Sweden = basket_encoded 

#step 6: Building the models and analyzing the results

# Building the model 
frq_items = apriori(basket_France.astype('bool'), min_support = 0.06, use_colnames = True) 
  
# Collecting the inferred rules in a dataframe 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
display(rules)

frq_items = apriori(basket_UK.astype('bool'), min_support = 0.02, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
display(rules)

frq_items = apriori(basket_Por.astype('bool'), min_support = 0.05, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
display(rules)

frq_items = apriori(basket_Sweden.astype('bool'), min_support = 0.04, use_colnames = True) 
rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
display(rules) 