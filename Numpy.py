import numpy as np
import urllib.request

climate_data = np.array([
    [3,4,5],[4,6,8], [4,5,6]
])
# prints (3,3)
print(climate_data.shape)

weights = np.array([0.3,0.2, 0.5])
# Prints (3,)
print(weights.shape)

arr3 = np.array([
    [[2,3,4],[2,3,4],[2,3,4]],
    [[4,5,6],[6,5,3],[5,6,7]]
])
# prints (2,3,3) ie. form outer to inner.
print(arr3.shape)
# prints float64
print(weights.dtype)
# Prints [0.3 0.2 0.5]
print(weights)

kanto = np.array([73,67,43])
# <class 'numpy.ndarray'>
print(type(kanto))
kanto_yield= np.dot(kanto,weights)
# Prints 56.8 it is calculated as 73*0.3+ 67*0.2 + 43*0.5
print(kanto_yield)
# Prints [21.9 13.4 21.5]
print (kanto* weights)

# prints 56.8
print((kanto * weights).sum())
# [4.2 6.4 5.2]
print(np.matmul(climate_data,weights))
# [4.2 6.4 5.2]
print(climate_data@weights)

# csv file to np array
urllib.request.urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv','climate.txt')
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data)
yields = climate_data@weights
# (10000,)
print(yields.shape)
climate_results = np.concatenate((climate_data, yields.reshape(10000,1)), axis=1)
# [[25.  76.  99.  72.2]
#  [39.  65.  70.  59.7]
#  [59.  45.  77.  65.2]
#  ...
#  [99.  62.  58.  71.1]
#  [70.  71.  91.  80.7]
#  [92.  39.  76.  73.4]]
print(climate_results)

# Save into file
np.savetxt('climate_result.txt', climate_results, fmt = '%2f', header='temperature,rainfall,humidity, yield_apples', comments='')