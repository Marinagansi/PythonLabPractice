'''
Check whether the given year is leap year or not. If year is leap
print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: •a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100•
a year is always a leap year if its number is exactly divisible by 40
'''
year=int(input("enter the year:"))
if year%4==0and yea%!=100 :
    if yea%400==0:
    print("LEAP YEAR")
else:
    print("common year")