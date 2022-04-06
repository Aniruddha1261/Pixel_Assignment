'''Create a matrix of dimensions m x n, with 0 being the values on the 
border, and all the values inside being 1. You may write maximum of 2 
lines of code. The matrix name should be mn_array. It should work for 
any values of m and n. You are only allowed to use the numpy.zeros() 
function.

The output of the above print() statement should be :

[[0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]'''

import numpy as np

m = 9
n = 7

# Write your 2 lines of code here
mn_array = np.array(np.zeros(m*n)).reshape(m,n)
for i in range(m):
    if i > 0 and i < m - 1:
        for x in range(n):
         if x > 0 and x < n - 1:
            mn_array[i][x] = 1
    
####

print(mn_array)