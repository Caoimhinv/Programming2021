import csv
from collections import Counter
from collections import defaultdict
words= []
with open('/Users/caoimhinvallely/Desktop/Programming/Programming2021/otherStuff/tuneDatabase.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for col in reader:
         csv_words = col[2].split(" ")
         for i in csv_words:
              words.append(i) 

words_counted = []
for i in words:
    x = words.count(i)
    words_counted.append((i,x))
withoutDupes = list(dict.fromkeys(words_counted))
with open('tuneFrequency.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(withoutDupes)