# A function in Python is a reusable block of code that performs a specific task.It is a group of statements performing a specific task. 
# Functions help in structuring programs, making code more readable, and avoiding repetition.
# Function can be called any number of times, anywhere in the program.
# In Python, functions are defined using the def keyword

# Syntax of a function
def func():
    print("Hello world")

# Function Call
# Whenever we want to call a function, we put the name of the function followed by parentheses
func() # This is a function call

# Function Definition
# A function definition is the part of a Python program where a function is declared or it can specified as the inner content of a function
def cele():
    name = input("Enter your name: ")
    print(f"Good day {name}")
# cele()

# Types of Functions
# 1) Built in functions: Already present in Python. Example: print(), range(), len() etc.
# 2) User defined functions : Defined by the users. Example: cele() just created by the user, func() etc.

# Function Arguments
# Function arguments in Python are values that you pass into a function when calling it. They allow you to provide input data for the function to process.
# These arguments work as a variable only that can we given to a function such that we can call it later

def argument(name, age): #Here name and age is are the argumets 
    if(age<=18):
        print(f"Congrats {name} your age is {age}. Here's your driving license") #Use case of those arguments
    else:
        print(f"So sorry {name} your age is {age}. No license for you")
argument("Moksh", 18) #These are the values given to the arguments listed in the function

# Return in functions
# In Python, the return statement is used inside a function to send a value back to the caller. It allows a function to produce a result that can be stored in a variable
# If we dont use the return statement and assign the function to the variable it will return NONE.
a = argument("Moksh", 20)
print(a) #None

# Various Things Should be noted down while using the return statement
# 1) When return is executed, the function stops running immediately.Any code after return is ignored.
# 2) If return is used without a value, or if a function has no return, it returns None.
# 3) Functions can return any data type. If there is a dictionary,list or tuple given to the return value it will give it to the variable and we can access it
# 4) Python allows returning multiple values.
# 5) You can use multiple return statements inside if-elif-else conditions or loops.

def ret():
    av1 = int(input("Enter Number 1: "))
    av2 = int(input("Enter Number 2: "))
    av3 = int(input("Enter Number 3: "))
    average = (av1+av2+av3)/2
    return average # Return the value of average
avg = ret() #Average Value
print(avg)

# Default Parameters
# Default arguments in Python are function parameters that have predefined values. 
# If the user does not provide a value for a parameter, Python automatically assigns the default value.
# If the person wants to overwrite the parameter it can do it by specifing its different value in the call parameters

def default(name="Moksh",age=18): #Default Parameters
    if(age<=18):
        print(f"Congrats {name} your age is {age}. Here's your driving license")
    else:
        print(f"So sorry {name} your age is {age}. No license for you")

# default() By calling it you are printing the default values given in the arguments
default("Rahul", 17) #Overwriting the values of arguments

# Recursions
# Recursion is a programming technique where a function calls itself to solve a problem. Instead of using loops
# It is used to directly use a mathematical formula as function.
# Recursion breaks a problem into smaller subproblems until it reaches a base case (a condition where recursion stops).

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# Now let's understand this
# factorial(5)  Waiting for factorial(4)
# factorial(4)  Waiting for factorial(3)
# factorial(3)  Waiting for factorial(2)
# factorial(2)  Waiting for factorial(1)
# factorial(1)  Base case(if statement) reached → Returns 1

# factorial(1) returns 1
# factorial(2) was waiting for factorial(1), so it calculates 2 * 1 = 2 and returns 2
# factorial(3) was waiting for factorial(2), so it calculates 3 * 2 = 6 and returns 6
# factorial(4) was waiting for factorial(3), so it calculates 4 * 6 = 24 and returns 24
# factorial(5) was waiting for factorial(4), so it calculates 5 * 24 = 120 and returns 120