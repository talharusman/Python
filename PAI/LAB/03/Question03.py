try:
    list1 = input("Enter the first list (separated by commas): ").split(',')
    list2 = input("Enter the second list (separated by commas): ").split(',')

    list1 = [x.strip() for x in list1]
    list2 = [x.strip() for x in list2]

    if len(list1) != len(list2):
        raise ValueError("Lists must have the same number of elements")

    dictionary = {}
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        dictionary[key] = value

    with open('text03.txt', 'w') as f:
        for key, value in dictionary.items():
            f.write(f"{key}: {value}\n")

    print("Dictionary written to text03.txt")

except ValueError as e:
    print(f"Error: {e}")
except IOError as e:
    print(f"Error writing to file: {e}")