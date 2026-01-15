## Refer https://flask.palletsprojects.com/en/stable/tutorial/
from datetime import datetime
import os
from sqlalchemy import text
from flask import Flask, jsonify, redirect, render_template,g, request , session, url_for
import requests

from flask_sqlalchemy import SQLAlchemy

from UserService import UserService
from UserRepo import UserRepo
## DEFINITIONS
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = "supersecretkey"  # Replace with a secure key in production



env = os.environ.get("FLASK_ENV", "development")
print("Current Environment: " + env)

if(env == 'development'):
    app.config.from_object('config.DevelopmentConfig')  
else:
    app.config.from_object('config.ProductionConfig')

# Initialize SQLAlchemy
db = SQLAlchemy(app)


@app.context_processor
def inject_user():
    return dict(context_username=session.get("username"),
                context_ext_api=app.config.get("EXT_API"),
                context_debug=app.config.get("DEBUG"),
                context_port=app.config.get("PORT"),
                context_date = datetime.now().strftime("%Y-%m-%d")
                )

@app.before_request
def before_request():
    g.start_time = datetime.now()
    g.user_service = UserService()
    g.user_repo = UserRepo(g.user_service)

# Home  route /
@app.route('/')
def index():
    # Check if user session exists
    if (session.get("username") is not None):
        model = {'username': session.get("username")} 
        return render_template('home.html', model=model)
    else:
        return render_template('login.html') 

## HOME PAGE 
@app.route('/home', methods=['GET','POST'])
def home(): 
    # Check if user session exists
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if (username == 'admin@example.com' and password == 'admin'):
            print(username + " logged in successfully.")
            session["username"] = username
            
            model = {'username': request.form.get('username')}
            
            return render_template('home.html', model=model)
        else:
            return render_template('login.html', error='Invalid Credentials')
    else:
        if (session.get("username") is not None):
            model = {'username': session.get("username")}
            return render_template('home.html', model=model)
        else: 
            return render_template('login.html')
        

## SIGNOUT
@app.route('/signout', methods=['GET','POST'])
def signout():
    session["username"] = None
    session.clear()
    return redirect(url_for('index')) #index  is function name for  login ##url_for withredirect (app.route hosted API endpoint ) is used to redirect

## ABOUT
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('comp_userlist.html',userlist=g.user_repo.get_all_users())


@app.route('/external-users')
def external_users():
    return g.user_repo.get_all_users()

# Add this new API endpoint (after the /external-users route)
@app.route('/getEmployee')
def get_employee():

    try:
        # Execute query to fetch all employees
        employee_service = EmployeeService(None)
        employee_list = employee_service.fetch_employees()
        return render_template('comp_empDBlist.html',userlist=employee_list)
        # return jsonify({
        #     'success': True,
        #     'data': employee_list,
        #     'count': len(employee_list)
        # })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

class EmployeeService():
    def __init__(self, employee_repo: EmployeeRepository):
        self.employee_repo = employee_repo 
    
    def fetch_employees(self):
        employee_repo = EmployeeRepository(self)
        return employee_repo.get_all_employees()

class EmployeeRepository():
    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service
    
    def get_all_employees(self):
        try:
            result = db.session.execute(text("SELECT * FROM employee"))
            employees = result.mappings().all()        
                # Convert to list of dictionaries
            employee_list = [dict(row) for row in employees]
            return employee_list
        except Exception as e:
            print(f"Error fetching employees: {e}")
            return []
    

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



# # SQL Server Connection - Using Integrated Security (Windows Authentication)
# Note: When using Integrated Security=True, DO NOT include username/password
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     "mssql+pyodbc://pyuser:password123@localhost/empDB"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
# )


# API data fetch from SQL Server
# @app.route('/employees')
# def employees():
#     result = db.session.execute(text("SELECT * FROM employee"))
#     return jsonify(result.mappings().all())


#db = SQLAlchemy(app)

# @app.route('/employees')
# def employees():
#     result = db.session.execute(text("SELECT * FROM employees"))
#     return jsonify(result.mappings().all())
#GLobal If you dont want to pass username in every render_template, use a context processor:
# all places You can then use {{con text_username}} in html 