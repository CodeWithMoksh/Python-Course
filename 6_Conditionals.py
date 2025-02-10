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
# There can be any number of elif statements. 
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
if("Harry" in text):
    print("Yes the text is about Harry")
else:
    print("No the text is not for harry")
