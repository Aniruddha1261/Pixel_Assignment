'''Calculate the difference between the maximum and the minimum values
 of a given array along the third axis. Use only the ndarray.min() and 
 ndarray.max() functions. Write only 1 line of code.
 
 Original array : 
 [[[ 13  21  12]
  [ 76  10  25]
  [ 63  17  82]
  [ 19 130 115]
  [122 134 124]
  [159 176 174]]

 [[ 18 191 202]
  [ 21 222  23]
  [214  25 246]
  [ 27   8  29]
  [ 30  31   3]
  [  3  34  35]]]
The output of the above print() statement should be :

[[  9  66  65 111  12  17]
 [184 201 221  21  28  32]]
'''
import numpy as np

Orig_array = np.array([[[13, 21, 12],
                        [76, 10, 25],
                        [63, 17, 82],
                        [19, 130, 115],
                        [122, 134, 124],
                        [159, 176, 174]],
                       [[18, 191, 202],
                        [21, 222, 23],
                        [214, 25, 246],
                        [27, 8, 29],
                        [30, 31, 3],
                        [3, 34, 35]]])
print("Original array : \n", Orig_array)

print(np.ndarray.max(Orig_array, axis=2) - np.ndarray.min(Orig_array, axis=2)) # Write 1 line of code inside the print() statement