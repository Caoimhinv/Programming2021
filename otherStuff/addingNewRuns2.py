# programme to add runs/routes to my training database
# Author: Caoimhin Vallely

import csv
import datetime

def addNewRun():

    newEntry = open('runningDatabase.csv', 'a')
    w = csv.writer(newEntry)

#   # ref for date - https://datatofish.com/python-current-date/
    Route = input("Where'd we run today Caoimhin?: ")
    Date = str(datetime.datetime.today().strftime ('%d/%m/%Y')) #todays date in my preferred format
    Distance = float(input("How far'd you go?: "))
    distanceRound = round(Distance, 2) # round to 2 decimal places
    w.writerow([Route, Date, distanceRound])  
    print("Database is updated with ", Route, Date, distanceRound)

addNewRun()