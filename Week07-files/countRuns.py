# filename = "count.txt"

import os.path
filename = "cunt.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    # initialise file here
    writeNumber(0)
else:
    print("Hi")

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))
    
# main
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)