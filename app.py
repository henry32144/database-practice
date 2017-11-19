import sqlite3
import json
from flask import Flask, render_template, request, g , jsonify

# Initialize flask app.
app = Flask(__name__)

# Sqlite database path.
SQLITE_DB_PATH = 'enterprise.db'

# Database request status.
status_code = { 'operator_warn':"Only SELECT operator is accepted",
                'empty_warn':"Nothing input",
                'success':"Request has been send successful",
                'no_result':"Request successed, but no result",
                'error':"An error occurred:",
}

# Index page route, entry page and homepage, to show employee table preview and basic information.
@app.route('/')
def index():
        
    # Call get database function.
    db = get_db()

    # Select all from employee table.
    cursor = db.execute(
        'SELECT * FROM EMPLOYEE'
    ).fetchall()
    
    employees = []

    # Check if cursor is not empty.
    if cursor:
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

            # Table or data not exist.
            if not employees:
                err_msg = "<p>There are something wrong in database, please Contact me</p>"
                return err_msg, 404
        
    # Render Jinja2 html template module.
    return render_template (
        'index.html', 
        employees = employees
    )

# About page route.
@app.route('/about')
def show_about():
    return render_template('about.html')

# Contact page route.
@app.route('/contact')
def show_contact():
    return render_template('contact.html')

# Query page route.
@app.route('/query')
def show_query():
    return render_template('query.html')

# This route handle GET request, while the query page is loaded.
@app.route('/query/get-query-example', methods=['GET'])
def get_example():
    json_data = ''
    
    # Read json data
    with open('./query_example.json', encoding='utf-8-sig') as json_file:
                json_data = json.load(json_file)
                
    # Return json data
    return jsonify(json_data)

# This route get Text from Textarea, and send to database.
@app.route('/query/submit-query', methods=['POST'])
def submit_query():
    db = get_db()
    status = ''
    
    # Get text from requset.
    query_code = request.form.get('query-text')

    # Get text is not empty.
    if query_code != '':

        # Check if exist invalid operator.
        query_code = string_process(query_code)
        
        # Invalid operator exist, return warn.
        if query_code == 0:
            print('invalid')
            return render_template('query.html',
                status = {'warn':status_code['operator_warn']},
                user_input = query_code)
        
        # Not exist, send code to database.
        else:
            try:
                db = get_db()
                cursor = db.execute(
                    query_code
                ).fetchall()
                results = []

                # Check if result is not empty.
                if cursor:
                        
                    # Get columns names
                    columns = cursor[0].keys()
                    
                    # Append data
                    for row in cursor:
                        current_data = {}
                        count = 0
                        for value in row:
                            current_data.update({columns[count]: value})
                            count+=1
                        results.append(current_data)

                    # Success, return result.
                    return render_template('query.html',
                        status = {'success':status_code['success']},
                        user_input = query_code,
                        columns = columns,
                        results = results)

                # Result is empty, show status message.
                else:
                    return render_template('query.html',
                        status = {'success':status_code['no_result']},
                        user_input = query_code)

            # Something error occure in database, return error message.
            except sqlite3.Error as e:
                return render_template('query.html',
                    status = {'error':status_code['error']},
                    user_input = query_code,
                    error_message = e.args[0])
        
    # If nothing input, return warn message.
    return render_template('query.html',
                status = {'warn':status_code['empty_warn']})

# This function is to get connect to the database.
def get_db():
    db = getattr(g, '_database ', None)
    if db is None:
        db = g._database  = sqlite3.connect(SQLITE_DB_PATH)
        # Enable foreign key check
        db.execute("PRAGMA foreign_keys = ON")
        db.row_factory = sqlite3.Row

        # Check if table exist.
        check_table = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='EMPLOYEE';").fetchone()
        if not check_table:
                with open('create_database.sql', encoding='utf-8') as f:
                        create_db_sql = f.read()
                with db:
                        db.executescript(create_db_sql)
    return db

# This function check invalid text and filter the text.
def string_process(query_str):
    is_valid = True
    query_str = query_str.replace('\'','\"')
    unavaliabe = ['DELETE','DROP','UPDATE','CREATE']
    for i in unavaliabe:
        if query_str.find(i) != -1:
            is_valid = False
    if is_valid != True:
        return 0
    else:
        return query_str

# Close the connection to the database.
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, '_database '):
        g.db.close()

if __name__ == '__main__':
    app.run(debug=True)

