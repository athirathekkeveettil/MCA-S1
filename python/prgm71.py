# program to write a csv file

import csv
fields=['Name','Department','Birth Month']
rows=[['Athira','MCA','November'],['Raju','BCA','March']]

with open('test.csv','w')as f:
    writer=csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
    f.close
