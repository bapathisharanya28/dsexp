import pandas as pd
student_data = {
    "Roll No": [101, 102, 103, 104],
    "Name": ["Anu", "Bobby", "Cheriy", "Duke"],
    "Department": ["IT", "IT", "CSE", "DS"]
}
df = pd.DataFrame(student_data)
df.to_json("students.json", orient="records", indent=4)
print("JSON file created successfully")