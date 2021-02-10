# program that inouts a number and outputs whether it's even or not
# Author: Caoimhin Vallely

number = int(input("Enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))