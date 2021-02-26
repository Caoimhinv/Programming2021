# anonymous functions
# lamda
# Author: Andrew Beatty

# def doubler (num):
    # return num * 2

# def tripler (num):
    # return num * 3

isMax = True
if isMax:
    fun = lambda num : num * 2
else:
    fun = lambda num : num * 3

var = fun(60)
print (var)