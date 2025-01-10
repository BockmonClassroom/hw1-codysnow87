# Cody Snow 
# HW1 DS5110
# January 9th, 2025

# Import the pandas library and name it pd (standard naming convention) 
import pandas as pd

# Read the Iris.csv file into a pandas dataframe from the data folder, 
# which must be in the same parent directory as the folder containing this script
df = pd.read_csv('./data/Iris.csv')

# Print the first 5 rows of the data to ensure it was read correctly
print("\n\nThe first 5 rows of the dataset:")
print(df.head())

# Print the entire data frame using to_markdown/tabulate for better formatting
print("\n\nAll rows in the dataset:")
print(df.to_markdown())