'''given  three integer ,print the smallest one'''
num_1= int(input('enter the number:'))
num_2=int(input("enter the number:"))
num_3=int(input("enter the number:"))
if num_2>num_1<num_3:
    print(f'{num_1} is the smallest')
elif num1>num_2<num_3:
    print(f"{num_2} is the smallest")
else:
    print(f"{num_3}  the smallest")