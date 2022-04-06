'''Complete the for loop such that whenever there is an prime number
 it prints the number plus "I was a prime" in the same line, otherwise it prints nothing.

Using the looping statement and the control statements'''

for i in range(100):
  # Write Code here
    if i == 1 or i == 2:
        print(i, end = " ")
        print("I was a prime")
    x = 2
    while x < i + 1 and i > 2:
        if i % x != 0 and x < i:
            x += 1
        elif i % x == 0 and x < i:
            x += 1
            break
        elif i == x:
            print(i, end = " ")
            print("I was a prime")
            x += 1
            break
  #Don't tamper the next line
        
  
  
  