'''Delete set of keys (keysToRemove) from a dictionary and display the resultant dictionary
Given : The "sampleDict" dictionary has already been defined in the below code .

Expected Output: {'city': 'New york', 'age': 25}'''

# Given Dictionary
from os import popen


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}

# remove the keys present in the list below from the dictionary 
keysToRemove = ["name", "salary"]
# Write your code here
for x in keysToRemove:
    sampleDict.pop(x)
print(sampleDict)


'''Write a program in Python to read the admission number,
 name of student and his/her stream of 10 students and create a 
 dictionary from this information. print the dictionary'''


dic_new = {
    "admission number" : 0,
     "name" : "annu",
     "stream" : "prod", 
 }
for x in range(10):
  dic_new[x] = {
      
     "admission number" : int(input(print("enter admission number",end = " : "))),
     "name" : str(input(print("enter name of student", end = " : "))),
     "stream" : str(input(print("enter stream of student", end = " : "))),
     
 }
print(dic_new)