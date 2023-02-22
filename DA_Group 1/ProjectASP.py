# Importing the necessary libraries
import pandas as pd
import numpy as np

# Loading the data file using pandas
visitor_raw_df = pd.read_excel("Int Monthly Visitor.xlsx")

# give a name to the missing column name
raw_col = list(visitor_raw_df.columns)
raw_col[0] = "year_month"
visitor_raw_df.columns = raw_col

# split the year and month, we only interested in year
# after split, we store year and month columns
visitor_raw_df["year"] = visitor_raw_df["year_month"].str.split().str[0]
visitor_raw_df["month"] = visitor_raw_df["year_month"].str.split().str[1]

# Displaying the loaded data
print(visitor_raw_df.head())

print(visitor_raw_df.columns)pp

# select Asia country column (include year column), put into new df
# filter year
# groupby year
# sum
# sort by top 3



