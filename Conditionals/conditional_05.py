year = int(input("Enter the year:"))

if (year == 400) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not")