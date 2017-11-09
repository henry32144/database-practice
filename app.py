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
	columns = cursor[0].keys()
	for row in cursor:
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

@app.route('/query/select-example', methods=['POST'])
def select_example():
	return render_template('query.html')

@app.route('/query/submit-query', methods=['POST'])
def submit_query():
	return render_template('query.html')

# Database Functions
def get_db():
	db = getattr(g, '_database ', None)
	if db is None:
		db = g._database  = sqlite3.connect(SQLITE_DB_PATH)
		# Enable foreign key check
		db.execute("PRAGMA foreign_keys = ON")
		db.row_factory = sqlite3.Row
	return db

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, '_database '):
		g.db.close()

if __name__ == '__main__':
	app.run(debug=True)

