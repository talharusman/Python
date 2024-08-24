marks_dict = {}

print("Enter marks for 3 subjects:")
marks_dict["Maths"] = float(input("Maths: "))
marks_dict["Science"] = float(input("Science: "))
marks_dict["English"] = float(input("English: "))
total_marks = sum(marks_dict.values())
average_marks = total_marks / len(marks_dict)
percentage = (total_marks / 300) * 100
print("\nResults:")
print("Average Marks:", average_marks)
print("Percentage:", percentage)
