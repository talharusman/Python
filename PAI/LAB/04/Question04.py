class Employee:
    def __init__(self):
        self.name = ""
        self.monthly_salary = 0
        self.tax_percentage = 0

    def get_data(self):
        self.name = input("Enter employee name: ")
        self.monthly_salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter tax percentage: "))

    def Salary_after_tax(self):
        tax_amount = (self.monthly_salary * self.tax_percentage) / 100
        return self.monthly_salary - tax_amount

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage

employee1 = Employee()

employee1.get_data()
salary_after_tax = employee1.Salary_after_tax()
print(f"Salary after tax: {salary_after_tax:.2f}")
employee1.update_tax_percentage(3)

salary_after_tax = employee1.Salary_after_tax()
print(f"Salary after tax (updated): {salary_after_tax:.2f}")