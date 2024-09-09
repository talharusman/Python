import json

try:
    num = int(input('Enter the number of people: '))
    people_dict = {}

    for i in range(num):
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        people_dict[name] = age

    with open('LAB03/Task5.json', 'w') as file_obj:
        json.dump(people_dict, file_obj)

except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(str(e))

try:
    with open('LAB03/Task5.json', 'r') as file_obj:
        people_dict = json.load(file_obj)

        # Find the person with the maximum age
        max_age = max(people_dict.values())
        max_age_names = [name for name, age in people_dict.items() if age == max_age]
        print('Max age is: ', max_age)
        print('Name(s) with max age: ', ', '.join(max_age_names))

        # Find people with the same age
        age_counts = {}
        for age in people_dict.values():
            if age in age_counts:
                age_counts[age] += 1
            else:
                age_counts[age] = 1

        same_age_names = []
        for age, count in age_counts.items():
            if count > 1:
                same_age_names.extend([name for name, age in people_dict.items() if age == age])
        if same_age_names:
            print('Same age is: ', ', '.join(same_age_names))
        else:
            print('No one has the same age.')

except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("Issue occurred while reading the file.")
except Exception as e:
    print(str(e))

    