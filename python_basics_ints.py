# Numerical types
## Numerical types are: Integers, Floats, Composite, Big ints & Complex numbers etc

# Defining an int
num1 = 20
print(type(num1))
## Float
num2 = 20.0
print(type(num2))

# Mathematical Operators: +, -, *, %, /  These take priority over logical operators but use brackets to be sure
result1 = 10 + 12 #Adding
result2 = 21 - 6 #Subtracting
result3 = 15 * 4 #Multiplying
result4 = 20 % 3 #Finding remainder(when dividing by the second number how much is left between the next divisable num)
result5 = 20 / 2 # Dividing
print (result1, result2, result3, result4, result5)

# Logical Operators:
num1 = 10
num2 = 10
num3 = 13

# Greater than/smaller than or equal to --> returns a boolean (true or false)
print(num1>num2) #false
print(num3>num1) #true
print(num2<num3) #true
print(num1 >= num2) #true
print (num3 <= num2) #false

# Check if the same
## Data type matters
print('10' == 10) #false
print(10 == 10) #true
print(num1 == num2) #true