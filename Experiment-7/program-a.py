import pandas as pd
data = {
    "Name": ["Ravi", "Sita", "Arun", "Priya", "Kiran", "Anil", "Lakshmi", "Rahul"],
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Year": [2, 2, 3, 3, 2, 3, 3, 2],
    "Marks": [85, 90, 78, 88, 75, 82, 95, 70]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nGroup by Department:")
for department, group in df.groupby("Department"):
    print(f"\nDepartment: {department}")
    print(group)
print("\nAverage marks by Department:")
print(df.groupby("Department")["Marks"].mean())
print("\nGroup by Department and Year:")
for key, group in df.groupby(["Department", "Year"]):
    print(f"\nGroup: {key}")
    print(group)
print("\nAverage marks by Department and Year:")
print(df.groupby(["Department", "Year"])["Marks"].mean())
