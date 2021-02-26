
data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
       {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
       {'first': 'Alan',  'last': 'Turing',     'YOB': 1912}]

# list = [22,33,11,1,44]
# print(list)
# newList = sorted(list)
# print(newList)

def sortFun(item):
    print ("in sortFun")
    return item['last']

# print (data)
# newData = sorted(data, key = sortFun)
# for item in newData:
#     print(item)

# doing the same thing as previous function with lambda
newData = sorted(data, key = lambda item : item['last'])
for item in newData:
    print(item)