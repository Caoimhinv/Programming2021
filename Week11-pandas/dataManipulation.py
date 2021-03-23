# this module is for functions that I need to 
# do data manipulation
# Author: Andrew Beatty

'''
this gets a series of you unique values from a column that contains 
some of the values in a delimited form
'''
import pandas as pd
import random
import re

def getSeriesOfUnique(dataFrame, nameOfCol, delim = '/'):

    # drop na gets rid of the values in the series that have no value
    # this actually returns a numpy.ndarray
    valuesWithDelims = dataFrame[nameOfCol].dropna().unique()

    # iterate through it and break up the delimited values
    # I am using a set becaue this will remove duplicates as I add them
    # yes I am sure there is a more efficient way of doing this
    uniqueValues = set([])  # empty set
    for valueInCol in valuesWithDelims:
        #print (staff, ":", type(staff)) # for debugging
        valueAsList = re.split('/', valueInCol)
        uniqueValues.update(valueAsList)
    ds = pd.Series(list(uniqueValues))
    # I take the liberty of sorting this series
    ds.sort_values()
    return ds