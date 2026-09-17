import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

df = pd.read_json(url)

print("First 5 Records:")
print(df.head())