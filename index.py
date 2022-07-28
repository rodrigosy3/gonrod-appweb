from flask import Flask, request, session, redirect, render_template
import pyrebase

app = Flask(__name__)
config = {
    'apiKey': "AIzaSyC_uo2GHTS04ooTtU4XqXzPY4eJCxB8hRc",
    'authDomain': "gonrod-14db8.firebaseapp.com",
    'projectId': "gonrod-14db8",
    'storageBucket': "gonrod-14db8.appspot.com",
    'messagingSenderId': "705466489310",
    'appId': "1:705466489310:web:a0a1aa96c9e7eb9f30a54f",
    'measurementId': "G-Q8EYEQ2V2D",
    'databaseURL': ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app.secret_key = 'secret'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return "Correo o contraseña incorrecta"

    if ('user' in session):
        return render_template('home.html')
    
    return render_template('login.html')

@app.route('/cerrar-sesion')
def logout():
    session.pop('user')
    return redirect('/')

if (__name__ == "__main__"):
    app.run(debug=True)