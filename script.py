# CHAPTER 1 MODULES
# Print Function
# print("Hello World") #This type of function is used to print a single but if you want to print a no of lines at a single time you can use Triple Quotes (""" or ''')

# print("""Pretty women wonder where my secret lies.
# I'm not cute or built to suit a fashion model's size
# But when I start to tell them,
# They think I'm telling lies.""")

# Modules
# A module is a file containing code written by somebody else(usually) which can be imported and used in our programs.
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# PIP: Is the package manager for python. We can use pip to install a module on your system.
# It is used in the terminal



# CHAPTER 2 VARIABLES,OPERATORS AND DATA TYPES
# Variable:
# What are variables? Variables are the container that stores data values
# There are some of the rules of writing a variable name the rules are as follows=
# A variable name can contain alphabets, digits, and underscores. 
# A variable name can only start with an alphabet and underscores. 
# A variable name can’t start with a digit. 
# No white space is allowed to be used inside a variable name. 
# No keyword cannot be used as variables
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
# Represents the absence of value or a null value.We use this to represent that this variable exists which does not contain any value
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
rol = float(sui) # It changes the type of the text to float
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



# CHAPTER 3 STRINGS
# String is a datatype in python it is used to store the characters and even sometimes even the numbers in string form
# When we say strings are immutable in Python, it means that once a string is created, its content cannot be changed. You cannot change them by running functions on them.
# If anything written in Single cots(''), Double Cots("") or Triple Cots(''' ''') can be considered as a string.
# Single and double quotes are used for single-line strings, while triple quotes are used for multi-line strings and docstrings. Triple quotes can also include both single and double quotes without escaping them.

a ='Moksh' # Single quoted string
b = "Moksh" # Double quoted string
c = '''Moksh
Hello
My dear
''' # Triple quoted string

# If we want to find any strings length we will be using len() command
print(len(a)) 

# String Slicing
# It allows you to extract a portion of a string by specifying a start and end index. It follows the format string[start:end].
# Suppose we have a string "Moksh" its character starting would be from index 0. So in this if we count from zero there will be 4 charcaters
# If we want to start the counting from the ending we will start from -1 .Like -1,-2....
# For more you can go through this https://i.ytimg.com/vi/BhmsJAzIp6w/maxresdefault.jpg

# sl = name[index_start:index_end]
nameshort = b[0:4] #In this we have to first put the variable name whom we have to slice and then by opening the brackets and writing the starting and end_point. But excluding the end_point which is 4(it will only print the object till 3)
nameshort1 = b[2] #This will be printing one character
nameshort2 = b[:4] #This means that the ind_start is 0 and the ind_end is 4
nameshort3 = b[2:] #This means that the ind_start is 2 and the ind_end is last length of the string
print(nameshort3)

alpa = "abcdefghijklmnopqrstuvwxyz"
print(alpa[0:9:4]) #This will first process the characters 0 to 9 and after it will give skip starts skiping 4 characters from the list obtained
# For example it will first process abcdefghij and after skipping 4 it will first print the ind_start character which is 'a' and then start skipping 4 character including the first letter 'a'

# String Functions
sigma = "Sigma Boii"
# 1)Length of the string()
print(len(sigma))

# 2)Endswith():- It is used to confirm that a string ends with it or not. It results in True or False. The function is case-sensitive
print(sigma.endswith("Boii"))

# 3)Startswith():- It is used to confirm that a string starts with it or not. It results in True or False. The function is case-sensitive
print(sigma.startswith("Sig"))

# 4)Capitalize():- It is used to capitalize the first character of the sentence
print(sigma.capitalize())

# 5)Lower(): Converts all characters in a string to lowercase.
print(sigma.lower())

# 6)Upper(): Converts all characters in a string to uppercase.
print(sigma.upper())

# 7)Strip():Removes leading and trailing whitespaces (or specific characters).
print(sigma.strip())

