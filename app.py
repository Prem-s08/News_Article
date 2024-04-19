from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'  # Set a secret key for session management
NEWS_API_URL = 'http://scaleable.eba-hk2jstsk.us-east-1.elasticbeanstalk.com/news'

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if is_logged_in():
        news_data = fetch_news()
        return render_template('index.html', news=news_data)
    else:
        return redirect(url_for('login'))
    
def is_logged_in():
    return 'user_id' in session
    
# Route to render the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

# Route to render the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Check if username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return render_template('signup.html', error='Username or email already exists')
        else:
            # Create a new user
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('index'))
    return render_template('signup.html')

# Function to check if user is logged in
def is_logged_in():
    return 'user_id' in session

# Function to log out the user
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/convert_currency')
def convert_currency():
    return render_template('convert_currency.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

def fetch_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        news_data = response.json()
        return news_data
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True,port=5001)
