'''Create a 4 x 2 x 3 3D-array of numbers from 4 to 27 (both inclusive).
 Use exactly two functions of NumPy to accomplish this. Write only one 
 line of code.
 
The output of the above print statement should be :

[[[ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]]

 [[16 17 18]
  [19 20 21]]

 [[22 23 24]
  [25 26 27]]] '''

import numpy as np
# Write your 1 line of code after the assignment operator (=)
mat_24 = np.array(range(4,28)).reshape(4,2,3)

print(mat_24)