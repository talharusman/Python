import numpy as np

student_dtype = np.dtype([
    ('name', 'U20'),  # 'U20' means a Unicode string of maximum length 20
    ('age', 'i4'),    # 'i4' means a 4-byte integer
    ('grade', 'f4')   # 'f4' means a 4-byte float
])

students = np.array([
    ('Talha', 20, 85.5),
    ('Raghib', 22, 90.0),
    ('Saif', 21, 78.5),
    ('Fahad', 23, 88.0)
], dtype=student_dtype)


print(students)

print("Names of students:", students['name'])
print("Ages of students:", students['age'])
print("Grades of students:", students['grade'])