import sqlite3

db = sqlite3.connect("enterprise.db")

db.row_factory = sqlite3.Row

cursor = db.execute(
        'SELECT * FROM EMPLOYEE'
).fetchall()

employees = []
columns = cursor[0].keys()
for row in cursor:
        current_data = {}
        count = 0
        for value in row:
                current_data.update({columns[count]: value})
                count+=1
        print (current_data)
        employees.append(current_data)

