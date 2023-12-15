# program to write into a csv dict file

import csv
fields=['Name','Department','BirthMonth']
rows=[{'Name':'Athira','Department':'MCA','BirthMonth':'November'},{'Name':'Abhi','Department':'Mtech','BirthMonth':'June'}]

with open('test1.csv','w') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    f.close
