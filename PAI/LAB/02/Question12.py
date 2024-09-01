list1 = input("Enter the elements of the first list separated by space: ").split()
list2 = input("Enter the elements of the second list separated by space: ").split()

if len(list1) != len(list2):
    print("Error: Both lists must have the same number of elements.")
else:
    result_dict = {}
    for i in range(len(list1)):
        result_dict[list1[i]] = list2[i]
    
    print("Resulting dictionary:", result_dict)
