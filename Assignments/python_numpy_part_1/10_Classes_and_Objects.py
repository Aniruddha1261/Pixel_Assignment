'''Write a Python Program to create a class named Student.

It should be initialised with attributes like name, age, rollno, favourite subject(a single subject).

Write a class method getDetails() which prints the name, age and rollno of the object in the below format.

Expected Output Format

Name : name</br> Age : age</br> RollNo : rollno</br>

Expected Example Output

Name : Gautam</br> Age : 20</br> RollNo : 68

Now, there is a list fav_list such that it contains a list of subjects which are favourite to the Principal.

fav_list = ["EG","Mechanics","Chemistry"]
You have to write a class Method isFav() which returns a boolean value i.e either **true** if any of the favourite subject of the principal matches with that of the student. Think of some suitable logic here.

Create 2 objects of class Student with attributes of your choice taken via user input.

Call Both the methods for both the objects. Note - Print the result of the isFav() method.

Bonus Task - Write the body of isFav() method in just one line.'''

from turtle import st

class Student():
    def __init__(self):
        self.name = str(input(print("Enter your name : ", end = " ")))
        self.age = int(input(print("Enter your age : ", end = " ")))
        self.roll = int(input(print("Enter your Roll No : ", end = " ")))
        self.favorite_subject = str(input(print("Enter your favorite subject : ", end = " ")))

    def getDetails(d):
        print("Name : ", d.name)
        print("Age : ", d.age)
        print("RollNo : ", d.roll)
        #print(d.favorite_subject)
    def isFav(f):
        fav_list = ["EG", "Mechanics", "Chemistry"]
        if f.favorite_subject in fav_list:
            return True
        else:
            return False

s = Student()
s.getDetails()
print(s.isFav())

ss = Student()
ss.getDetails()
print(ss.isFav())