# Testin and reading a csv file
# Author: Caoimhin Vallely

import csv

fileName = "tuneDatabase.csv"

with open(fileName, "rt") as tunes:
    csvReader = csv.reader(tunes, delimiter = ',')
    firstLine = True
    count = 0
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        print(line)