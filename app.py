import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)
SQLITE_DB_PATH = 'enterprise.db'




@app.route('/')
def index():
	db = get_db()
	cursor = db.execute(
		'SELECT * FROM EMPLOYEE'
	).fetchall()
	employees = []
	for row in cursor:
		employees.append({
			'Fname': row[0],
			'Minit': row[1],
			'Lname': row[2],
			'Ssn': row[3],
			'Bdate': row[4],
			'Address': row[5],
			'Sex': row[6],
			'Salary': row[7],
			'Super_ssn': row[8],
			'Dno': row[9],
		})
	if not employees:
		err_msg = "<p>There are something wrong in database, please Contact me</p>"
		return err_msg, 404
	return render_template (
		'index.html', 
		employees = employees
	)

@app.route('/about')
def show_about():
	return render_template('about.html')

@app.route('/contact')
def show_contact():
	return render_template('contact.html')

@app.route('/query')
def show_query():
	return render_template('query.html')



# Database Functions
def get_db():
	db = getattr(g, '_database ', None)
	if db is None:
		db = g._database  = sqlite3.connect(SQLITE_DB_PATH)
		# Enable foreign key check
		db.execute("PRAGMA foreign_keys = ON")
	return db

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, '_database '):
		g.db.close()

if __name__ == '__main__':
	app.run(debug=True)

