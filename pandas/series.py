import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Accessing by label
print("\nAccessing by label\n")
print(s[2])  # Access the element with label 2 (value 30)

# Accessing by position
print("\nAccessing by position\n")
print(s.iloc[3])  # Access the element at position 3 (value 40)

# Accessing multiple elements
print("\nAccessing multiple elements\n")
print(s[1:4])   # Access a range of elements by label
