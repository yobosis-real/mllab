
import csv

with open("trainingdata.csv") as file:
    data = list(csv.reader(file))

h = ['0'] * (len(data[0]) - 1)

for row in data:

    if row[-1] == "Yes":

        for i in range(len(h)):

            if h[i] == '0':
                h[i] = row[i]

            elif h[i] != row[i]:
                h[i] = '?'

print("Final Hypothesis:")
print(h)
