# this programme picks 5 random sets of tunes for me to practice each day!
# Author: Caoimhin Vallely

import pandas as pd

df = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', index_col=0)
# opens file containing current tune
with open('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tune_status.txt') as f:
    status = int(f.read())

x = input("Will we move on (or stay put)? y/n :")
if x == 'y':
    # moves to the next tune
    current = status + 1
    df1 = df[0:current]
    # picks a random sample of 5 tunes to practice
    tunesOfTheDay = df1.sample(n=5)
    print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")
    # displays the last 3 tunes learnt
    recentlyLearnedTunes = df1[current-3:current]
    print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes, "\n")
    # prints todays new tune
    todaysNewTune = str(df.iloc[current])
    print("NEW TUNE FOR TODAY:\n ", todaysNewTune, "\n")
    # updates the current tune file
    with open('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tune_status.txt', 'w+') as t:
       t.write(str(current))
else:
    df1 = df[0:status]
    tunesOfTheDay = df1.sample(n=5)
    print("5 TUNES TO REVISE TODAY:\n", tunesOfTheDay, "\n")
    recentlyLearnedTunes = df1[status-4:status-1]
    print ("RECENTLY LEARNED TUNES TO PRACTICE:\n", recentlyLearnedTunes, "\n")
    last_learnt_tune = str(df.iloc[status-1])
    print("LAST LEARNT TUNE TO REVISE:\n ", last_learnt_tune)


