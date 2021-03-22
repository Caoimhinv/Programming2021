# demonstration of a module
# Author: Andrew Beatty lecture

import datetime as dt

def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__ == '__main__':
    person1 = {
        'firstname': 'andrew',
        'lastname': 'beatty',
        'dob': dt.date(2010,1,1),
        'height': 180,
        'weight': 100
    }

    displayperson(person1)
    gethealthdata(person1)
