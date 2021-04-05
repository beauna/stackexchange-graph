import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

# Loading all the JSON files.
scores = json.loads(open('score.json').read())
names = json.loads(open('names.json').read())
years = json.loads(open('years.json').read())
months = json.loads(open('months.json').read())

# Converts years/months to days, this reads from the JSON arrays and converts
# them to integers so they can be multiplied.

days_years = [i * 365 for i in years]
# print(days_years)

days_months = [i * 30 for i in months]
# print(days_months)

# Converted years/months to days, naming convention is dYears = daysYears.
dYears = [4380, 3285, 4380, 4015, 4380, 4380, 4015, 4015, 4380, 4015, 4380, 4380, 4380, 4380, 4015, 4380, 4380, 4015, 4015, 4380, 3650, 4380, 4380, 4380, 2190, 3650, 4380, 4380, 3650, 4015, 4015, 2555, 4380, 4380, 4380, 2920, 4380, 3285, 4015, 4015, 4015, 4380, 4380, 4380, 3285, 4380, 4380, 4380, 4380, 3285]
dMonths = [180, 150, 60, 180, 210, 180, 300, 330, 180, 210, 240, 150, 180, 180, 330, 210, 60, 150, 120, 180, 330, 180, 180, 180, 270, 90, 180, 0, 60, 240, 330, 150, 0, 180, 90, 270, 180, 270, 210, 150, 330, 0, 0, 180, 120, 180, 60, 180, 180, 60]

# Sum of dYears + dMonths (this has been added to the data.json file.)
sumDays = []
for (i, x) in zip(dYears, dMonths):
    sumDays.append(i+x)
# print(sumDays)

# Pandas reading the data.json file.
df = pd.read_json('data.json')

# Create the scatterplot.
# Figure changes the size of the plot, 20 width by 10 height.
fig = plt.figure(figsize=(20, 10))
ax0 = fig.add_subplot()

# Set the tick range for y axis.
ax0.set_yticks(np.arange(500000, 1500000, 100000), minor=False)

# df['days'], df['scores'] is x,y. s is size, alpha is opacity, c is colour.
ax0.scatter(df['days'], df['scores'], s=50, alpha=0.5, c='r')

# Names for axis and title.
plt.title('Top 50 StackExchange Users')
plt.ylabel('Score')
plt.xlabel('Age (days)')
plt.show()
