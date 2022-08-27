# Leap year is on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#       unless the year is also evenly divisible by 400

year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0:
    print(f"The year {year} is a leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")


"""
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
"""