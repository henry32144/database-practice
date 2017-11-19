import sqlite3
import json
from flask import Flask, render_template, request, g , jsonify

app = Flask(__name__)
SQLITE_DB_PATH = 'enterprise.db'

status_code = { 'operator_warn':"Only SELECT operator is accepted",
                'empty_warn':"Nothing input",
                'success':"Request has been send successful",
                'no_result':"Request successed, but no result",
                'error':"An error occurred:",
}


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

@app.route('/query/get-query-example', methods=['GET'])
def get_example():
    json_data = ''
    with open('./query_example.json', encoding='utf-8-sig') as json_file:
                json_data = json.load(json_file)

    return jsonify(json_data)

@app.route('/query/submit-query', methods=['POST'])
def submit_query():
    db = get_db()
    status = ''
    query_code = request.form.get('query-text')
    if query_code != '':
        query_code = string_process(query_code)

        if query_code == 0:
            print('invalid')
            return render_template('query.html',
                status = {'warn':status_code['operator_warn']},
                user_input = query_code)
        else:
            try:
                db = get_db()
                cursor = db.execute(
                    query_code
                ).fetchall()
                results = []
                if cursor:
                    columns = cursor[0].keys()
                    for row in cursor:
                        current_data = {}
                        count = 0
                        for value in row:
                            current_data.update({columns[count]: value})
                            count+=1
                        results.append(current_data)

                    return render_template('query.html',
                        status = {'success':status_code['success']},
                        user_input = query_code,
                        columns = columns,
                        results = results)
                else:
                    return render_template('query.html',
                        status = {'success':status_code['no_result']},
                        user_input = query_code)
            except sqlite3.Error as e:
                return render_template('query.html',
                    status = {'error':status_code['error']},
                    user_input = query_code,
                    error_message = e.args[0])
    return render_template('query.html',
                status = {'warn':status_code['empty_warn']})

# Database Functions
def get_db():
    db = getattr(g, '_database ', None)
    if db is None:
        db = g._database  = sqlite3.connect(SQLITE_DB_PATH)
        # Enable foreign key check
        db.execute("PRAGMA foreign_keys = ON")
        db.row_factory = sqlite3.Row
    return db

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


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, '_database '):
        g.db.close()

if __name__ == '__main__':
    app.run(debug=True)

