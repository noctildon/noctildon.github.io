"""
Pandas handles data in a tabular format, similar to a spreadsheet or SQL table.
It is a powerful tool for data analysis and manipulation.
"""

import pandas as pd

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [20, 21, 19, 18],
    'height': [165, 180, 175, 190],
    'weight': [60, 70, 65, 80]
})

# read from a csv file
# df = pd.read_csv('data.csv')

print(df)
print(df.head(2))     # the first 2 rows
print(df.tail(2))     # the last 2 rows
print(df.shape)       # the shape of the DataFrame
print(df.columns)     # the column names
print(df.dtypes)      # the data types of each column
print(df.info())      # a concise summary of the DataFrame
print(df['name'])     # the 'name' column
print(df.name)        # the 'name' column

print(df[['name', 'age']])   # the 'name' and 'age' columns
print(df[0:2])               # the first 2 rows
print(df.loc[0])             # the first row
print(df.loc[0:2])           # the first 3 rows
print(df.loc[0, 'name'])     # the first row and the 'name' column
print(df.loc[0:2, 'name'])   # the first 3 rows and the 'name' column

print(df.loc[0:2, ['name', 'age']])  # the first 3 rows and the 'name' and 'age' columns
print(df.iloc[0])             # the first row
print(df.iloc[0:2])           # the first 2 rows
print(df.iloc[0, 0])          # the first row and the first column
print(df.iloc[0:2, 0])        # the first 2 rows and the first column
print(df.iloc[0:2, 0:2])      # the first 2 rows and the first 2 columns

print(df[df.age > 19])        # the rows where the age is greater than 19
print(df[df.age > 19][['name', 'age']])                               # the 'name' and 'age' columns where the age is greater than 19
print(df[df.age > 19][['name', 'age']].reset_index(drop=True))        # Reset the index of the DataFrame
print(df.sort_values(by='age'))                                       # Sort the DataFrame by the 'age' column
print(df.sort_values(by='age', ascending=False))                      # Sort the DataFrame by the 'age' column in descending order
print(df.sort_values(by=['age', 'height']))                           # Sort the DataFrame by the 'age' and 'height' columns
print(df.sort_values(by=['age', 'height'], ascending=[True, False]))  # Sort the DataFrame by the 'age' and 'height' columns in ascending and descending order respectively
print(df.groupby('age').mean())                                       # Group the DataFrame by the 'age' column and calculate the mean of each group
