# Walrus operator
# The Walrus Operator (:=) is a shortcut that allows you to assign a value to a variable while using it in the same expression.

# Think of it like this:
# Normally, you first assign a value, then use it.
# With the walrus operator, you can do both at the same time.

# while True:
#     if not (user_input := input("Enter Something here: ")):
#         break
#     else:
#         print(f"You entered this number {user_input}")


# Type Definitions
# Type definitions in Python help you explicitly specify the expected types of variables, function arguments, and return values. This makes the code more readable, maintainable, and less error-prone.
# In this you can specify that the variable, function or a return value you are creating supports which data type.

a : int = 1 #In this we are suggesting to be it as a integer
def sum(x : int, y: int) -> int: #In this we are calling a function which suggestes to have the values x and y as integers and the return value also be a integer.
    return x+y
print(sum(1,7))

# This only recommends that which value should you have to enter in the variable or in functions
# Use 'mypy' to detect such type mismatches before execution. Install it if not.

# Type Hints:-
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.
# You can import List, Tuple and Dict types from the typing module

from typing import List, Tuple, Dict, Union #In this we are importing the List from the typing module

# List of Strings
lis : List[str] = ["Moksh", "Sanvi", "Aaashu"] #In this also we are only suggesting the data type the values should be from

# Tuple of a string and integers
person: Tuple[str, int] = ("Alice", 30) # This shows that the tuple is allowed to have str and int data types.

# Dictionary of a string and integer
dic : Dict[str, int] = {"Age":18, "Salary":900000}

# Union type for variables that can hold multiple types 
uni : Union[int, str] = "ID123" # In a string you can use both string or a integer
uni = 1234


# Match Cases
# The match-case statement in Python is like a smart alternative to multiple if-elif-else conditions. It was introduced in Python 3.10 and helps check different possible values of a variable in a cleaner and more readable way.

def day(day):
    match day:
        case "Monday":
            print("The week just started. Work hard!!")
        case "Friday":
            print("Congrats the weekend is near")
        case "Sunday":
            print("It's a Holiday. Enjoyyy!!!")
        case _ :
            print("It's just a normal day")
day("Friday")

# Some Limitations:-
# 1) match-case only checks for direct values or patterns.
# 2) It cannot evaluate expressions or conditions like if-else does.
# 3) You cannot use comparison operators (>, <, ==) or mathematical calculations inside case.
# 4) Mathematical calculations

# Where we can use Match-Case:-
# 1) match-case is useful when checking for exact values
# 2) Great for structured data like tuples or lists. For example:-

point = (0,0)
match point:
    case (0,0):
        print("The Point lies on the Origin")
    case (x,0):
        print(f"The point lies on the x-axis at {x}")
    case (0,y):
        print(f"The point lies on the y-axis at {y}")
    case (x,y):
        print(f"The point lies on the {x,y}")
    

# Dictionary Merge:-
# The Merge operator(|) two dictionaries into a new dictionary without changing the originals.
dic1 = {"a": 7, "b": 3}
dic2 = {"b": 5, "c": 9}
merged = dic1 | dic2
print(merged)

# What happended here?
# "a": 7 (from dict1) is added to merged.
# "b": 5 (from dict2) overwrites "b": 3 (from dict1).
# "c": 9 (from dict2) is added.
# dict1 and dict2 remain unchanged.

# Use | When:
# You want to create a new dictionary without changing the original ones.
# You need to merge dictionaries without modifying any existing data.
# You prefer immutable operations (where original data remains untouched).

# Update Operator:-
# The |= operator updates an existing dictionary in-place (modifies it directly).
up1 = {"a": 1, "b": 2}
up2 = {"b": 3, "c": 4}

up1 |= up2# the Dictionaries are merged without creating a new one. It updates first dictionary through the values we got form merging the dictionaries. That merged will be updated to the first dictionary. 
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# What happened here?
# up1 is modified (not a new dictionary).
# "b": 3 (from up2) replaces "b": 2 (from up1).
# "c": 4 is added to up1.
# up2 remains unchanged.

# Use |= When:
# You want to modify an existing dictionary directly.
# You don’t need a new dictionary, just an in-place update.
# You want to save memory (since |= avoids creating a new object).


# Exception Handling
# In Python, exception handling is used to catch and handle errors in a program without crashing it. For example:-
# Imagine you are using an ATM, and you enter the wrong PIN. Instead of shutting down, the ATM shows an error message and asks you to try again.

