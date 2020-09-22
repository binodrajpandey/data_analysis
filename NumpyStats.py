import numpy as np

# Maths
arr1 = np.array([1,3,4,6])
arr2 = np.array([1,3,4,6])
# prints 14
sum = np.sum(arr1)
print(sum)
print(np.mean(arr1))
print(np.nanmean(arr1))
print(np.std(arr1))
print(np.max(arr1))
# should have compatible shape
arr3 = arr1+arr2
print(arr3)
arr4 = arr1+3
#prints [4 6 7 9] ie. 3 is added in each elements
print(arr4)
print(arr1/2)
print(arr1%2)
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[1,2,3,4]])
arr3 = arr1+arr2
# Prints
# [[ 2  4  6  8]
#  [ 6  8 10 12]] ie. value will be replacted to make equql shape. so this kinds of arrays are compatible.
print(arr3)