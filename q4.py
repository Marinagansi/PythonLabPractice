#given three integer,print the smallest one
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num2>num1<num3:
    print("num1 is smallest")
elif num1>num2<num3:
    print("num2 is the smallest")
elif num1>num3<num2:
    print("num3 is the smallest")