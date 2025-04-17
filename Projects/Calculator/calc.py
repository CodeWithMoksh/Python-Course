print("Here are the operators on which you can perform the calculations: \nAddtion(+) \nSubtraction(-) \nDivision(/) \nMultiplication(*)")

num1 = int(input("Enter the first number of your expression: "))
opr = input("Enter the operator: ")
num2 = int(input("Enter the second number of your expression: "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

if opr == "+":
    print(add(num1, num2))
elif opr == "-":
    print(sub(num1, num2))
elif opr == "*":
    print(mul(num1,num2))
elif opr == "/":
    print(div(num1,num2))
else:
    print("So sorry but can't understand your written text")