# 8)Join(): Joins elements of a list into a single string with a specified delimiter. The delimiter is the string that will be placed between the elements when they are joined. It could be a space (" "), a comma (","), or any other string.
j = ["Moksh", "is", "a","intelligent", "boy"]
print(" ".join(j))

# 9)Replace(): Replaces occurrences of a substring with another substring.
s = "Hello World"
print(s.replace("World", "Python"))

# 10)Find(): It finds the index value in the given string what we have to find as we can find the index values of some strings,characters or even double or signle spaces
space = "Hellloo I  am on the  moon"
print(space.find("  "))

# Escape Sequence Character
# 1. Backslash (\\)
# Used to include a literal backslash in a string.
print("This is a backslash: \\")  # Output: This is a backslash: \

# 2. Single Quote (\'')
# Used to include a single quote inside a string enclosed by single quotes.
print('It\'s a beautiful day!')  # Output: It's a beautiful day!

# 3. Double Quote (\")
# Used to include double quotes inside a string enclosed by double quotes.
print("She said, \"Hello!\"")  # Output: She said, "Hello!"

# 4. Newline (\n)
# Moves the text after it to a new line.
print("Hello\nWorld!")  # Output: 
# Hello
# World!

# 5. Tab (\t)
# Adds a horizontal tab space.
print("Name:\tJohn")  # Output: Name:   John

# 6. Carriage Return (\r)
# Moves the cursor to the beginning of the line, overwriting the existing content.
print("Hello\rWorld!")  # Output: World!



# CHAPTER 4 LISTS AND TUPLES
# Python lists are containers to store a set of values of any data type.
# As we know that we cannot change any extisting strings bcz they are imutable. 
# If we use arrays and lists we can change the data in it as they are mutable

fruit = ["Apple", "Orange", "Banana", "Grapes", "Kiwi"]#This is a type of list of strings we can even store boolean, integers or floating datatypes
print(fruit[0])#A list can be indexed just like a string.

fruit[1] = "Suiii" #As lists are mutable means changable so we can change them except creating a new one.
print(fruit[1])

# List Methods

exa = ["Moksh", "Suyash", "rythm", "Nitin", "Sanvi", "Aakash", "Rohan"]
num = [1,2,6,2,9,2,5,1,0]
# 1)Append(): Adds an element to the end of the list.This modifies the list in place and does not return anything.
exa.append("Swara") #It takes only one argument if we want to add many items we can use extend()

# 2)Sort():Sorts the list in ascending order (or descending with reverse=True)
num.sort() #This is in ascending order
# num.sort(reverse=True) #This is in descending order
print(num)

# 3)Extend():Adds elements of another list to the end of the current list.
exa.extend([1,2,3,4,5])

# 4)Insert():It inserts an element at a specific position.
num.insert(2, "Moksh")

# 5)Reverse(): Reverses the elements of the list in place.Means the last one will come at the first and it continues second last at the second place like this.
num.reverse()
print(num)

# 6)Pop(): Removes and returns the element at a specified index (default is the last element).
arr = [1,2,3,4,5,6,7,8]
arr.pop() #If there is no specified value so it will remove the last value as default
arr.pop(3) #It will remove the element on the 3th position
print(arr.pop(4)) #By printing the values like this you will be getting a return of a value which will say out the present element on the desired position

# 7)Clear(): Removes all elements from the list.
# arr.clear()
# print(arr)

# Tuples in python:-
# Tuples are better than lists when you want data that shouldn't change. They are faster, use less memory, and can be used as keys in dictionaries or elements in sets. Tuples also make your code clearer by showing that the data is fixed and won't be modified.
# The sign of a tuple is parentheses (). You can create and use tuples by placing items inside parentheses, separated by commas.
# It prevents modification of critical data

# Creating a Tuple:
tuple1 = (1,2,3, "Moksh", True, False, "Shivam")
print(type(tuple1)) 

# Empty Tuples:
empty_tuple = ()
print(type(empty_tuple))

# Single Element Tuple:
single_element = (5,)
print(type(single_element))

# Tuples Methods

