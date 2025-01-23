import pandas as pd

# Example DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 22, 34, 42]}
df = pd.DataFrame(data)

# Iterate over the 'Name' column
for index, row in df.iterrows():
    df.at[index, 'Name'] = 'Bob'

print (df)