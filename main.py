import sys
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    print(f"Checking the year: {year}")

    leap = False
    # Write your logic here
    validYears = list(range(1900, 100001))

    if year in validYears:
        print(f"year: {year} in range.")
        if year % 4 == 0 and year % 100 == 0:

            if year % 400 == 0:
                leap = True
                return leap
            else:
                leap = False
                return leap

        elif year % 4 == 0 and year % 100 != 0:
            leap = True
            return leap
        
        else:
            leap = False
            return leap
            
    else:
        print(f"Please enter a year bewteen 1900 to 100,000 (inclusive).")
        sys.exit()

year = sys.argv[1]

try:
    year = int(year)
except ValueError:
    print("Please enter numbers only.")
    sys.exit()

print(f"You entered: {sys.argv[1]}")

result = is_leap(year)
print(result)

#  the years 2000 and 2400 are leap years
#  while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