# 1)Count(): Returns the number of times a specific value appears in the tuple.
my_tuple = (1, 2, 3, 1, 2, 1, 1,20)
print(my_tuple.count(1))  # Output: 4

# 2)Index(): Returns the index of the first occurrence of a specific value.
my_tuple1 = (10, 20, 30, 20)
print(my_tuple1.index(20))  # Output: 1

# 3)Membership Testing
print(20 in my_tuple)  # Output: True
print(40 in my_tuple)  # Output: False

# 4)Repetition:Repeat a tuple multiple times.
repeated = (5,) * 3  # Output: (5, 5, 5)
print(repeated)

# 5)Length(): It will give the length of the tuple
print(len(repeated))

# 6)Sum(): This will sum all the elements in the list present
print(sum(my_tuple1))



# CHAPTER 4 DICTIONARY AND SETS
# A dictionary in Python is an unordered, mutable, and indexed collection used to store key-value pairs. It allows for fast lookups, insertions, and deletions using hashing.
# In python a same value floating point number and a integer is termed same.For ex: 1.0 and 1 are equal according to python 
# Dictionaries are defined using {} with key-value pairs separated by ':'
# It is used for quick lookups and to access the values easily that we cannot do in the tuples or the lists
# PROPERTIES OF PYTHON DICTIONARIES:
# 1. It is unordered : The first key inserted appears first in the output when iterating.The second key inserted appears second, and so on.
# 2. It is mutable : Can be changed
# 3. It is indexed : In a dictionary, keys act as indexes instead of numerical positions.
# 4. Cannot contain duplicate keys : Dictionary keys must be unique. If you try to define a dictionary with duplicate keys, Python will overwrite the previous value with the new one.

# Dictionary Keys must be unique
marks = {
    "Moksh": 100,
    "Rohan": 67,
    "Sanvi":100,
    "Himanshu": 1
}

marks["Suii"] = 4 #It is used to add a new key-value pair into the dictionary. If the key-value is already there in the dictionary then so it will change the value of that key-value
print(marks)

# Dictionary Methods

fruits = {
    "Orange" : 78,
    "Apple" : 34,
    "Grapes": 28,
    "Mango": 100
}

# 1) Dictionary Keys: It gives all the keys present in the dictionary like Orange, Apple etc.
#print(fruits.keys())
#print(list(fruits.keys()))# You can also convert the keys into a list

# 2) Items(): Returns all key-value pairs as a view object.
print(fruits.items())

# 3) Values(): It return all the values in a dictionary
print(fruits.values())

# 4) Update(): It updates a particular key in a dictionary. If the key is not available in the dictionary it will add it and add its value too if given
fruits.update({"Grapes":29}) #We should use curly brackets to describe it as a dictionary and make updates in the other dictionary
print(fruits)

# 5) Get(): It is used to return the value of the specified keys
print(fruits.get("Grapes"))

# The difference between fruits["Grapes"] and fruits.get("Grapes") are:
# fruits["Grapes"] return an error if there is any Incorrect key written
# fruits.get("Grapes") If there is any wrong key written it will not return an error but print 'None'

# 6) Clear(): It clears the dictionary
# fruits.clear()

# 7) Copy(): It is used to create a independent copy of the orgininal dictionary. We can also use the assignment operator to this but there's a catch in assignment if we make changes in the original dict. it will affect the copy one also but its not same with the copy() method
new = fruits.copy()
print(new)

# 8) Popitem(): Remove and Return the Last Inserted Key-Value Pair
sui = new.popitem() #Here it return the Last Key-Value Pair and even removes it from the dict.
print(new)

# 9) Pop(): Removes and returns the value of the given key. If the key doesn’t exist, it returns the default value (or raises a KeyError if no default is provided).
ext = new.pop("Grapes") #It return the value present in grapes
print(new)
#print(new[1]) # This will return an error because the index can only be justified in keys or values forms not in forms of positions

# 10) Length(): It is used to give us the length of a dictionary which includes a pair of key-value pairs
len(new)

