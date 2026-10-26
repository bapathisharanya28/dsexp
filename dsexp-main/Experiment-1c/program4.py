import pandas as pd

# Reading all sheets
excel_data = pd.read_excel(
    "college-data.xlsx",
    sheet_name=None
)

print("Available Sheets:")
print(excel_data.keys())

print("\nStudent Sheet:")
print(excel_data["Students"])

print("\nCourse Sheet:")
print(excel_data["Courses"])