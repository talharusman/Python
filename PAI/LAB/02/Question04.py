def employee(name, salary = 10000):
    tax = salary*(2/100)
    salary -= tax

    return name, salary

name = input("Enter the employee name: ")
salary = int(input("Enter the empolyee salary: "))

print("(Name, Salary) ->",employee(name, salary))