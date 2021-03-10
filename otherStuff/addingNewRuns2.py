# programme to add runs/routes to my training database
# Author: Caoimhin Vallely

import csv
import datetime

def addNewRun():

    newEntry = open('runningDatabase.csv', 'a')
    w = csv.writer(newEntry)

#   # ref for date - https://datatofish.com/python-current-date/
    Route = input("Where'd we run today Caoimhin (as a string)?: ")
    Date = str(datetime.datetime.today().strftime ('%d/%m/%Y'))
    Distance = float(input("How far'd you go?: "))
    distanceRound = round(Distance, 2)
    w.writerow([Route, Date, distanceRound])  
    print("Database updated with ", Route, Date, distanceRound)

addNewRun()