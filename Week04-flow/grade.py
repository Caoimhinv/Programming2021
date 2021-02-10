# This program reads in a students percentage
# and prints out the corresponding grade
# Author: Caoimhin Vallely

percentage = float(input("Enter the percentage:"))

percentageRounded = round(percentage)
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentageRounded < 40:
    print("Fail")
elif percentageRounded < 50:
    print("Pass")
elif percentageRounded < 60:
    print("Merit 1")
elif percentageRounded < 70:
    print("Merit 2")
else:
    print("Distinction")