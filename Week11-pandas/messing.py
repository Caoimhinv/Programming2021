# demonstrate reading from TSV and excel
# Author Andrew Beatty

import pandas as pd
import re
import numpy as np
import dataManipulation

filename = '/Users/caoimhinvallely/Desktop/Programming/pands2021/code/week11-Extra pandas/Lecture/originalData.tsv'

df = pd.read_table(filename)
list_of_cols = ['Module ID', 'Duration']
print(df[list_of_cols].head(2))

df['new'] = df['Duration'] * df['Number of Weeks']

list_of_cols = ['Number of Weeks', 'Duration', 'new']
print(df[list_of_cols].head(10))