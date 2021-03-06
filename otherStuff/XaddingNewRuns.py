# programme to add runs/routes to my training database
# Author: Caoimhin Vallely

# N.B. Started again and created a better script - addindNewRuns2.py

from csv import writer

# solution referenced from https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def addNewRun(fileName, newEntry):
    # Open file in append mode
    with open(fileName, 'a+') as f:
        # Create a writer object from csv module
        csv_writer = writer(f)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(newEntry)

row_contents = str(input("What did you do today Caoimhin?: "))
addNewRun('runningDatabase.csv', row_contents)

# to do:
# - automatically add todays date?
# - separate questions for route and distance?