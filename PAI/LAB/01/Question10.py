numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in numbers.split()]

largest_number = max(numbers)
print("The largest number is:", largest_number)