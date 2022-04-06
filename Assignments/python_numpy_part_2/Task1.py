import numpy as np
'''Write a single line of code to extract all numbers from the
 given NumPy array which are strictly less than a specified number.
 Given array : 
 [[5.  2.7 5.1]
 [4.9 6.2 8.5]
 [1.4 2.8 9.5]]
The task is to write a single line of code to print the numbers from 
the numbers array which are strictly less than n, that is, the numbers 
which are strictly less than 5. Write the code inside the print statement 
given below. The code should work for any array numbers and for any value of n,
 so use variables only, and not constants like 5.
The output for the given array should be :
[2.7 4.9 1.4 2.8]
 '''

numbers = np.array([[5.0, 2.7, 5.1],
                  [4.9, 6.2, 8.5],
                  [1.4, 2.8, 9.5]])
#print("Given array : \n", numbers)
n = 5
mask = numbers < n
print(numbers[mask]) # Write your 1 line of code inside the print() statement