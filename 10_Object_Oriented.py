# Object-Oriented Programming (OOP) is a way of writing programs using objects and classes.
# It helps in organizing code, making it reusable, and keeping it clean.


# Classes: In Object-Oriented Programming (OOP), a class is a blueprint for creating objects
class Student:
    name = "Moksh"
    section = "D"
    age = "17"


# Object: An object is an instance(a specific object created from a class) of a class or we can say an object is a real thing made from the blueprint.
student1 = Student() #This is an object which contains all the data of the class and presents in real life
print(student1)


# Constructors
# A special method (__init__()) that runs when an object is created. It runs automatically when ClassName() is called. If you don’t define one, Python adds an empty constructor.
class Student2:
    def __init__(self, fullname):
        self.name = fullname

studentdetails = Student2("Moksh")
print(studentdetails.name)

# 1) The new variables created in the object are called attributes. For ex: In (self.name) we are creating a variable inside the object using a attribute
# 2) A method is a function that is associated with an object or a class, used to define the behavior of that object or class and perform specific actions on it.
# 3) The self parameter is essential in Python classes because it refers to the object being created. If we removed self, Python will throw an error.
# 4) self is **not a keyword** but just a convention. You **can** use another name, but it's not recommended as a good practise

# There are two types of Constructors
# a)Default constructors: These are the constructors in which only 'self' is given as the parameter. If it is not specified or not mention, Python will automatically specify one for the process
# b)Paramaterized constructor: These are the constructors in which more than one parameters are specified(including self).

# Some more special Constructors
# 1) __str__() : The __str__() method acts like a constructor for displaying objects in a readable format when print(object) is called.
# def __str__(self):
        # return f"Kindly don't do this, it will only print the location of object"

# 2) Copy : A copy constructor is used to create a new object with the same values as another object.
# def copy(self):  # Copy constructor
        # return Student(self.name, self.age)
# student2 = student1.copy()  # Creates a new object with same values


# Attributes
# There are two types of attributes: Class attributes and instance attributes

# Class Attribute :  Defined at the class level (outside __init__()).Shared by all objects (same value for every instance).Changes made to a class attribute affect all instances.
# In shortly it is defined outside every function and each and every object as to follow its created value.
class Car:
    color = "red" #Class attr
    def __init__(self, brand):
        self.brand = brand
car1 = Car("mercedes")
car2 = Car("BMW")
print(car1.color) # Accessing class attr

# We can change the value of class attr by these methods:-
Car.color = "blue" #This will change for all the object
car1.color = "orange" #This will change for only one object


# Instance Attribute : Defined inside __init__() using self.Each object has its own separate copy.Changing an instance attribute does NOT affect other instances.
# Inshortly we can say that it is defined inside the function and each object as seperate access to these instances
class Bag:
    color = "Orange"
    def __init__(self, brand):
        self.brand = brand #Instance attribute
bag = Bag("LouisVuiton")
print(bag.brand) #Accessing the instance attribute seperate for each object


# Methods
# A method in Python is a function inside a class that operates on objects of that class.Defined using def inside a class.Takes self as the first parameter (so it can access instance attributes).
class Student5:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def greet(self):  # Instance Method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

student1 = Student5("Moksh", 17)
print(student1.greet())
# Output: Hello, my name is Moksh and I am 17 years old.


# Static Methods
# Methods that don't use the self parameter(work at class level)
# These are used with some function in which we don't have any need to specify the self parameter.

class Student6:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    @staticmethod #This is a decorator needs to be specified before creating creating a static method 
    def hello():
        print("Hello this is a static method")

# Decorator allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
# 1)"Decorator allows us to wrap another function":
# Think of a decorator as a gift wrapper. You take an existing function (the "gift") and wrap it with some extra code (the "wrapper") to add new features or behavior.
# 2)"Extend the behavior of the wrapped function":
# The wrapper adds something extra to the original function. For example, if your original function just says "Hello," the decorator can make it say "Hello" and do a dance.
# 3)"Without permanently modifying it":
# The original function stays the same. You’re not changing its code. Instead, you’re just adding a temporary layer (the decorator) that enhances it when you call it.


# DEL Keyword
# It is used to delete the properties of the object or the whole object
stu = Student6("Moksh", 18)
del stu.name #This will delete the property of stu object


# Private Attributes and Methods
# We can make any attribute or a method private which can only be accessed inside the class not outside it
# By using '__' in starting of the attribute or method name it makes it private.
# Use of making the methods private :- It is mostly used by the other functions for their own processing.  
class Person:
    __password = "184628465" #Private attribute
    @staticmethod
    def __help(): #Private method
        print("Hey I need Help")
per = Person()
#per.__help() This will through an error as __help is private and unaccessable
#print(per.__password) This will pass an error


