"""
In the georgia calender, three conditions are used to identify a leap year:
1. The year is evenly divisible by 4; is a leap year, unless:
2. The year is evenly divisible by 100; it is NOT a leap year, unless:
3. The year is evenly divisible by 400; then it is a leap year.
this means that in thr georgia calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 
2100, 2200, 2300 and 2500 are NOT leap years.

"""

def is_leap(year):
    leap=False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True    

    return leap

year = int(input())
print(is_leap(year))