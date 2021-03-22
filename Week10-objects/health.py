# use person module
# author: Andrew Beatty lecture

from personModule import *

person1 = {
    'firstname': 'andrew',
    'lastname': 'beatty',
    'dob': dt.date(2010,1,1),
    'height': 180,
    'weight': 100
}

displayperson(person1)
gethealthdata(person1)