# program that requests inputs until user enters -1
# Author: Caoimhin Vallely

Answer = -1

number = int(input("Enter an integer:"))

while number != Answer:
    print("Nope!")
    number = int(input("Enter another integer:"))

print ("Well done!")