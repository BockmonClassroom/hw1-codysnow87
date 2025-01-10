# Cody Snow 
# HW1 DS5110
# January 9th, 2025

# Import the pandas library and name it pd
import pandas as pd

# Read the Iris.csv file into a pandas dataframe
df = pd.read_csv('./data/Iris.csv')

# Print the first 5 rows of the data to ensure it was read correctly
print("The first 5 rows of the data are:")
print(df.head())

# Print the entire data frame row by row using the itertuples() function and a foreach loop
for row in df.itertuples():
    print(row)