# Variable:
# What are variables? Variables are the container that stores data values
# There are some of the rules of writing a variable name the rules are as follows=
# A variable name can contain alphabets, digits, and underscores. 
# A variable name can only start with an alphabet and underscores. 
# A variable name can’t start with a digit. 
# No while space is allowed to be used inside a variable name. 
# No keyword cannot be used in variables
# a=1
# b=2
# print("Hello There you have the solution of the most tough equation in the world:",a+b)

# Data Types:
# There are main four types of data types: String(str), Boolean(True,False), Integers(int), Floating Numbers(Decimals), None
# Numeric Types
# Used to represent numbers.
int_data = 10            # Integer (whole number)
float_data = 10.5        # Float (decimal number)

# Sequence Types
# Used to store text in a string format.
string_data = "Hello"    # String (sequence of characters)

# Boolean Type
# Used to represent True or False values.
bool_data = True         # Boolean (True or False)

# None Type
# Represents the absence of value or a null value.We use this to represent that this variable what does not contain any value
none_data = None         # NoneType (no value)

# Operators
# 1. Arithmetic Operators
# Used for mathematical operations.
a, b = 10, 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division (float result): 3.333...
print(a // b) # Floor Division: 3 (integer result)
print(a % b)  # Modulus: 1 (remainder)
print(a ** b) # Exponentiation: 1000 (10^3)

# 2. Comparison Operators
# Used to compare two values; result is a boolean.
print(a == b)  # Equal: False
print(a != b)  # Not Equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# 3. Logical Operators
# Used for logical operations on boolean values.
x, y = True, False
print(x and y) # Logical AND: False
print(x or y)  # Logical OR: True
print(not x)   # Logical NOT: False

# 4. Assignment Operators
# Used to assign values to variables.
a = 5         # Assign: a = 5
a += 2        # Add and assign: a = a + 2
a -= 1        # Subtract and assign: a = a - 1
a *= 3        # Multiply and assign: a = a * 3
a /= 2        # Divide and assign: a = a / 2
a //= 2       # Floor divide and assign
a %= 2        # Modulus and assign
a **= 3       # Exponentiation and assign

# Type Function
# It is used to find out the type of a value
sui = "69"
rol = float(sui)
mes = str(rol)
print(type(mes))
print(type(rol))
print(type(sui))
print(mes)

# Input function
# It is used to get the values from the user each user who enters their values will be stored as a string form even they entered a floating or integer value
name1 = input("Enter Your Lucky No.:")
passwo = input("Enter your Unlucky No.:")
print("Here is your sum of the no.:", name1+passwo) #I knew it will only be contactinating the values as they are in string forms to get the actual sum you need to convert them into int or float