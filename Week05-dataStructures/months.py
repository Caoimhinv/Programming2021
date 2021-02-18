# Create a tuple that stores the months of the year.
# From that tuple create another tuple
# with just the summer months (May, June, July).
# Print out the summer months one at a time.

# Author: Caoimhin Vallely

months = ("January", "February", "March", 
        "April", "May", "June", "July", 
        "August", "September", "October", 
        "November", "December")

summerMonths = months[5:8]

for month in summerMonths:
    print(month)