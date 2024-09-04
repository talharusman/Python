try:
    name = input("Enter employee name: ")
    CNIC = input("Enter employee CNIC number: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))

    with open("text04.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"CNIC: {CNIC}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Salary: {salary:.2f}\n")

    print("Employee bio_data saved to text04.txt")

    contact_number = input("Enter employee contact number: ")

    with open("text04.txt", "a") as f:
        f.write(f"Contact Number: {contact_number}\n")

    print("Contact number appended to text04.txt")

    with open("text04.txt", "r") as f:
        print("\n\n")
        print("Employee bio_data:")
        print(f.read())

except ValueError as e:
    print(f"Error: Invalid input - {e}")
except IOError as e:
    print(f"Error writing to file: {e}")