# Python provides the try-except block to handle errors.
try:
    num = int(input("Enter the Number: "))
    div = 10/num
    print(f"The Number after division with 10 is : {div} ")
except ValueError: # If an error occurs (e.g., the user enters "abc"), the except block runs.
    print("You are supposed to enter a number...")

# We can also Catches any error (exception) that occurs and prints its message. Like this:-
try:
    num1 = int(input("Enter the Number: "))
    div1 = 10/0
except Exception as v:
    print("The Error Occured: ", v)

# What Happended in this code:
# 1) Exception is the base class for most errors in Python. Through which it can detect any error occured in case.
# 2) as v stores the error message inside the variable v.
# 3) print(v) displays the actual error message.
# We can take the use of this Exception as to catch the errors. But we can use it different sort of errors in which we have to display some other type of text. For example we can display some other text in ValueError as we done before and for other errors we can use Exception.


# Raising Exceptions:-
# In Python, you can manually trigger errors using the raise keyword. This is called raising an exception.

# Why Would Someone Raise an Exception?
# 1) To stop the program when something goes wrong.
# 2) To enforce rules (e.g., prevent negative numbers in age input).
# 3) To improve debugging by providing custom error messages.
# 4) To ensure valid data before continuing execution.

# The Syntax is:
# raise ExceptionType("Custom error message")

age : int = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print(f"Your age is {age}")

# Custom Error:-
# You can create your own error types by making a custom exception class.
class NegativeNumber(Exception): # We inherit from Python's built-in Exception class. This allows our custom error to inherit all the properties and behavior of Python exceptions.
    pass  # Custom exception with no extra logic

def check_number(n):
    if n < 0:
        raise NegativeNumber("Negative numbers are not allowed!")
    else:
        return f"{n} is valid!"

print(check_number(5))   # Works fine
#print(check_number(-3))  # Raises NegativeNumberError


# Try with Else Clause:-
# In Python, you can use an else clause with try-except to run some code only if no error occurs.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Kindly enter a valid number.....")
else:
    print(f"You entered this number: {num}") # This will run only if no error occures

# Python tries to execute the try block.
# If an error occurs, it goes to except.
# If no error happens, the else block runs.


# Try with Finally:-
# In Python, the finally block is used with try-except to ensure some code always runs, no matter what happens—whether an error occurs or not.
# Runs even if there is a return or exit() in try or except.

try:
    num = int(input("Enter a number here: "))
    div = num/10
    print("The divsion of the number is: ", div)
except Exception as v:
    print(v)
print("This code will always run...")

# Why Use finally Instead of Just a Normal Print Statement?
# 1) To ensure critical cleanup happens, even if there's a return, break, or exit. For example if we return a value in a function, the code next written in it is not considered. But finally overwrites this still runs.
def division(a,b):
    try:
        result = a/b
        return result
    except ValueError:
        print("Enter a valid number.......")
    finally:
        print("This code will always run even after return value")
print(division(12,2))

# 2) Cleaning Up a File. For example:-
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing the file.")  # This will always run
    if 'file' in locals(): #locals() checks if file was successfully created before trying to close it.
        file.close()  # Ensures file is closed
# I am using this sort of code only for explanation. Except this you can use with open() method to perform the same task. Or the Nested try-finally


# Global Keyword
# The global keyword in Python allows you to modify a global variable inside a function.
# A global variable is a variable declared outside a function and can be used anywhere in the script.

# Why Do We Need the global Keyword?
# If you try to modify a global variable inside a function, Python creates a new local variable instead, rather than changing the global one.
# To modify a global variable inside a function, use the global keyword.

count = 0  # Global variable
def increment():
    global count
    count += 1
increment()
increment()
print(count)  # Output: 2


# Enumerate Function:-
# The enumerate() function in Python adds a counter (index) to an iterable (like a list or tuple), allowing you to loop over it while keeping track of the index.
# Helps track the index while looping.
# Avoids manually updating an index variable (i = 0, i += 1).

fruits = ["apple", "mango", "banana"] #List of fruits
for index,fruit in enumerate(fruits): #Index here means the index value the for loop is operating currently. The fruit contains the value present at the index.
    print(f"The fruit on index {index} is: {fruit}")

# We can even give a start value to enumerate function
fruits = ["apple", "mango", "grapes"] #List of fruits
for index,fruit in enumerate(fruits, start=1): #The start=1 means the counting will start from 1
    print(f"The fruit on index {index} is: {fruit}")