# Sets
# A set is an unordered collection of unique elements and sets are mutable. Sets are defined by enclosing elements in curly braces {} or by using the set()
# The elements written in sets must be immuatable like you cannot add Lists as they are mutable and even dictionaries
# It is unordered, Stores only values not the keys as compare to dictionaries, The elements must be unique
# Sets cannot be indexed

# Example of a set:-
s = {1,2,8,5,4,6,7,7} #If there's anything coming in repetition like here is 7 it will be printed only one's.As a set is unordered it will automatically sort the list and make it in a ascending(default) form.
l = [1,2,5,3,7,8]
s = set(l) #It helps to convert a list into a set

# Use set() when converting from another collection (list, tuple, dict keys).
# Use {} when defining a set directly for better readability and performance.

empty = set()# If you want to create a empty set you cannot create it by using curly brackets as it will make it a dictionary so else you can use set() to create a empty set

# Sets Methods
setex = {1,2,3,8,9,4, "Moksh", "Aaashu"} 
# 1) Add(): Adds an single element to the set
setex.add(24)

# 2) Update(): Adds multiple elements to the set.
setex.update(["Added", "None"])

# 3) Remove(): Removes the specified element from the set. Raises a KeyError if the element is not found.
setex.remove("Moksh")

# 4) Discard(): It also removes the specified element from the set. But it does not raise a KeyError of the element is not found.
print(setex.discard("Moksh"))#It will not raise any error but print None if the element is not found

# 5) Pop(): It is used to remove any random element from the set. Actually this method is not preferred in most cases. 
# But it any be usefull by selecting a random number to find out the winners of the lottery etc.
random = setex.pop()
# The pop() method removes an arbitrary element from setex.
# The removed element is assigned to the variable random.
# The original set setex is modified in place because sets are mutable.
print(random)

# There are two more important methods Union and intersection which should be there but as they contain deep language. I prefer to learn this from other sources like chatpgt or google.



# CHAPTER 6 CONDITIONAL STATEMENTS
# A conditional expression (also called a ternary operator) is a short way to write an if-else statement
# If the condition is True, return one value. Else, return another value.
# The if-else statement helps us make decisions in our program. It allows us to execute different code based on conditions.

age = int(input("Enter your age: "))

# Single If-else statements
if age>=18:
    print("Congrats you are eligible to vote")
else:
    print("Sad you are not eligible to vote")

# Indentation in Python is the use of spaces or tabs at the beginning of a line of code to indicate a block of code.For example here the print statements contain a tab spaces called indent
# If we want to leave the if else statements we will remove the tab spaces and start it from the new line

# If-elif-else Ladder
# It is used to represent many conditions that will be executed for this we uses elif which helps us to represent many conditions

sub = str(input("Enter your favourite subject: "))
if sub=="English":
    print("You will be a English Teacher one day")
elif sub=="Maths":
    print("You will be a great Mathematician")
elif (sub=="Science"):
    print("You will be a great Scientist")
elif sub=="Computer":
    print("Congrats you are like me")
else:
    print("Invalid Statement")

print("Here the program ends")#Here the if-elif-else ladder ends

# Now here's a catch somes. As we know we can use if statements too instead of elif. But kindly never do this the reasons are:-
# If you use multiple if statements instead of elif, the program will check all conditions independently, even if an earlier condition is already True.
marks = 35

if marks >= 90:
    print("Grade: A")
# 1st If statement has been ended

if marks >= 80:#As it contains a elif statement 'if' is no more independent 
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")

# The program checks all if conditions, even after finding a match.
# Since marks = 85, both marks >= 80 and marks >= 70 are True, so it prints both "B" and "C", which is incorrect.
# If a condition don't have any else statements and all the if-elif resulted false then nothing will be printed.

# RELATIONAL OPERATORS 
# Relational Operators are used to evaluate conditions inside the if statements. Some 
# examples of relational operators are: 
# ==: equals. 
# >=: greater than/ equal to. 
# <=: lesser than/ equal to.

