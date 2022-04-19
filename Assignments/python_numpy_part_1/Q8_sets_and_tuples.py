'''Sets and Tuples
Check if two sets have any elements in common. If yes, display the common elements.

set1 = {10, 20, 30, 40, 50}

set2 = {60, 70, 80, 90, 10}

Expected output:

Two sets have items in common

{10}'''

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Write your code here to get common elements among them
for x in set1:
    for y in set2:
        if x is y:
            print(x)


'''Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Write your code here to replace last value of tuples in the list
'''for x in list1:
    tup1 = x[0:3][0:2]
print(tup1)
a = range(101)
tup2 = tuple(a)'''
tup2 = tuple()
for x in list1:
    tup1 = tuple(x[0:2])
    tup2 += tup1
tup = list(list1[0:3:1][2])
#tup[0:3][2] = 100
print(tup2)