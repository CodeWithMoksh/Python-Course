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
# Break is used when we want to exit the loop right now. Python’s break always terminates the nearest enclosing loop (like while or for), not the if, else, or try.
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