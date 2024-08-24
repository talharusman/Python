list_input = input("Enter a list of numbers separated by spaces: ").split()

list_input = [int(i) for i in list_input]
number = int(input("Enter a number: "))
list_input = [i for i in list_input if i >= number]

print("The updated list is:", list_input)
