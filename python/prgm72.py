# program to read the csv file and display the content

import csv
with open('test.csv',mode='r')as f:
    file=csv.reader(f)
    for lines in file:
        if lines:print(lines[0],'\t',lines[1],'\t',lines[2])
