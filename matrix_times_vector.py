import numpy as np


a = np.array([[ 1, 0 ,3, 0], [ 0, 6 ,0, 8], [ 0, 10 ,11, 0] , [ 13, 0 , 0, 16]])
b = np.array([2,
              5,
              4,
              1])

c = a.dot(b)

print c

e = np.matrix([[ 1, 0 ,3, 0], [ 0, 6 ,0, 8], [ 0, 10 ,11, 0] , [ 13, 0 , 0, 16]])
f = np.matrix([[ 2], [5], [4], [1]])

g = e * f

#np.matmul(a, b)
print g