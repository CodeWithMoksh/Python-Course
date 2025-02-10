# hindi = {
#     "Chalu": "Clever",
#     "Khamosh": "Quiet",
#     "Pagal": "Mental",
#     "Chuha": "Mouse",
#     "Kapde": "Clothes"
# }

# word = input("Enter the Word you want:")
# print(hindi.get(word,"Not found"))
# set1 = set()
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# num1 = int(input("Enter the 1 number"))
# set1.add(num1)
# print(set1)

# set1 = {18,"18","78"}
# print(set1)

# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(len(s))

# dic = {}
# f1 = input("Enter your one favorite subject: ")
# n1 = input("Enter your name: ")
# f2 = input("Enter your one favorite subject: ")
# n2 = input("Enter your name: ")
# f3 = input("Enter your one favorite subject: ")
# n3 = input("Enter your name: ")
# f4 = input("Enter your one favorite subject: ")
# n4 = input("Enter your name: ")
# dic.update({f1:n1,f2:n2,f3:n3,f4:n4})
# print(dic)

# s = {8, 7, 12, "Harry", [1,2]}


# marks = int(input("Enter your marks: "))
# if marks>=32:
#     print("Congrats you are pass")
# if marks==32:
#     print("You are just pass")
# elif marks<=32:
#     print("Sorry you are Failed")
# elif marks<27:
#     print("You need to work hard")

# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))
# num3 = int(input("Enter the number 3: "))
# num4 = int(input("Enter the number 4: "))

# if(num1>num2 and num1>num3 and num1>num4):
#     print(f"The Greatest number is: {num1}")
# elif(num2>num1 and num2>num3 and num2>num4):
#     print(f"The Greatest number is: {num2}")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print(f"The Greatest number is: {num3}")
# elif(num4>num1 and num4>num2 and num4>num3):
#     print(f"The Greatest number is: {num4}")

# mark = int(input("Enter marks of 1st subject: "))
# mark2 = int(input("Enter marks of 2st subject: "))
# mark3 = int(input("Enter marks of 3st subject: "))
# per = ((mark+mark2+mark3)/300*100)

# if(per>=40 and mark>=33 and mark2>=33 and mark3>=33):
#     print("You are passed:",int(per))
# else:
#     print("So sorry you just failed:",int(per))

# text = input("Enter the text you have received from the company: ")
# lis = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# if(lis in text):
#     print("Yes you are being scammed")
# else:
#     print("No bro it's correct no spam")

# surname = input("Enter your username: ")

# if(len(surname)<10):
#     print("Your surname has less than 10 characters")
# else:
#     print("Your surname contains more than 10 characters")

# name = input("Enter your name: ")
# l = ["Rohan", "Sanvi", "Moksh", "Suyash","Ram","Aryaman"]
# if(name in l):
#     print("Yooo there's it is")
# else:
#     print("No sorry")

# marks = int(input("Enter your marks: "))

# if(marks>=90):
#     print("Your grade is: Ex")
# elif(marks>=80):
#     print("Your grade is: A")
# elif(marks>=70):
#     print("Your grade is: B")
# elif(marks>=60):
#     print("Your grade is: C")
# elif(marks>=50):
#     print("Your grade is: D")
# elif(marks<50):
#     print("Your grade is: F")

# text = input("Enter the text: ")
# if("Harry".lower() in text.lower()):
#     print("Yes the text is about Harry")
# else:
#     print("No the text is not for harry")

# l = "Moksh"
# for i in l:
#     print(i)

# ic = {
#     "Moksh":78,
#     "Sole":80,
#     "Spirit":33
# }
# for i in ic.values():
#     print(i)

# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{num}*{i}=", num*i)

# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for i in l:
#     if(i.startswith("H")):
#         print(f"Greeting to {i}")
#     else:
#         pass

# i=1
# num = int(input("Enter the number: "))
# while(i<11):
#     print(f"{num}*{i}= {num*i}")
#     i+=1

# num = int(input("Enter the number: "))
# for i in range(2,num):
#     if(num%i == 0):
#         print("Your number is not a prime number")
#         break
#     else:
#         print("Yes it is a prime number")

# n = int(input("Enter the number: "))
# sum = 1
# for i in range(1,n+1):
#     sum*=i
# print(f"The factorial of {n} is {sum}")
'''
  * 
 *** 
*****
'''
# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print("*",end="")
#     print()

# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     print

# num = int(input("Enter the number: "))
# for i in range(10,0):
#     print(f"{num} X {i} = {num*i}")

# num = int(input("Enter the number: "))
# for i in range(10,-1,-1):
#     print("The counting starts:",i)

# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
# print(greatest(5,2,3))

# def celsius(c):
#     return print(f"{c} degrees to farenhiet is:",(c*9/5)+32)
# cel = int(input("Enter the celsius degrees: "))
# celsius(cel)

# def natural(n):
#     if (n==1):
#         return 1
#     else:
#         return n + natural(n-1)

# print(natural(10))

# def star(n):
#     if(n==0):
#         return
#     else:
#         return print("*"*n),star(n-1)

# star(10)

# def inches(c):
#     return print(f"{c} inches to cms is:",(c*2.54))
# cel = int(input("Enter the inches: "))
# inches(cel)

# lis = ["Moksh", "Suii", "Su", "HelloSu", "Namasu"]
# def rem(lis,name):
#     n = []
#     for i in lis:
#         if not(i==name):
#             n.append(i.strip(name))
#     return n

# print(rem(lis, "su"))

# def multiply(n):
#   for i in range(1,11):
#     print(f"{n} X {i} = ",n*i)
# multiply(3)