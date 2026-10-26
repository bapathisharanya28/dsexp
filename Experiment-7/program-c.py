import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("First 5 records:")
print(df.head())
print("\nDataset information:")
df.info()
print("\nStatistical summary:")
print(df.describe())
print("\nGroupBy using a single column:")
print(df.groupby("species")["sepal_length"].agg(
    ["count", "sum", "mean", "std", "min", "max"]
))
print("\nGroupBy using multiple columns:")
print(df.groupby(["species", "sepal_width"])["sepal_length"].mean().head(15))
print("\nSummary statistics by species:")
print(df.groupby("species").agg({
    "sepal_length": ["mean", "std", "min", "max"],
    "sepal_width": ["mean", "std", "min", "max"],
    "petal_length": ["mean", "std", "min", "max"],
    "petal_width": ["mean", "std", "min", "max"]
}))
print("\nNumber of records in each species:")
print(df["species"].value_counts())
print("\nAverage petal length by species:")
print(df.groupby("species")["petal_length"].mean())
print("\nAverage petal width by species:")
print(df.groupby("species")["petal_width"].mean())
print("\nMaximum sepal length by species:")
print(df.groupby("species")["sepal_length"].max())
