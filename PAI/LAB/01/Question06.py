physics_marks = 40
chemistry_marks =78
maths_marks = 82
marks = {
    "Physics": physics_marks,
    "Chemistry": chemistry_marks,
    "Maths": maths_marks
}
average_marks = sum(marks.values()) / len(marks)
top_subject = max(marks, key=marks.get)
print("Your average marks are:", average_marks)
print("The subject with the highest marks is:", top_subject)
