# This program reads in numbers until
# the user enters 0
# it will then print them back out again
# and their average
# Author: Caoimhin Vallely

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("enter another number (0 to quit): "))

for x in numbers:
    print (x)

# I want the average to be a float
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))
print(numbers)
print(type(numbers))