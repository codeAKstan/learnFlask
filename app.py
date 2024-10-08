from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home page", user="codeAKstan")

@app.route('/items')
def items():
    items = ['apple', 'banana', 'grape', 'strawberry']
    return render_template('items.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)