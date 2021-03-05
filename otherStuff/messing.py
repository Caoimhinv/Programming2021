# Testin and reading a csv file
# Author: Caoimhin Vallely

import csv

fileName = "runningDatabase.csv"

with open(fileName, "rt") as running:
    csvReader = csv.reader(running, delimiter = ',')
    firstLine = True
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        print(line[2])