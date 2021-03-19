# experimtnenting with try/except
# author: Andrew Beatty

# filename = 'data.txt'

import sys

# print (sys.argv)
filename = sys.argv[1]

try:
    with open(filename) as f:
        print(f.read())
    var = 10/0
except FileNotFoundError as e:
    #print ("file (", filename, ") does not exist")
# except:
#     print ("An exception ocurred")
    print(e)
    
print ("The End")
