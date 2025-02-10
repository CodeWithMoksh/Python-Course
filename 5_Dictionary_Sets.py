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