# Task 1.2 - Date Of Easter
# Given the year, find the date which Easter lands on in that year
# https://en.wikipedia.org/wiki/Date_of_Easter

year=int(input("Enter a year to calculate the date of Easter: "))
a=year%19
b=year%4
c=year%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7
date=22+d+e
if year==1954 or year==1981 or year==2049 or year==2076: date-=7
if date>31: print("The date of Easter in year "+str(year)+" is "+str(date-31)+" April.")
else: print("The date of Easter in year "+str(year)+" is "+str(date)+" March.")