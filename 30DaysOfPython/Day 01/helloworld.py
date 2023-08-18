#Day 1 - 30DaysOfPython

import math

#Simple Math functions

""" print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

#Check Data Types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple """


#---------------------------------------------

""" print (2+3)
print('Loïc')
print(type(2+3))
print(type('Loïc'))
print(type({'name':'Loïc'}))
print(type((1,2,3,4)))
print(type([1,2,3]))

Pistache = True

print(Pistache)
 """


#--------------------------------------------

#Find Euclidian Distance between (2,3) & (10,8)

A = 2
B = 3
C = 10
D = 8

Aa = C-A
Bb = D-B

print("Distance between coordinates =", Aa,",", Bb)

Cc = math.pow(Aa,2)
Dd = math.pow(Bb,2)

print("Square the results :", Cc,",",Dd)

x = Cc + Dd


print("Sum the results up :", x)

result = math.sqrt(x)

print("Square root the result :", result)

result = round(result)

print("Round the result :" , result)

print("Result is :" , result)