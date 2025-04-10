# String is a datatype in python it is used to store the characters and even sometimes even the numbers in string form
# When we say strings are immutable in Python, it means that once a string is created, its content cannot be changed. You cannot change them by running functions on them.
# If anything written in Single cots(''), Double Cots("") or Triple Cots(''' ''') can be considered as a string.
# Single and double quotes are used for single-line strings, while triple quotes are used for multi-line strings and docstrings. Triple quotes can also include both single and double quotes without escaping them.

a ='Moksh' # Single quoted string
b = "Moksh" # Double quoted string
c = '''Moksh''' # Triple quoted string

# If we want to find any strings length we will be using len() command
print(len(a)) 


# String Slicing
# It allows you to extract a portion of a string by specifying a start and end index. It follows the format string[start:end].
# Suppose we have a string "Moksh" its character starting would be from index 0. So in this if we count from zero there will be 4 charcaters
# If we want to start the counting from the ending we will start from -1 .Like -1,-2....
# For more you can go through this https://i.ytimg.com/vi/BhmsJAzIp6w/maxresdefault.jpg

# sl = name[index_start:index_end]
nameshort = b[4:0] #In this we have to first put the variable name whom we have to slice and then by opening the brackets and writing the starting and end_point. But excluding the end_point which is 4(it will only print the object till 3)
nameshort1 = b[2] #This will be printing one character
nameshort2 = b[:4] #This means that the ind_start is 0 and the ind_end is 4
nameshort3 = b[2:] #This means that the ind_start is 2 and the ind_end is last length of the string
print(nameshort3)

alpa = "abcdefghijklmnopqrstuvwxyz"
print(alpa[0:9:4]) #This will first process the characters 0 to 9 and after is it will give starts skiping 4 characters from the list obtained
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

# 11)Split(): Cut the String into Pieces. This function is very important and used in many projects. This is being used to seperate the string into parts. The best ex. we can take is of a file name we want to extract by removing its extention.
# .split(separator) cuts a string into parts, wherever it finds the separator.It returns a list of parts.By default, it splits on spaces if no separator is given.
message = "Moksh Jain: Hello there!"
parts = message.split(':')
print(parts)
# You can tell .split() to only split once: This is used when the seperator is coming in the string multiple times and we want only some parts to be seperated
line = "Pari Didi: How are you doing?"
name, msg = line.split(':', 1)
print(name, msg)

# 12)Any(): The any() function is a built-in Python function that checks if at least one value in an iterable (like a list, tuple, or generator) is True. It is better than loops as they check all the values even after getting True
# It returns True immediately when it finds the first True.
# Best Method to use with loops
numbers = [0, 0, 4, 0]
print(any(num > 0 for num in numbers))  # Output: True


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