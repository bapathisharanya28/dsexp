import pandas as pd

student_data = {
    "Roll No": [101, 102, 103, 104],
    "Name": ["Anu", "Bobby", "Cherry", "Duke"],
    "Department": ["IT", "IT", "CSE", "DS"],
    "Percentage": [89, 92, 88, 85]
}

df = pd.DataFrame(student_data)

df.to_excel(
    "students.xlsx",
    sheet_name="Student-Details",
    index=False
)

print("Data Successfully written to students.xlsx")