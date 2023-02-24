# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the data file
# Displaying the loaded data
visitor_raw_df = pd.read_excel("Project_File.xlsx")
print(visitor_raw_df)

# give a name to the missing column name
raw_col = list(visitor_raw_df.columns)
raw_col[0] = "Year_Month"
visitor_raw_df.columns = raw_col

# split the year and month, we only interested in year
# after split, we store year and month columns
visitor_raw_df["Year"] = visitor_raw_df["Year_Month"].str.split().str[0]
visitor_raw_df["Month"] = visitor_raw_df["Year_Month"].str.split().str[1]

# select countries from Others Region column (include year column), put into new df
OthersRegion_df = visitor_raw_df[[' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ', 'Year']]
print(OthersRegion_df.head())
print(OthersRegion_df.columns)

# filter year
filter_df = OthersRegion_df[(OthersRegion_df['Year'] > "2007") & (OthersRegion_df['Year'] < "2018")]
print(filter_df)

# sum
FilteredSumOthersRegion_df = filter_df.iloc[:, [0, 1, 2, 3, 4]]
print(FilteredSumOthersRegion_df.sum())

# sort by top 3
top3_df = FilteredSumOthersRegion_df.sum(axis=0).sort_values(ascending= False)[:3]
print(top3_df)

# bar chart