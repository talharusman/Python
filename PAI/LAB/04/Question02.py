list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [i + j for i in list1 for j in list2]
print(result)