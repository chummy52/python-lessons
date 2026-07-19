#Arithmethic Operators and Math Functions 

# Augmented Assignment Operators (+=, -=, *= or **=, /=, etc.)
# Modulus Operator (%) - gives the remainder of any division
# ex: if the variable is even then "0", if odd, then there will be remainder


#Math Related Functions

# ex:
x = 3.14
y = 2.71
z = -67

# 1st: Round Function (round) - rounds a number to the nearest whole number
# ex:
result = round(x)
print (result)

# 2nd: Absolute Value Function (abs) - gives the distance of a number from 0, 
# or the positive version of a number, it gives the absolute value of a number.
# ex:
result = abs(z)
print (result)

# 3rd: Power Function (pow) - raises numnber to the power of another number 
# ex: 
result = pow(z, 2) # (-67, 2) you can use the numbers too
print (result)

# 4th: Maximum Function (max) - gives the max value of various values, or gives max value of sets of numbers.
# ex: 
result = max(x, y, z)
print(result)

# 5th: Minimum Function (min) - gives the min value among variables (the opposite of the max function)
# ex:
result = min(x, y, z)
print (result)



# Math Modules (import math)
# ex:
import math
a = 24
b = 24.15 # this is for the float modules

print(math.pi) # this gives the value of the pi
print(math.e) # gives the value of e

result = math.sqrt(a)
print (result)

result_float_1 = math.ceil(b)
result_float_2 = math.floor(b)
print (result_float_1)
print (result_float_2)
