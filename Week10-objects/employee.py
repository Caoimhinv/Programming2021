# Author: Andrew Beatty lab

import datetime as dt
from timeSheetEntry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __str__(self):
        return self.first + ' ' + self.last

    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timeSheetEntry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timeSheetEntry)

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

if __name__ == '__main__':
    test = Employee('some', 'one')
    print (test)
    assert ('some one' == str(test))
    test.logminutes('pl', 30)
    test.logminutes('pl', 60)
    mins = test.gettotaltime()
    print (mins)
    assert(mins == 90)
    print ('all good')