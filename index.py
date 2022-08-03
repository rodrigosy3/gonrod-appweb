from flask import Flask, request, session, redirect, render_template
import firebase_admin
from firebase_admin import credentials, db
import pyrebase
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firebase_SDK.json")
cred = credentials.Certificate(file_path)
config = {
    'apiKey': "AIzaSyC_uo2GHTS04ooTtU4XqXzPY4eJCxB8hRc",
    'authDomain': "gonrod-14db8.firebaseapp.com",
    'projectId': "gonrod-14db8",
    'storageBucket': "gonrod-14db8.appspot.com",
    'messagingSenderId': "705466489310",
    'appId': "1:705466489310:web:a0a1aa96c9e7eb9f30a54f",
    'measurementId': "G-Q8EYEQ2V2D",
    'databaseURL': "https://gonrod-14db8-default-rtdb.firebaseio.com/"
}
app = Flask(__name__)

firebase = firebase_admin.initialize_app(cred, config)
pyrebase= pyrebase.initialize_app(config)
auth = pyrebase.auth()
app.secret_key = 'secret'

# LOGIN
# @app.route('/<email>', methods=['POST', 'GET'])
# def home(email):
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return "Ocurrio un error"

    if ('user' in session):
        return render_template('home.html')

    return render_template('login.html')

@app.route('/cerrar-sesion')
def logout():
    session.pop('user')
    return redirect('/')

# CATALOGO

# for key, val in snapshot.items():
#     # print('{0} tiene {1} metros de altura'.format(key, val))
#     print("*************************")
#     print('{0}'.format(key, val))
#     print("*************************")

@app.route('/catalogo-de-productos')
def catalogo():
    ref = db.reference('/')
    snapshot = ref.get()
    return render_template('catalogo-de-productos.html', snapshot = snapshot)

if (__name__ == "__main__"):
    app.run(debug=True)
