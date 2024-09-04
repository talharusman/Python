with open(r'C:\Users\k230065\PycharmProjects\Lab03\text01.txt') as fileobj:
    contant = fileobj.read()

count = 0
for i in range(len(contant)):
    count+=1
print(count)
