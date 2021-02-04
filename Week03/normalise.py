# This program reads in a string and strips
# any leading or trailibg spaces.
# It also converts all the letters to lower case.
# Also outputs the length of the original string
# and the normalised one.

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That String normalised is :{}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised))