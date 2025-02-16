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
open = open("9_File_io_example.txt", "r") #In this we are opening a file containing some text
read = open.read() #Reading the context of the open file and storing it on the variable
open.close() #After opening a file we should close it to don't get any problems in the code
print(open)
