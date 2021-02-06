# program to convert float amount of dollars to absolute number in cents
# Author: Caoimhin Vallely

amount = float(input('Please enter an amount in dollars:'))
amountInCents = abs(amount * 100) # finds absolute value of number
amountInCentsInt = int(amountInCents) #casts float to int
print('That amount in cent is {}c'.format(amountInCentsInt))