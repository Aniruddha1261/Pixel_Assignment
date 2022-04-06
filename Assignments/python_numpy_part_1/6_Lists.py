'''Write a Python program to count the number of strings 
where the string length is 2 or more and the first and last 
character are same from a given list of strings. Go to the editor
Sample Input :['abc', 'xyz', 'aba', '1221']
Sample Output :2
Explanation :'aba' and '1221' have length greater than 2 and also 
has matching first and last character.'''

list1 = ['abc','xyz','aba','1221']
# Write your code here
count = 0
for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(count)

'''Write a Python program to print the numbers 
of a specified list after removing even numbers from it.
Hint : Use List Comprehension'''
# Write your code here

lst = [2, 3, 3, 3, 6, 4, 5, 8, 7 ,9 , 11]
for x in lst:
    if x % 2 == 0:
        lst.remove(x)
for x in lst:
    if x % 2 == 0:
        lst.remove(x)

print(lst)