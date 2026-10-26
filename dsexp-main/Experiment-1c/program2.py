import pandas as pd

# Reading an Excel file
df = pd.read_excel(
    "students.xlsx",
    sheet_name="Student-Details"
)

print("Data read from Excel File:")
print(df)