
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement calculate_bonus method")

    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary:.2f}"

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring someone.")


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(f"{self.name} is writing code.")

class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.30

emp = Employee("Raghib", 50000)
print(emp)  # Employee: Raghib, Salary: $50000.00

mgr = Manager("Fahad ", 70000)
print(mgr.calculate_bonus())  # 14000.0
mgr.hire()  # Fahad is hiring someone.

dev = Developer("Umer", 60000)
print(dev.calculate_bonus())  # 6000.0
dev.write_code()  # Umer is writing code.

sen_mgr = SeniorManager("Talha Rusman", 80000)
print(sen_mgr.calculate_bonus())  # 24000.0
sen_mgr.hire()  # Talha Rusman is hiring someone.
