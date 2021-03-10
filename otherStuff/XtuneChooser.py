# Acesses a database and returns a random row
# Author: Caoimhin Vallely

import csv
import random

fileName = "tuneDatabase.csv"

with open(fileName, "rt") as tunes:
    csvReader = csv.reader(tunes)
    tuneOfTheDay = random.choice(list(csvReader))
    print(tuneOfTheDay)