def calculate_average(temperatures):
    """Calculate the average temperature"""
    return sum(temperatures) / len(temperatures)

def find_max_min(temperatures):
    return max(temperatures), min(temperatures)


def sort_temperatures(temperatures):

    return sorted(temperatures)


def delete_temperature(temperatures):

    day = int(input("Enter the day you wish to remove the record of: "))
    del temperatures[day]
    return temperatures

temperatures = [-15, -5, 0, 7, 12, 18, 21, 24, 29, 32, 35, 37, 40, 43, 47, 50, -10, 2, 9, 15, 22, 28, 33, 39, 42, 46, -20, 6, 13, 20, 25]

print("Average temperature: ", calculate_average(temperatures))
print("Maximum and Minimum values of the list: ", find_max_min(temperatures))
print("List in ascending order: ", sort_temperatures(temperatures))
print(delete_temperature(temperatures))