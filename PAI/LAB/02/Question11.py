students_grades = {
    'Talha_Rusman': [85, 90, 78],
    'Fahad': [92, 88, 79],
    'Ragib': [85, 87, 91]
}

def add_grade(student, grade):
    if student in students_grades:
        students_grades[student].append(grade)
    else:
        print(f"Student {student} not found.")

def average_grade(student):
    if student in students_grades:
        grades = students_grades[student]
        average = sum(grades) / len(grades)
        print(f"Average grade for {student} is {average:.2f}")
    else:
        print(f"Student {student} not found.")

def add_student(student):
    if student not in students_grades:
        students_grades[student] = []
        print(f"Student {student} added.")
    else:
        print(f"Student {student} already exists.")

def remove_student(student):
    if student in students_grades:
        del students_grades[student]
        print(f"Student {student} removed.")
    else:
        print(f"Student {student} not found.")

add_grade('Talha_Rusman', 95)
average_grade('Talha_Rusman')
add_student('Saif')
remove_student('Ragib')

print(students_grades)
