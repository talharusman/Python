myList = []

result=1
size = int(input("Enter the size of the list: "))

for i in range(size):
    myList.append(int(input(f"Enter the number {i+1}: ")))

for j in range(size):
    result *= myList[j]

print("Result: ", result)