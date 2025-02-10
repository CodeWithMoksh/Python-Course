# Python lists are containers to store a set of values of any data type.
# As we know that we cannot change any extisting strings bcz they are imutable. 
# If we use arrays and lists we can change the data in it as they are mutable

fruit = ["Apple", "Orange", "Banana", "Grapes", "Kiwi"]#This is a type of list of strings we can even store boolean, integers or floating datatypes
print(fruit[0])#A list can be indexed just like a string.

fruit[1] = "Suiii" #As lists are mutable means changable so we change them except creating a new one.
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

# 5)Reverse(): Reverses the elements of the list in place.
num.reverse()
print(num)

# 6)Pop(): Removes and returns the element at a specified index (default is the last element).
arr = [1,2,3,4,5,6,7,8]
arr.pop() #If there is no no specified value so it will remove the last value as default
arr.pop(3) #It will remove the element on the 3th position
print(arr.pop(4)) #By printing the values like this you will be getting a return of a value which will say out the present element on the desired position

# 7)Clear(): Removes all elements from the list.
# arr.clear()
# print(arr)


# Tuples in python

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