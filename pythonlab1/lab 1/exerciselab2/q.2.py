#wap which accepts marks of four subjects and display  total marks, percentage and grade
#hint mare that 70 %-distiction, more than 60%-first, mar tha 40%-pass, less than 40%-fail
math=int(input("enter the number:"))
science=int(input("enter the number:"))
social=int(input("enter the number:"))
eng=int(input("enter the number:"))
total=math+science+social+eng
#for math
percent=total/400*100
print(f'the total mark is {total}')
print(f'obtain {percent}')
if percent>70:
    print("distiction")
elif percent>60:
    print("first division")
elif percent >40:
    print("pass")
else:
    print("fail")
