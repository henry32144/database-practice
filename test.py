import sqlite3

db = sqlite3.connect("enterprise.db")

db.row_factory = sqlite3.Row

cursor = db.execute(
        'SELECT * FROM EMPLOYEE'
).fetchall()

employees = []
columns = cursor[0].keys()
for row in cursor:
        print()
        employees.append({
                columns[0]: row[0],
                columns[1]: row[1],
                columns[2]: row[2],
                columns[3]: row[3],
                columns[4]: row[4],
                columns[5]: row[5],
                columns[6]: row[6],
                columns[7]: row[7],
                columns[8]: row[8],
                columns[9]: row[9],
        })

