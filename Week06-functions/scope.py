# messing with scope
# Author: from Andrew Beatty lecture

var = 10

def cube(num):
    # global var
    var = 66
    print("in function var is ", var)
    return num ** 3

print(cube(4))
print("outside function var is ", var)