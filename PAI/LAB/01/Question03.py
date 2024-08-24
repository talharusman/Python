num = (input("Enter the num")).split()
count = 0
for i in num:
    if int(i)%2 == 0:
        count = count + 1
print (count)