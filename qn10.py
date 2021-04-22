'''Write a Python program to sum of three given integers. However, if two values are equal sum will be zero'''
num1=int(input("enter the number:"))
num2=int(input("enter the number"))
num3=int(input("enter the number:"))
if num1!= num2!=num3:
        add=num1+num2+num3
        print(add)
if num1==num2:
    print("zero")
elif num2==num3:
    print("zero")
elif num1==num3:
    print("zero")