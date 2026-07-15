#The Magic Calculator
def add(n1,n2):
    print(f"{n1} + {n2} = {n1+n2} ")
def subtract(n1,n2):
    print(f"{n1} - {n2} = {n1-n2} ")
def multiply(n1,n2):
    print(f"{n1} * {n2} = {n1*n2} ")
def divide(n1,n2):
    try:
        print(f"{n1} / {n2} = {n1/n2} ")
    except ZeroDivisionError:
        print(f"Error: the second number is zero.")       
num1=int(input("enter a number of your choice "))
num2=int(input("enter another number "))
sign=input("which operation: +,-,*,/\n")
try:
    if sign=="+":
        add(num1,num2)
    elif sign=="-":
        subtract(num1,num2)
    elif sign=="*":
        multiply(num1,num2)
    elif sign=="/":
        divide(num1,num2)
    else:
        raise TypeError("Unrecognized sign")
except TypeError as e:
    print(f"Error: {e}")        