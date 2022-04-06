'''First, create a chessboard of size n x n using NumPy. 
n can have any value, even or odd. If the square is black, 
its value should be 1, else, it should be 0. Now, we have an array 
of locations where some chess pieces are. Print whether the locations 
are black squares, or white. You will be given an array for score. 
If the piece is on a white square, print the median of that particular 
piece's row as the score for that piece. If it is on a black square, 
print the sum of the square roots of the column of that piece. 
Add up all the scores obtained and print it as the final score. 
It should work for any and all values of n, locations, and scores.'''
# Black == 1
# WHITE == 0
import numpy as np

n = 9
locations = [(1, 2), (3, 2), (7, 6), (2, 4), (8, 8)] # Locations are in format (Row, Column) with indexing starting from 0
scores = np.arange(n*n).reshape((n, n))
print("Score Table : \n", scores)


# Write your code to create the chessboard here. Use variable chessboard to store it.
chessboard = np.array(np.zeros(n*n)).reshape(n,n)
chessboard[0:n:2, 1:n:2] = 1
chessboard[1:n:2, 0:n:2] = 1

###
print(chessboard)
'''The output of the above print() statement should be :

[[0 1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0 1]
 [0 1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0 1]
 [0 1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0 1]
 [0 1 0 1 0 1 0 1 0]
 [1 0 1 0 1 0 1 0 1]
 [0 1 0 1 0 1 0 1 0]]'''

# Print whether the locations are on black or white squares
for x in locations:
    i = x[0]
    j = x[1]
    if chessboard[i][j] == 0:
        print("WHITE")
    else:
        print("BLACK")

'''The output of the above code should be :

BLACK
BLACK
BLACK
WHITE
WHITE'''
sum = 0
# Write the code to print individual scores, and total score
for x in locations:
    i = x[0]
    j = x[1]
    if chessboard[i][j] == 0:
        print(np.median(scores[i]))
        sum = sum + float(np.median(scores[i]))
    else:
        print(np.sum(np.sqrt(scores[:,j])))
        sum = sum + float(np.sum(np.sqrt(scores[:,j])))

'''The output of the above code should be :

51.75610550712166
51.75610550712166
55.47253576970644
22.0
76.0
-------
TOTAL Score =  256.98474678394973'''
print("TOTAL Score = ", sum)