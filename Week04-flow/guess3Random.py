# Program that asks the computer to guess a number
# until correct
# Author: Caoimhin Vallely

import random

numberToGuess = 30

guess = random.randint(0,100)

while guess != numberToGuess:
    if guess < numberToGuess:
        print ("It's not", guess,"! Too low")
    else:
        print ("It's not", guess,"! Too high")
    guess = random.randint(0,100)

print ("Well done computer! Yes the number was ", numberToGuess)