# Enumerate with Strings:-
word = "Jainmoksh"
for index,w in enumerate(word, start=1):
    print(f"The Word on index {index} is: {w} ")


# List Comprehentions:-
# A list comprehension is a shortcut for creating lists in Python. It lets you write a for-loop in a single line in a clean and easy way.
# Faster execution compared to regular loops.

numbers = [i for i in range(0,5)] # In this the values from 0 to 4 are appending automatically into the list
print(numbers)

# Syntax:
# new_list = [expression for item in iterable]

# Understanding the line of code:- [i for i in range(5)]
# First i (Expression):-	    This is the value that will be added to the list.
# Second i (Loop Variable):-	This takes each value from range(5).
# range(5):-	                Generates numbers 0, 1, 2, 3, 4.

# Squaring of the numbers:-
numList = [1,6,3,9,10,2]
sqaure = [i*i for i in numList] # 'i' is the value taken from the numList and then multiplied with itself and appended to the list.


# Lambda keyword
# A lambda function is a small, one-line function that does not have a name. It is used when you need a quick function for simple calculations. Instead of using def to define a function, you use the lambda keyword.

# Syntax:-
# lambda arguments: expression

# lambda → A special keyword to create a small function.
# arguments → Inputs (like normal function parameters).
# expression → The operation to be performed (must be a single line).

sqaure = lambda a: a*a  # 'a' is given as the parameter and the expression as a*a which is used for getting the sqaure of the number
print(sqaure(5))

# Passing more than 1 parameter:-
total = lambda a,b,c,d: a+b+c+d  #The expression we are performing it directly return its value
print(total(100,200,300,400))


# Format Method
# The format() method in Python is used to insert values into a string. It helps you create dynamic sentences without manually joining strings.

# Syntax:-
# "Some text {} and {}".format(value1, value2)

# {} → A placeholder where the value will be inserted.
# .format(value1, value2, ...) → Values to be placed in {}.

val = "Some text is {} here which is {} jain is a {} boy.".format("entered", "Moksh", "good")
print(val)

# This format method is used in previous versions of python but still used in many websites which are still using that version.
# Now this method is replaced by 'f' string as we are using in our overall course.

# We can even change the sequence of getting the values in parantheses by entering the index of the listed values. 
val = "Some text is {1} here which is {0} jain is a {2} boy.".format("entered", "Moksh", "good")
print(val)


# Map:-
# Apply a Function to Each Item. Takes a function and a list (or other iterable). Applies the function to each item in the list. Returns a new list with the modified values.
numbers = [1,2,3,4,5,6,7,8,9,10]
cube = list(map(lambda x: x**3, numbers)) # The 'x' given as a parameter takes the values from the numbers one by one and map function appends that number into the list. To get that numbers we have to convert this map into a list to access it.
print(cube)

# map() is a function that iterates over the list numbers.
# It takes each element from numbers and passes it to the lambda function.
# The lambda function receives each element as x and processes it.

def make_even(num):
    if num%2 != 0:
        return num+1
    else:
        return num
sqaure = list(map(make_even, numbers))

# How map() is working in this code
# Takes 1 → Calls make_even(1) → Returns 2
# Takes 2 → Calls make_even(2) → Returns 2
# Takes 3 → Calls make_even(3) → Returns 4

# Normally, map(function, iterable1, iterable2, ...) can take multiple iterables.
# If a function has more than one parameter, map() will take elements from multiple lists at the same time, passing one value from each list to the function.


# Filter:-
# The filter() method is used to select certain items from a list based on a condition.

# Syntax:-
# filter(function, iterable)

# function → A function that returns True or False.
# iterable → A list (or other collection) to filter.
# Only the items where function returns True are kept!

animals = ["Lion", "Elephant", "Giraffe", "Rhino", "Deer","Charvik", "Donkey"]
even_number = list(filter(lambda x: len(x) > 5, animals)) #This filters the list of animals on a condition which return true or false
print(even_number)


# Reduce:-
# The reduce() function is used to combine all elements of a list into a single value.

# Syntax:-
# from functools import reduce
# reduce(function, iterable)

# function → A function that takes two values at a time and combines them.
# iterable → A list (or other collection) to process.
# Keeps reducing until only one final result remains.

from functools import reduce
numbers = [1, 2, 3, 4]
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)