# Important Terms
# 1) Encapsulation :- Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class).
# For Example of a capsule -
# The medicine (data) is protected inside the capsule.
# You can’t open the capsule directly.
# You can only take it as prescribed (use public methods to access data).


# 2) Abstraction:-  Abstraction means showing only the important details and hiding the complex implementation.Users should only see what they need to use and not the internal complexity.
# For Example of a mobile phone - You press a button to make a call (you don’t need to know how signals work internally).The internal working (radio waves, processing) is hidden from the user.


# 3) Inheritance:- Inheritance is a feature in Object-Oriented Programming (OOP) where one class (child class) gets the properties and methods of another class (parent class).It allows code reuse and avoids writing the same code multiple times.
# class Animal(): #Parent
#     def speak(self):
#         return "Hello I can speak aloud"

# class Dog(Animal): #Child
#     def bark(self):
#         return "Baaoo Baaaoooo"
    
# class Cat(Animal, Dog): #Multiple Inheritance
#     def meow(self):
#         return "Meooowww"

# dog = Dog()
# print(dog.speak())
# print(dog.bark())

# As we can see Animal is the parent of Dog. Dog is accessing the properties of Animal. Likewise there are three types of inheritance:-
# 1) Single Inheritance – One parent, one child. Means the there is only one parent and one child using its property
# 2) Multiple Inheritance – One child, multiple parents. Means there are multiple parents and only one child are their are properties
# 3) Multilevel Inheritance – Grandparent → Parent → Child. Means the properties are being transferrend from one grandfather to its father and again to its child


# Class Method:-
# A class method in Python is a method that works on the class itself, not on individual objects.
# It is defined using the @classmethod decorator.
# It takes cls as the first parameter instead of self.
# It can modify class attributes (shared across all objects).

class Employeee:
    name = "Moksh"

    @classmethod
    def get_name(cls):
        print(f"Hello {cls.name}, You are a brilliant student")

emp = Employeee()
emp.name = "Sanvi"
print(emp.get_name())


# Super Method:-
# super() is a built-in function in Python that allows a child class to call methods from its parent class.
class Car:
    def __init__(self, type): 
        self.type= type #In this we are creating a type attribute for car

    def get_type(self):
        return (f"Your car model is {self.type}")

class ToyotaCar(Car): #Get the Properties of Car
    def __init__(self, name, type): #We gave the type as a parameter such that we can take the value of it and give to Car.
        super().__init__(type) #In this we are calling the __init__ constructor of Car in which we are passing the value of type(given as parameter which we will specify in the object). By calling the init it will run its inner function which is (self.type = type). So the type will be assigned to the type attribute in Car class.
        self.name = name

    def get_details(self):
        print(f"Your car name is {self.name} and {self.get_type()}") #In this we can see that the type value which we will pass in the obj is assigned to self.type in Car() class through which we are able to access the get_type method which requires the type as a parameter

car1 = ToyotaCar("Toyota", "Petrol")
car1.get_details()


# Property Decorator
# The @property decorator in Python allows a method to be accessed like an attribute.
#  It converts a method into a property, meaning you can call it without parentheses ().
class Marks:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def per(self):
        return {((self.phy + self.chem + self.math)/3)}

mark = Marks(98, 99, 100)
mark.math = 80
print(mark.per) # No need for '()' as it behaves like a attribute


# IsInstance Function
# The isinstance() function in Python is used to check if a variable belongs to a specific data type or class. Returns True if the object is an instance of the specified class/type. Returns False otherwise.
v = ""
if isinstance(v, int): # The first parameter is the obj we want to check and the second parameter is the data type the object should be from.
    print("Yeahh it is a integer")
else:
    print("So sorry it is not a integer")


# Getters and Setters

# Getter: A method that retrieves (gets) the value of a private attribute.
# Setter: A method that modifies (sets) the value of a private attribute, usually with validation.

# For example we take a analogy of a real life situation which is of a bank locker:-
# The key to open the locker = Getter → Allows you to access your valuables safely.
# The bank rules to store items = Setter → Ensures that only valid items (jewelry, documents) can be stored

class BankLocker:
    def __init__(self, lock_number):
        self.__locker_number = lock_number #Private attribute so it cannot be accessed and changed by other users

    def get_number(self): # Getter Method
        return self.__locker_number
    
    def set_number(self, value): #Setter Method
        if isinstance(value, int) and value > 0:
            self.__locker_number = value
        else:
            raise ValueError("Sorry you are passing a wrong number try passing above 0")
        
bank1 = BankLocker(787)
#Getting the Number
print(bank1.get_number())

#Setting the Number
bank1.set_number(453)
print(bank1.get_number())

#Trying with a different data type
# bank1.set_number("453")
# print(bank1.get_number()) #This Raises a ValueError bcz the data type specified is integer