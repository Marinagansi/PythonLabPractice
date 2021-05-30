'''if name is less than 3 characters long name must be at least 3 characters otherwise if it's more than
50 character -name must be maximum of 50 characters otherwise-name looks good!'''
name=len(input("enter the name"))

if (name)<3:       # we can do len(name)
    print("name must be  at least 3 char")
elif name>50:
    print("name must be maximum 50 char")
else:
    print("name looks good")