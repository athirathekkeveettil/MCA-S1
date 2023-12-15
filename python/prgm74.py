# program to raed and display from csv dict file

import csv
with open('test1.csv','r')as f:
    file=csv.DictReader(f)
    for lines in file:
        if lines:
          print(lines['Name'],'\t',lines['Department'],'\t',lines['BirthMonth'])
