from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h2>About Page</h2><p>This is the about page.</p>"

@app.route('/contact')
def contact():
    return "<h2>Contact Page</h2><p>Contact us at contact@example.com</p>"


@app.route('/user/<username>')
def show_user_profile(username):
    return f"<h2>User Profile</h2><p>Hello, {username}!</p>"

if __name__ == '__main__':
    app.run(debug=True)
