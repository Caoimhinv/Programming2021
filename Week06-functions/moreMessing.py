import random

def sqrt():
    L=[]
    global number
    number = float(input("enter a postive number: "))
    A = random.uniform(1, number)
    while len(L) < 10:
        A = 0.5 * ((number / A) + A)
        L.append(A)
    return L

var = sqrt()
print("The square root of ", number, "is approximately ", var[9])