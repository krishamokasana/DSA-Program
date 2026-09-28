from numpy import *

arr = array([1,2,3,4,5])
print(arr.nbytes)

arr = array([[1,2,3],[4,5,6]])
print(arr.nbytes)

arr = array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr.nbytes)
