import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)
# Column Selection
print("\nColumn Selection\n")
print(df['Name'])  # Access the 'Name' column

# Accessing Rows
print("\nAccessing Rows\n")
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

# Slicing
print("\nSlicing\n")
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows


# Finding Unique Elements
print("\nFinding Unique Elements\n")
unique_dates = df['Age'].unique()
print(unique_dates)

# Conditional Filtering
print("\nConditional Filtering\n")
high_above_25 = df[df['Age'] > 25]
print(high_above_25)

# Saving DataFrames
df.to_csv('trading_data.csv', index=False)