# LOGICAL OPERATORS 
# In python logical operators operate on conditional statements. For Example: 
# and – true if both operands are true else false. 
# or – true if at least one operand is true or else false. 
# not – inverts true to false & false to true.
# IN Command:-
# in works when comparing a single string to a list (exact match required).
# in works when checking a substring inside a larger string.
# in does NOT work if you try to compare a whole list to a string.
lis = ["Make a lot of money", "buy now", "subscribe this", "click this"]
st = input("Enter the comment: ")
if(lis[0] in st or lis[1] in st or lis[2] in st or lis[3] in st):
    print("Yes it is a scam")
else:
    print("No it is not a scam")
# Or
text = input("Enter the text: ")
if("Moksh" in text):
    print("Yes the text is about Moksh")
else:
    print("No the text is not for Moksh")



# CHAPTER 7 LOOPS
# A Loop in programming is a command that repeats a set of instructions multiple times. 
# Loops are used to save time, reduce errors, and make code more organized it also helps us in avoiding code repetions
# There are two types of loops in python, 'for' loops and 'while' loops 
# If we entered into a loop it will run until the given condition becomes false
# For example we have to write 1-5 numbers in normal we do like this-
print(1,2,3,4,5)
# The same task can be done through the help of loops
for i in range(1,6):
    print(i)

# WHILE LOOPS:-
# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
# It is useful when the number of iterations is not known beforehand and depends on some condition.
# The syntax of while loop is
# while condition:
     # Code block to execute

i = 1
while(i<4):
    print(i)
    i+=1

# While Loops in List
l = ["Moksh", "Sanvi", "Aashu","Meet",False,True,69]
i=0#We should always define the variable before that will be used in the loop 
while(i<len(l)):
    print(l[i])
    i+=1

# Common mistakes done that will result in infinite loop
# l = ["Moksh", "Sanvi", "Aashu","Meet",False,True,69]
# while(i < len(l)):  ❌ 'i' is not defined before use
#     i = 0  ❌ Resetting 'i' to 0 on every iteration
#     print(l[i])
#     i += 1  # ❌ This doesn't increment i correctly

# Some main keypoints of WHILE LOOP are :-
# 1) A variable should be initialized before the loop.
# 2) The loop variable should be modified inside the loop to avoid infinite loops.
# 3) If the condition never becomes False, the loop runs forever.
# 4) If you want to avoid infinite loop you can use break statements.
# 5) Use while loops when the number of iterations is unknown. Some real-life examples of this are Keep asking the user to enter a password until they enter the correct one.


# FOR LOOPS
# Unlike while loops, for loops in Python automatically handle the assignment and increment of the loop variable.
# Python’s for loop works by using something called an iterator. The loop variable (like i) gets its value from an iterator, which automatically moves to the next item of a list,tuple or any other elements in each iteration.

for i in range(3):  # range(3) → [0, 1, 2]
    print(i)

# What is happening in this code:
# 1)range(3) creates an iterator that generates numbers: [0, 1, 2].
# 2)The loop automatically takes the first value (0) and assigns it to i.
# 3)The body of the loop (print(i)) runs.
# 4)Python automatically moves to the next value (1) and assigns it to i.
# 5)The loop repeats with i = 1, then i = 2.
# 6)When all values are used, the loop stops automatically.

# For loops in list
for i in l:
    print(i)

# For loops Slicing
# In the range(start, stop, step) function, the third value (step) specifies the increment or decrement between consecutive numbers in the sequence.
for i in range(4,20,2):
    print(i)

# For loops in Strings
txt = "Moksh"
for i in txt:
    print(i)

# For loops in Tuples
tup = (2,4,7,9,3,7,5)
for i in tup:
    print(i)

# For loops in Dictionaries
dic = {
    "Moksh":78,
    "Sole":80,
    "Spirit":33
}
for i in dic.values():
    print(i)

# For loop with else
# Else is used when the loop stop or finishes
for i in range(1,3):
    print(i)
else:
    print("Here the loop ends")

