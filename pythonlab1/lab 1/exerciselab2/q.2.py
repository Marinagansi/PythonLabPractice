#wap which accepts marks of four subjects and display  total marks, percentage and grade
#hint mare that 70 %-distiction, more than 60%-first, mar tha 40%-pass, less than 40%-fail
math=float(input("enter the number:"))
science=float(input("enter the number:"))
social=float(input("enter the number:"))
eng=float(input("enter the number:"))
total=math+science+social+eng
#for math
percent=total/400*100
print(f'the total mark is {total}')
print(f'obtain {percent}')
if percent>70:
    print("distinction")
elif percent>60:
    print("first division")
elif percent >40:
    print("pass")
else:
    print("fail")
