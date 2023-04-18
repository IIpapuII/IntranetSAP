from flask import Flask
from flask import render_template, request, redirect, session, abort

app = Flask(__name__)
app.secret_key = 'wilmer'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['password'] == 'wilmer':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return home()
    
    if 'username' in session:
        print(session)
        return render_template("home.html")
    return render_template("index.html")

@app.route('/home')
def home():
    if 'username' in session:
        return render_template("home.html")
    return redirect('/')


