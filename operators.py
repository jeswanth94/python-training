# Trying for Arithmetic operators
a=10
b=15.5
mod = b%a
print ('mod')
"' gives us the remainder result'"

#Relative operator
a=10
b=12
a!=b
print ('true')

#assignment operator

a=100
a+=200
print(a)

#Identity Operators
a=10
b=10
if a is b:
      print ('true')
else:
      print ('false')

#bitwise operator
a=10
b=20
bo = a&b
bo1= a|b
bo2= a^b
bo3= ~a
print(bo)
print(bo1)
print(bo2)
print(bo3)



#Binary Operator
a=10
b=20
c= a and b
print(c)


a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print("Line 1 - a is available in the given list")
elif( b not in list ):
   print("Line 2 - b is not available in the given list")
else:
    print("no inputs")
