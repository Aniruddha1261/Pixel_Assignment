clubs = ['SRA' , 'Aero' , 'Racing' , 'DSC' , 'COC'] 
membership= ['SRA' , 'DSC']
# Write your code here
'''Create a boolean list respective to the clubs you are
 a member of without using the '==' operator:
  Expected output: [true,false,false,true,false] 
  HINT: use the membership operator'''
for i in range(5):
    print(clubs[i] in membership)

# Write your code here
'''Convert the boolean list into a list of binary one or zero
 without using the operator '=='. 
 Expected output: [1,0,0,1,0] 
 HINT: Check out identity operator'''
for i in range(5):
    if((clubs[i] is membership[0]) or (clubs[i] is membership[1])):
        print(1)
    else:
        print(0)

# Write your code here
'''You are provided with the following:
 expression = 4_6_9_3_2319 Using the 
 operators: +,-,*, /, % in places of the make 
 an expression that reads the value: 25.0.'''

expression = 4*6- 9/3 +23-19 
print(expression)
