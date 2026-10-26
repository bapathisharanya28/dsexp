import pandas as pd

student_data = {
    "Roll No": [101, 102, 103],
    "Name": ["Anu", "Bobby", "Cherry"],
    "Department": ["IT", "IT", "CSE"],
    "Percentage": [89, 92, 88]
}

course_data = {
    "Course-ID": ["C101", "C102", "C103"],
    "Course-Name": ["Python", "DataScience", "Machine Learning"],
    "Credits": [4, 3, 4]
}

students_df = pd.DataFrame(student_data)
courses_df = pd.DataFrame(course_data)

# Writing multiple DataFrames to different sheets
with pd.ExcelWriter("college-data.xlsx", engine="openpyxl") as writer:

    students_df.to_excel(
        writer,
        sheet_name="Students",
        index=False
    )

    courses_df.to_excel(
        writer,
        sheet_name="Courses",
        index=False
    )

print("Multiple sheets successfully written to college-data.xlsx")