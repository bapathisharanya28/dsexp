import pandas as pd
from io import StringIO
json_data = """
[
    {
        "RollNo": 101,
        "Name": "Anu",
        "Marks": 89
    },
    {
        "RollNo": 102,
        "Name": "Bobby",
        "Marks": 92
    },
    {
        "RollNo": 103,
        "Name": "Charitha",
        "Marks": 88
    }
]
"""
df = pd.read_json(StringIO(json_data))
print("Parsed JSON Data")
print(df)