'''Swap the first and the last, and the second and the third columns 
from the given 4x4 matrix. Write your code in one line and don't use 
any functions.

Original matrix : 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
The output of the above print statement should be :

[[ 3  2  1  0]
 [ 7  6  5  4]
 [11 10  9  8]
 [15 14 13 12]]'''

import numpy as np

orig = np.arange(16, dtype='int').reshape(-1, 4)
print("Original matrix : \n", orig)

## Write Your code here
orig[:,[0,3]] = orig[:,[3,0]]
orig[:,[1,2]] = orig[:,[2,1]]

print(orig) # Write your 1 line of code inside the print() statement