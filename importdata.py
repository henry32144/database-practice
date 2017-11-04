import sqlite3
import csv
                #here
with open('./tables/dependent.csv', newline='') as f:
    csv_reader = csv.DictReader(f)
    #change here
    dependent = [
        (row['Essn'], row['Dependent_name'], row['Sex'], row['Bdate'], row['Relationship'])
        for row in csv_reader
    ]


db = sqlite3.connect('enterprise.db')

with db:
    db.executemany(             
        'INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES (?, ?, ?, ?, ?)',
        #change here
        dependent
    )
                        
c = db.execute('SELECT * FROM DEPENDENT')
for row in c:
    print(row)
