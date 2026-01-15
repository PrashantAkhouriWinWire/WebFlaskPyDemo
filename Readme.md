# Installation 
pip install

# Initaite the Web (app.py)

app=Flask(__name__)

# craete API 
@app.route('/home') 
 def home():
   return render_template('home.html', model=data)

or 
   redirect(url_for('home'))


# create Templalt folder ( for Html )
 templates
  -- home.html
  -- login.html 
  -- comp_userlist.html
- return render tenplate 
return render_template('home.html', model=data)

# Inline html script rendering  (  {%    %}) 

Eg  
{% if userlist is none %}
    <p>No users found.</p>
{% else %}
{% for user in userlist %}
<table class="table table-bordered">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{{ user.id }}</td>
            <td>{{ user.name | upper }}</td>
            <td>{{ user.email }}</td>
        </tr>
    </tbody>
</table>
<br>

{% endfor %}
{% endif %}


# Inline Html  value rendering  {{ variableValue }} 
Eg.
  <div>{{ username }}</div>
## With Decoratores 
like uppercase 
<div>{{ username | upper }}</div> 


# Sub Section Html Rending  

- Subsection HTML ( {% include <htmlfilename> %})
- Child Component section  { %block tiltle/comntent %} {% endblock %}
Eg.
- home.html ( parent Html file )
<title>{% block title %}Home Page{% endblock %}</title>
<body>
   {% include 'navbar.html' %} 
    {% block content %}
   <div> Loading....</div> 
    {% endblock %}

- comp_userlist.html (child )

{%extends "home.html" %}
{% block title %}User List{% endblock %}
{% block content %}
<div> ALl your child design html </div>
{% end block %}


# Session and Cookies 
from flask import request

- Session 
session.clear() 
GET - sessions.get("user)  or session["user]
SET - session["user"] = value

- cookies 

# form 

Same as old form process 
login.html
------
<form method="POST" action="/home">
<input type=text name="username" >
<input type="submit">Submit</input>
</form>

main.py
----------
@app.route("/home",method=["POST"])
def home():
 username = requests.form.get("username")  [ or request.form["username] ]

# DB COnnnectionns 
sqlelite or SQLAlchemy 
pyodbc for SQL Server
first pip install 

# DEPLOYMENT 
refer docker file