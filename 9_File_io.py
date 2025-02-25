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