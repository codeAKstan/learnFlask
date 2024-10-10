from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', user="codeAKstan")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user_name = request.form['name']
    else:
        user_name = request.args.get('name', 'Guest')  # Default to 'Guest'
    return f"Hello, {user_name}!"



if __name__ == "__main__":
    app.run(debug=True)