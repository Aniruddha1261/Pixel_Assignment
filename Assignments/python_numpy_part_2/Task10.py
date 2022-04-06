'''Create a linear scale (arithmetic progression) with n points starting 
from a, with a common difference of d. Calculate the standard deviation 
of an array of exponentials of each element of the linear scale. Write 
only 1 line of code. It should work for any values of n, a, and d.
The output of the above print() statement should be : 1.3820163896209162e+28'''
import numpy as np

n = 10
a = 3
d = 7
# Write 1 line of code inside the print() statement
print(np.std(np.exp(np.linspace(a,a + (n-1)*d,n)))) 