import numpy as np

arr = np.arange(2,19,2)

a = arr.reshape(3,3)

def mul(x,y):
    return x*y

myMul = np.frompyfunc(mul,2,1)

b = myMul(a,4)

c = np.multiply(np.eye(3,3),b)

print(a,'\n')
print(b,'\n')
print(c)