# Break Statements
# Break is used when we want to exit the loop right now
for i in range(50):
    if i==5:
        break# Exit the loop right now if i value becomes 5
    print(i)

# Continue Statements
# It is used when we have to skip a particular iteration
for i in range(10):
    if i==5:
        continue
    print(i)

# Pass statements
# The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. 
# To just pass the loop to complete it in future we use this statement
for i in range(0,5):
    pass

# Argument in print statement
# End is a argument in print statement used to print the elements in a single line.
for i in range(1,5):
    print(i,end="")#This will print the numbers from 1 to 5 in a sinngle line

# Nested Loops
# Loop inside another loop is nested loop
num = int(input("Enter the number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end="")
    print()



# CHAPTER 8 FUNCTIONS & RECURSIONS
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



# CHAPTER 9 FILE IO
# File I/O in Python refers to reading from and writing to files. Python provides built-in functions to handle file operations using the open() function.

# Volatile storage is a type of memory that loses its data when power is turned off. Ex: RAM
# Volatile memory is important as it is used to load the programs faster and after closing the program vanishing the data to load any other program much more faster

# Non-volatile storage retains its data even when power is turned off. Ex: SSD, HDD
# Used for permanent or long-term storage of files, operating systems, and applications.

# Persistent storage is a data storage device that keeps data even when the device is powered off. Ex: Databases, Cloud Storage devices(Googlee drive, Dropbox)
# Ensures data is structured, retrievable, and accessible over time (databases, cloud storage, logs).

# There are 2 types of files:
# 1. Text files (.txt, .c, etc) 
# 2. Binary files (.jpg, .dat, etc)

# OPENING A FILE 
# Python has an open() function for opening files. It takes 2 parameters:  filename and mode.
# The open() function can create a new file if it does not already exist, but it depends on the mode you use.

open2 = open("9_File_io_example.txt", "r") #In this we are opening a file containing some text. The task to be performed is written in the mode option. By default it's r(read)
read = open2.read() #Reading the context of the open file and storing it on the variable
open2.close() #After opening a file we should close it to don't get any problems in the code
print(read)

txt = "Hello Moksh I am writing this text in vscode editor and you are redirected"
# f = open("Sample.txt" , "w") This will create a new file named Sample.txt if it don't exists
# f.write(txt) Write function is used to write text into a file having mode set to "w" if some content is already written in it, it will overwrite that
# f.close() Always remember to close a file if opened for any reasons
# reading = f.read() This will read the content of the file
# f.close()
# print(reading)

# ReadLines Functions
# The readlines() function in Python reads all lines from a file and returns them as a list of strings.

# The readline() function reads one line at a time from a file and remembers the position, so when called repeatedly, it reads the next line each time.
# readline = open("Sample.txt").readline() # Readline returns a single line from the file and remember the position
# file = open("3_Strings.py") #Readlines return all the text written in the file in a form of a list
# f1 = file.readline()
# print(f1)
# f2 = file.readline()
# print(f2)
# f3 = file.readline()
# print(f3)
# file.close()

# To reduce these lines of code we can write it in a loop
f = open("9_File_io_example.txt")
f1 = f.readline()
while(f1 != ""):
    print(f1)
    f1 = f.readline()

# Appending
# This is used when we want to add or append some text into the file except overwriting it
appending = open("Sample.txt", "a")
for i in range(1,5):
    appending.write("Hello bro I am Moksh jain. This text is added")
    i+=1
appending.close()

# With Statement
# The best way to open and close the file automatically is the with statement. 
# with expression as variable:
    # Code block (where resource is used)

with open("9_File_io_example.txt", "w") as file:
    file.write("Hello This a sample file")

# Some important things to keep in mind:
# The + symbol in a file mode means that the file is opened for updating, which allows both reading and writing.
# It is used in combination with r, w, or a:
# 'r+' → Open for reading and writing, but the file must exist.
# 'w+' → Open for reading and writing, but the file is truncated (cleared) if it exists or created if it doesn’t.
# 'a+' → Open for reading and appending, but does not truncate. The file is created if it doesn’t exist.