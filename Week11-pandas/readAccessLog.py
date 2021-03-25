import pandas as pd 

path = '/Users/caoimhinvallely/Desktop/Programming/Programming2021/Week11-pandas/'
log_filename = path + 'access.log'

col_names= ('ip',
    'dash1',
    'userId'
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno'
)

df = pd.read_csv(log_filename, sep=' ', header= None, names=col_names)

df.drop(columns=['dash1', 'userId'], inplace=True)
print(df)

