class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Marks(Student):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"Algorithm Marks: {self.marks_algo}")
        print(f"Data Science Marks: {self.marks_dataScience}")
        print(f"Calculus Marks: {self.marks_calculus}")

class Result(Marks):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


result = Result("23k-0065", "Talha Rusman", 80, 90, 70)
result.display_info()
result.display_marks()
result.calculate_result()