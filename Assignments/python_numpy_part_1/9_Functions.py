'''Functions
1) Write a function called showNumbers that takes a parameter 
called limit. It should print all the numbers between 0 and 
limit with a label to identify the even and odd numbers. 
For example, if the limit is 3, it should print:

0 EVEN
1 ODD
2 EVEN
3 ODD'''

def showNumbers(limits):
    for i in range(limits):
        if i % 2 == 0:
            print(i , "EVEN")
        else:
            print(i , "ODD")

showNumbers(12)

'''2) Write a function that takes limit(integer) as a paramter
 and prints all the prime numbers between 0 and limit.'''

def limit(integer):
    for i in range(integer):
  # Write Code here
     if i == 1 or i == 2:
        print(i)
       # print("I was a prime")
     x = 2
     while x < i + 1 and i > 2:
        if i % x != 0 and x < i:
            x += 1
        elif i % x == 0 and x < i:
            x += 1
            break
        elif i == x:
            print(i)
            #print("I was a prime")
            x += 1
            break
limit(15)