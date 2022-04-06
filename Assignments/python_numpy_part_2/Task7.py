'''Get the value 78 from the given 3D array by indexing.
The output of the above print() statement should be : 78'''

import numpy as np

arr = np.array([[[34, 22, 3],
                 [41, 25, 23]],
                [[67, 28, 91],
                 [110, 11, 21]],
                [[16, 112, 44],
                 [78, 20, 12]]])

print(arr[2][1][0]) # Using indexing to get the element 78 from the array