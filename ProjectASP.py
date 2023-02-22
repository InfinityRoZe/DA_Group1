# Importing the necessary libraries
import pandas as pd
import numpy as np

# Loading the data file using pandas
visitor_raw_df = pd.read_excel("Int Monthly Visitor.xlsx")

# give a name to the missing column name
raw_col = list(visitor_raw_df.columns)
raw_col[0] = "Year_Month"
visitor_raw_df.columns = raw_col

# split the year and month, we only interested in year
# after split, we store year and month columns
visitor_raw_df["Year"] = visitor_raw_df["Year_Month"].str.split().str[0]
visitor_raw_df["Month"] = visitor_raw_df["Year_Month"].str.split().str[1]

# Displaying the loaded data
print(visitor_raw_df.head())
print(visitor_raw_df.columns)

# select countries from Others Region column (include year column), put into new df
OthersRegion_df = visitor_raw_df[[' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ', 'Year']]

print(OthersRegion_df)

# filter year


# groupby year

# sum

# sort by top 3
