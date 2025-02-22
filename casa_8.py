# Open file

filename = "./big-mac-full-index.csv"

# Open pandas

import pandas as pd

df = pd.read_csv(filename)

# Method 4: Using iterrows() method

for index, row in df.iterrows():
    print(f"{row['date']} {row['name']} Dollar Difference: ${int(row['local_price'] - row['dollar_price'])}")

input()
    
# Method 6: Using apply() method

def local_minus_dollar(row):
    return f"{row['date']} {row['name']} Dollar Difference: ${int(row['local_price'] - row['dollar_price'])}"

result = df.apply(local_minus_dollar, axis=1)
for res in result:
    print(res)
