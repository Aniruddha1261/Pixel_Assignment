'''Find the weighted average of the given array using only the
 ndarray.sum() function. Write only 1 line of code. 
 It should work for any weights or array values.
 The output of the above print() statement should be : 14.05'''
import numpy as np

orig_a = np.array([11, 12, 13, 14, 15, 16])
weights = np.array([-1, 4, 5, 2, 9, 1])
# Write 1 line of code inside the print statement
print(np.ndarray.sum(orig_a*weights)/np.ndarray.sum(weights)) 