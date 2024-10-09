import numpy as np

arr = np.random.choice([2,5,9,10],size = (4,4))

a = np.multiply(arr,np.eye(4,4))

arr2 = np.arange(1,32,2)

b = arr2.reshape(4,4)

c = np.add(a,b)

print(arr,'\n')
print(a,'\n')
print(b,'\n')
print(c,'\n')