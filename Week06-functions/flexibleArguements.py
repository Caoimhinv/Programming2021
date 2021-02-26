# more messing with functions
# from Andrew Beatty week 06 lectures

# print ("hi", 55, 343, [], {}, sep=":")

def average(*numbers):
    sumOf = sum(numbers)
    return sumOf / len(numbers)

ave = average (12, 13, 14, 131, 174, 220)
print ("average is ", ave)

def fun(arg1 = 0, arg2 = 1):
    return arg1 - arg2

print(fun(2))

def funkyArgs(**args):
    print (args)

funkyArgs(name = "joe", age = 33, courses = [])